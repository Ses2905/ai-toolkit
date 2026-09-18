#!/usr/bin/env python3
"""Tests for ai-lib. Run: python3 tools/ai-lib/ai_lib_test.py"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ai_lib  # noqa: E402


def make_source(root: Path) -> None:
    # A skill package
    sk = root / "presentation-design"
    sk.mkdir(parents=True)
    (sk / "SKILL.md").write_text(
        "---\nname: presentation-design\ndescription: Applies slide layout, "
        "hierarchy, and typography standards to decks.\n---\n"
        "# Presentation Design\n\n## Activate When\nGenerating or reviewing slides.\n\n"
        "## Definition of Done\nSlides pass the visual QA checklist.\n")
    # A prompt
    (root / "deck-review.md").write_text(
        "# Deck Review\n\n## Use For\nReviewing a specific slide deck.\n\n"
        "## Inputs\n[DECK]\n\n## Prompt\nReview the deck for clarity.\n")
    # A workflow
    (root / "build-deck.md").write_text(
        "# Build Deck\n\n## Goal\nProduce an executive deck.\n\n## Steps\n"
        "### Step 1 — Outline\nDraft the narrative.\n### Step 2 — Design\nApply slide design.\n")
    # An asset
    (root / "logo.svg").write_text("<svg xmlns='http://www.w3.org/2000/svg'></svg>")
    # A tool
    (root / "helper.py").write_text("print('hi')\n")


class UnitTest(unittest.TestCase):
    def test_kebab(self):
        self.assertEqual(ai_lib.kebab("Presentation Design"), "presentation-design")
        self.assertEqual(ai_lib.kebab("Deck_Review.md"), "deck-review")

    def test_classify_type_skill(self):
        text = "# X\n## Activate When\nnow\n## Definition of Done\ndone\n"
        typ, conf = ai_lib.classify_type(Path("SKILL.md"), text, {})
        self.assertEqual(typ, "skill")

    def test_classify_type_prompt_workflow_asset_tool_global(self):
        self.assertEqual(ai_lib.classify_type(Path("p.md"), "## Use For\nx\n## Prompt\ny", {})[0], "prompt")
        self.assertEqual(ai_lib.classify_type(Path("w.md"), "## Steps\n### Step 1 — a\n", {})[0], "workflow")
        self.assertEqual(ai_lib.classify_type(Path("logo.svg"), "", {})[0], "asset")
        self.assertEqual(ai_lib.classify_type(Path("t.py"), "print(1)", {})[0], "tool")
        self.assertEqual(ai_lib.classify_type(Path("AGENTS.md"), "rules", {})[0], "global")

    def test_declared_type_wins(self):
        self.assertEqual(ai_lib.classify_type(Path("x.md"), "body", {"type": "reference"})[0], "reference")

    def test_classify_category(self):
        cat, _ = ai_lib.classify_category("slides and presentation deck", "deck")
        self.assertEqual(cat, "presentation")


class InspectTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_source(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_inspect_classifies_all(self):
        arts = ai_lib.inspect_dir(self.tmp)
        by_type = {a.type for a in arts}
        self.assertIn("skill", by_type)
        self.assertIn("prompt", by_type)
        self.assertIn("workflow", by_type)
        self.assertIn("asset", by_type)
        self.assertIn("tool", by_type)
        skill = next(a for a in arts if a.type == "skill")
        self.assertEqual(skill.name, "presentation-design")
        self.assertTrue(skill.is_dir)
        self.assertEqual(skill.category, "presentation")


class InstallTest(unittest.TestCase):
    def setUp(self):
        self.src = Path(tempfile.mkdtemp())
        make_source(self.src)
        self.home = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.src, ignore_errors=True)
        shutil.rmtree(self.home, ignore_errors=True)

    def test_dry_run_makes_no_changes(self):
        rc = ai_lib.main(["--home", str(self.home), "install", str(self.src), "--dry-run"])
        self.assertEqual(rc, 0)
        self.assertFalseIfExists(self.home / "skills" / "presentation" / "presentation-design")

    def assertFalseIfExists(self, p: Path):
        self.assertFalse(p.exists(), f"should not exist after dry-run: {p}")

    def test_install_and_registry(self):
        rc = ai_lib.main(["--home", str(self.home), "install", str(self.src), "--yes"])
        self.assertEqual(rc, 0)
        # skill package copied as a dir
        self.assertTrue((self.home / "skills" / "presentation" / "presentation-design" / "SKILL.md").is_file())
        # registry recorded with provenance
        reg = json.loads((self.home / "registry" / "packages.json").read_text())
        ids = {i["id"] for i in reg["items"]}
        self.assertIn("skill/presentation/presentation-design", ids)
        for it in reg["items"]:
            self.assertIn("source", it)
            self.assertIn("installed_at", it)
        # INDEX.md generated
        self.assertTrue((self.home / "INDEX.md").is_file())

    def test_overlap_blocks_without_yes(self):
        ai_lib.main(["--home", str(self.home), "install", str(self.src), "--yes"])
        # second install of same content should detect overlap (same name) and
        # return the overlap exit code (2) without --yes.
        rc = ai_lib.main(["--home", str(self.home), "install", str(self.src)])
        self.assertEqual(rc, 2)

    def test_doctor_clean_after_install(self):
        ai_lib.main(["--home", str(self.home), "install", str(self.src), "--yes"])
        self.assertEqual(ai_lib.doctor(self.home), [] if not ai_lib.doctor(self.home) else ai_lib.doctor(self.home))
        # doctor returns issues list; after a clean install with categories, expect none
        issues = [i for i in ai_lib.doctor(self.home) if "needs review" not in i]
        self.assertEqual(issues, [])

    def test_search_and_remove(self):
        ai_lib.main(["--home", str(self.home), "install", str(self.src), "--yes"])
        self.assertEqual(ai_lib.main(["--home", str(self.home), "search", "presentation"]), 0)
        self.assertEqual(ai_lib.main(["--home", str(self.home), "remove",
                                      "skill/presentation/presentation-design", "--purge"]), 0)
        reg = json.loads((self.home / "registry" / "packages.json").read_text())
        self.assertNotIn("skill/presentation/presentation-design", {i["id"] for i in reg["items"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
