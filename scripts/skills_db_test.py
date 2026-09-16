#!/usr/bin/env python3
"""Tests for scripts/skills_db.py. Run: python3 scripts/skills_db_test.py"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import skills_db  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Expected category distribution for the current repo (48 skills).
EXPECTED_COUNTS = {
    "Product & Discovery": 18,
    "Design & Frontend": 9,
    "Motion & Animation": 6,
    "Presentations & Diagrams": 6,
    "Engineering Workflow": 5,
    "Setup & Install": 4,
}


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

    def test_yaml_and_minimal_agree(self):
        got = skills_db.parse_frontmatter(self.SAMPLE)
        self.assertEqual(got["name"], "demo")
        self.assertEqual(got["type"], "component")
        self.assertEqual(got["theme"], "pm-artifacts")
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


class ScoreTest(unittest.TestCase):
    def _skill(self, **kw):
        base = dict(
            name="x", category="Engineering Workflow", type="", theme="",
            description="", argument_hint="", best_for=[], command="",
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
        lean_score, _ = skills_db.score_skill(lean)
        rich_score, _ = skills_db.score_skill(rich)
        self.assertGreater(rich_score, lean_score)
        self.assertEqual(rich_score, 100)


class RepoScanTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = skills_db.scan_skills(ROOT)
        cls.by_name = {s.name: s for s in cls.skills}

    def test_total(self):
        self.assertEqual(len(self.skills), 48)

    def test_no_uncategorized(self):
        unc = [s.name for s in self.skills if s.category == skills_db.UNCATEGORIZED]
        self.assertEqual(unc, [], f"uncategorized skills: {unc}")

    def test_category_counts(self):
        counts = {c: sum(1 for s in self.skills if s.category == c) for c in skills_db.CATEGORIES}
        self.assertEqual(counts, EXPECTED_COUNTS)

    def test_command_linking_by_body_reference(self):
        # plan.md references skills/plan-the-work/ -> command should be "plan"
        self.assertEqual(self.by_name["plan-the-work"].command, "plan")
        self.assertEqual(self.by_name["debug-from-evidence"].command, "debug")
        self.assertEqual(self.by_name["capture-a-skill"].command, "new-skill")
        self.assertTrue(self.by_name["plan-the-work"].has_command)

    def test_ranks_are_dense_and_ordered(self):
        overall = sorted(s.rank_overall for s in self.skills)
        self.assertEqual(overall, list(range(1, len(self.skills) + 1)))
        top = min(self.skills, key=lambda s: s.rank_overall)
        self.assertEqual(top.rank_overall, 1)
        self.assertEqual(top.score, max(s.score for s in self.skills))

    def test_rank_in_category_is_dense(self):
        for c in skills_db.CATEGORIES:
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
        results = skills_db.search(self.skills, "")
        self.assertEqual(len(results), len(self.skills))


class BuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = skills_db.scan_skills(ROOT)

    def test_index_shape(self):
        idx = skills_db.build_index(self.skills)
        self.assertEqual(idx["total"], 48)
        self.assertEqual(idx["categories"], skills_db.CATEGORIES)
        self.assertEqual(sum(idx["counts_by_category"].values()), 48)
        # skills sorted by overall rank
        first = idx["skills"][0]
        self.assertEqual(first["rank_overall"], 1)

    def test_html_embeds_valid_json(self):
        html = skills_db.render_html(self.skills)
        marker = "const DB = "
        start = html.index(marker) + len(marker)
        end = html.index(";\nconst state", start)
        data = json.loads(html[start:end].replace("<\\/", "</"))
        self.assertEqual(data["total"], 48)

    def test_markdown_has_all_categories(self):
        md = skills_db.render_markdown(self.skills)
        for c in skills_db.CATEGORIES:
            self.assertIn(f"## {c}", md)


if __name__ == "__main__":
    unittest.main(verbosity=2)
