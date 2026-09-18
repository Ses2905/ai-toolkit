#!/usr/bin/env python3
"""Tests for scripts/skills_db.py. Run: python3 scripts/skills_db_test.py

Deliberately count-agnostic: the kit grows over time, so tests assert
invariants (every skill categorized-and-counted, dense ranks, live API works)
rather than hard-coding the number of skills.
"""

from __future__ import annotations

import json
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import skills_db  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def _skill_md_count(root: Path) -> int:
    n = 0
    for rel in skills_db.SKILL_ROOTS:
        base = root / rel
        if base.is_dir():
            n += len(list(base.glob("*/SKILL.md")))
    return n


class FrontmatterTest(unittest.TestCase):
    SAMPLE = (
        "---\n"
        "name: demo\n"
        'description: A short desc. Use when testing.\n'
        "type: component\n"
        "theme: pm-artifacts\n"
        "best_for:\n"
        '  - "One thing"\n'
        '  - "Another thing"\n'
        "intent: >-\n"
        "  Multi line\n"
        "  intent text.\n"
        "---\n"
        "# Body\n"
    )

    def test_parse(self):
        got = skills_db.parse_frontmatter(self.SAMPLE)
        self.assertEqual(got["name"], "demo")
        self.assertEqual(got["best_for"], ["One thing", "Another thing"])

    def test_minimal_parser_directly(self):
        block = skills_db._split_frontmatter(self.SAMPLE)
        data = skills_db._minimal_yaml(block)
        self.assertEqual(data["name"], "demo")
        self.assertEqual(data["best_for"], ["One thing", "Another thing"])
        self.assertIn("intent text.", data["intent"])

    def test_no_frontmatter(self):
        self.assertEqual(skills_db.parse_frontmatter("no frontmatter here"), {})


class CategorizeTest(unittest.TestCase):
    def test_explicit_name_wins(self):
        self.assertEqual(skills_db.categorize("apple-design", "", ""), "Design & Frontend")

    def test_theme_maps(self):
        self.assertEqual(
            skills_db.categorize("some-new-pm-skill", "discovery-research", ""),
            "Product & Discovery",
        )

    def test_keyword_fallback(self):
        self.assertEqual(
            skills_db.categorize("mystery", "", "Add a spring animation to the hero"),
            "Motion & Animation",
        )
        self.assertEqual(
            skills_db.categorize("mystery2", "", "Install the CLI and set up auth"),
            "Setup & Install",
        )
        self.assertEqual(
            skills_db.categorize("mystery3", "", "Write a handoff brief for the next session"),
            "Engineering Workflow",
        )


class ScoreTest(unittest.TestCase):
    def _skill(self, **kw):
        base = dict(
            name="x", source_root="skills", category="Engineering Workflow", type="",
            theme="", description="", argument_hint="", best_for=[], command="",
            has_command=False, has_rule=False, has_scripts=False, has_tests=False,
            has_examples=False, has_docs=False, file_count=1, skill_md_bytes=1000,
            in_catalog=False, in_readme=False,
        )
        base.update(kw)
        return skills_db.Skill(**base)

    def test_bounds(self):
        low = self._skill()
        low.score, _ = skills_db.score_skill(low)
        self.assertGreaterEqual(low.score, 0)
        self.assertLessEqual(low.score, 100)

    def test_more_signals_score_higher(self):
        lean = self._skill()
        rich = self._skill(
            description="d", best_for=["a"], type="component", theme="pm-artifacts",
            command="x", has_command=True, has_rule=True, has_scripts=True,
            has_tests=True, has_examples=True, has_docs=True, file_count=40,
            skill_md_bytes=40000, in_catalog=True, in_readme=True,
        )
        self.assertGreater(skills_db.score_skill(rich)[0], skills_db.score_skill(lean)[0])
        self.assertEqual(skills_db.score_skill(rich)[0], 100)


class RepoScanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = skills_db.scan_skills(ROOT)
        cls.by_name = {s.name: s for s in cls.skills}

    def test_total_matches_filesystem(self):
        self.assertEqual(len(self.skills), _skill_md_count(ROOT))
        self.assertGreater(len(self.skills), 0)

    def test_counts_sum_to_total(self):
        idx = skills_db.build_index(self.skills)
        self.assertEqual(sum(idx["counts_by_category"].values()), len(self.skills))
        # every skill's category is represented in the index categories
        for s in self.skills:
            self.assertIn(s.category, idx["categories"])

    def test_known_skills_categorized(self):
        cases = {
            "apple-design": "Design & Frontend",
            "product-strategy-session": "Product & Discovery",
            "hyperframes-animation": "Motion & Animation",
            "plan-the-work": "Engineering Workflow",
            "install-work-kit": "Setup & Install",
        }
        for name, cat in cases.items():
            if name in self.by_name:
                self.assertEqual(self.by_name[name].category, cat, name)

    def test_multi_root_scanning(self):
        # gpt-taste lives under .agents/skills; it must be discovered with its root.
        if ".agents/skills" in skills_db.SKILL_ROOTS and (ROOT / ".agents/skills").is_dir():
            self.assertIn("gpt-taste", self.by_name)
            self.assertEqual(self.by_name["gpt-taste"].source_root, ".agents/skills")

    def test_command_linking_by_body_reference(self):
        self.assertEqual(self.by_name["plan-the-work"].command, "plan")
        self.assertEqual(self.by_name["debug-from-evidence"].command, "debug")
        self.assertEqual(self.by_name["capture-a-skill"].command, "new-skill")
        self.assertTrue(self.by_name["plan-the-work"].has_command)

    def test_ranks_are_dense_and_ordered(self):
        overall = sorted(s.rank_overall for s in self.skills)
        self.assertEqual(overall, list(range(1, len(self.skills) + 1)))
        top = min(self.skills, key=lambda s: s.rank_overall)
        self.assertEqual(top.score, max(s.score for s in self.skills))

    def test_rank_in_category_is_dense(self):
        for c in skills_db.present_categories(self.skills):
            group = [s for s in self.skills if s.category == c]
            ranks = sorted(s.rank_in_category for s in group)
            self.assertEqual(ranks, list(range(1, len(group) + 1)))


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = skills_db.scan_skills(ROOT)

    def test_exact_name_ranks_first(self):
        results = skills_db.search(self.skills, "plan-the-work")
        self.assertEqual(results[0][0].name, "plan-the-work")

    def test_topic_query(self):
        results = skills_db.search(self.skills, "animation")
        self.assertTrue(results)
        self.assertEqual(results[0][0].category, "Motion & Animation")

    def test_empty_query_returns_all(self):
        self.assertEqual(len(skills_db.search(self.skills, "")), len(self.skills))


class BuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = skills_db.scan_skills(ROOT)

    def test_index_shape(self):
        idx = skills_db.build_index(self.skills)
        self.assertEqual(idx["total"], len(self.skills))
        self.assertEqual(idx["skills"][0]["rank_overall"], 1)

    def test_html_embeds_valid_json(self):
        html = skills_db.render_html(self.skills)
        marker = "let DB = "
        start = html.index(marker) + len(marker)
        end = html.index(";\nconst LIVE", start)
        data = json.loads(html[start:end].replace("<\\/", "</"))
        self.assertEqual(data["total"], len(self.skills))

    def test_html_has_refresh_and_live_api(self):
        html = skills_db.render_html(self.skills)
        self.assertIn('id="refresh"', html)
        self.assertIn("/api/refresh", html)
        self.assertIn("/api/skills", html)

    def test_markdown_has_present_categories(self):
        md = skills_db.render_markdown(self.skills)
        for c in skills_db.present_categories(self.skills):
            self.assertIn(f"## {c}", md)


class ServeTest(unittest.TestCase):
    """Boots the real handler on an ephemeral port and hits the live API."""

    @classmethod
    def setUpClass(cls):
        # Refresh rewrites artifacts; send them to a temp dir so the repo tree
        # is not mutated by the test run.
        cls.tmp = tempfile.mkdtemp(prefix="skills-db-test-")

        class Bound(skills_db._DBHandler):
            pass
        Bound.root = ROOT
        Bound.build_paths = {
            "json": f"{cls.tmp}/skills-index.json",
            "md": f"{cls.tmp}/SKILLS.md",
            "html": f"{cls.tmp}/skills-database.html",
        }
        cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Bound)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _get(self, path, method="GET"):
        req = urllib.request.Request(f"http://127.0.0.1:{self.port}{path}", method=method)
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, r.read()

    def test_index_html(self):
        status, body = self._get("/")
        self.assertEqual(status, 200)
        self.assertIn(b"Work Kit", body)

    def test_api_skills(self):
        status, body = self._get("/api/skills")
        self.assertEqual(status, 200)
        data = json.loads(body)
        self.assertEqual(data["total"], _skill_md_count(ROOT))

    def test_api_refresh(self):
        status, body = self._get("/api/refresh", method="POST")
        self.assertEqual(status, 200)
        data = json.loads(body)
        self.assertTrue(data.get("refreshed"))
        self.assertEqual(data["total"], _skill_md_count(ROOT))

    def test_404(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self._get("/nope")
        self.assertEqual(ctx.exception.code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
