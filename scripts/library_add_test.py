#!/usr/bin/env python3
"""Tests for scripts/library-add.py. Run: python3 scripts/library_add_test.py

Routes into a temp copy of the repo skeleton so the real tree is never touched.
"""

from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
# import the hyphenated module by path
_spec = importlib.util.spec_from_file_location("library_add", ROOT / "scripts" / "library-add.py")
library_add = importlib.util.module_from_spec(_spec)
sys.path.insert(0, str(ROOT / "tools" / "ai-lib"))
_spec.loader.exec_module(library_add)


class ClassifyTest(unittest.TestCase):
    def test_prompt(self):
        typ, cat, name = library_add.classify("## Use For\nreview a deck\n## Prompt\ndo it", None, "deck-review")
        self.assertEqual(typ, "prompt")
        self.assertEqual(name, "deck-review")

    def test_skill(self):
        text = "# X\n## Activate When\nnow\n## Definition of Done\ndone"
        self.assertEqual(library_add.classify(text, None, "x")[0], "skill")

    def test_workflow(self):
        text = "## Steps\n### Step 1 — a\n### Step 2 — b"
        self.assertEqual(library_add.classify(text, None, "flow")[0], "workflow")

    def test_kind_override(self):
        self.assertEqual(library_add.classify("whatever", "reference", "r")[0], "reference")

    def test_frontmatter_added_when_missing(self):
        out = library_add.ensure_frontmatter("## Use For\nx", "prompt", "product", "thing")
        self.assertTrue(out.startswith("---"))
        self.assertIn("type: prompt", out)

    def test_frontmatter_preserved(self):
        src = "---\nname: keep\n---\n# Keep\nbody"
        self.assertEqual(library_add.ensure_frontmatter(src, "prompt", "x", "keep"), src)


class RouteWriteTest(unittest.TestCase):
    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        for d in ("scripts", "skills", "prompts/commands", "workflows", "references", "templates", "tools/ai-lib"):
            (self.repo / d).mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "tools" / "ai-lib" / "ai_lib.py", self.repo / "tools" / "ai-lib" / "ai_lib.py")
        # Place the script at scripts/ so its parent.parent resolves to the temp repo.
        shutil.copy2(ROOT / "scripts" / "library-add.py", self.repo / "scripts" / "library-add.py")
        self._spec = importlib.util.spec_from_file_location("library_add_tmp", self.repo / "scripts" / "library-add.py")
        self.mod = importlib.util.module_from_spec(self._spec)
        sys.path.insert(0, str(self.repo / "tools" / "ai-lib"))
        self._spec.loader.exec_module(self.mod)

    def tearDown(self):
        shutil.rmtree(self.repo, ignore_errors=True)

    def test_prompt_lands_in_prompt_kit(self):
        rc = self.mod.main(["--kind", "prompt", "--name", "deck-review", "--category", "presentation",
                            "## Use For\nreview a deck\n## Prompt\ndo it"])
        self.assertEqual(rc, 0)
        self.assertTrue((self.repo / "prompts" / "commands" / "deck-review.md").is_file())

    def test_skill_lands_in_work_kit(self):
        rc = self.mod.main(["--kind", "skill", "--name", "visual-qa",
                            "# Visual QA\n## Activate When\nreviewing UI\n## Definition of Done\npasses"])
        self.assertEqual(rc, 0)
        self.assertTrue((self.repo / "skills" / "visual-qa" / "SKILL.md").is_file())

    def test_no_overwrite(self):
        args = ["--kind", "prompt", "--name", "dup", "## Prompt\nx"]
        self.assertEqual(self.mod.main(args), 0)
        self.assertEqual(self.mod.main(args), 2)  # refuses to overwrite

    def test_dry_run_writes_nothing(self):
        rc = self.mod.main(["--kind", "skill", "--name", "ghost", "--dry-run", "# G\nbody"])
        self.assertEqual(rc, 0)
        self.assertFalse((self.repo / "skills" / "ghost").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
