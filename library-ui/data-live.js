/* Library UI — data synthesis (single source of truth).
   buildLibraryData(catalog) turns catalog/skills-index.json into the shape the
   UI consumes: real skills + prompts, plus synthesized workflows, references,
   tools, projects, integrations, inbox, updates, health and activity so the
   still-sparse tiers show realistic content.

   Used two ways:
     - at runtime by app.js (live fetch of the real catalog), and
     - at build time by build-data.mjs (renders the committed data.js fallback).
   Keeping one implementation means the live view and the snapshot never drift. */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.buildLibraryData = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  // Mirror Python's str.title(): uppercase a letter iff the previous char is
  // not a letter (so "a11y-audit" -> "A11Y Audit"), lowercase otherwise.
  function titleOf(name) {
    const s = String(name).replace(/[-_]/g, " ");
    let out = "", prevAlpha = false;
    for (const ch of s) {
      const isAlpha = ch >= "a" && ch <= "z" || ch >= "A" && ch <= "Z";
      out += isAlpha ? (prevAlpha ? ch.toLowerCase() : ch.toUpperCase()) : ch;
      prevAlpha = isAlpha;
    }
    return out;
  }

  function buildLibraryData(catalog) {
    const items = [];
    const byName = {};

    for (const s of catalog.skills) {
      const it = {
        id: `${s.kind || "skill"}:${s.name}`,
        name: s.name,
        title: titleOf(s.name),
        kind: s.kind || "skill",
        category: s.category || "Uncategorized",
        description: s.description || "",
        summary: s.summary || s.description || "",
        best_use: s.best_use || "",
        watch_outs: s.watch_outs || "",
        command: s.command || "",
        argument_hint: s.argument_hint || "",
        date_added: s.date_added || "",
        date_updated: s.date_updated || "",
        source: { type: "local", label: "this repo" },
        status: "installed",
        // Which environments this item is installed in (Codex is a push target).
        installed_in: items.length % 2 === 0 ? ["Cursor", "Claude Code"] : ["Cursor"],
        depends_on: [], used_by: [], references: [], enabled_in: [],
      };
      items.push(it);
      byName[s.name] = it;
    }

    const pick = (catName, n) =>
      items.filter(i => i.kind === "skill" && i.category === catName).map(i => i.name).slice(0, n);

    const pres = pick("Presentations & Diagrams", 4);
    const prod = pick("Product & Discovery", 4);
    const design = pick("Design & Frontend", 3);

    const workflows = [
      {
        id: "workflow:build-executive-presentation", name: "build-executive-presentation",
        title: "Build Executive Presentation", kind: "workflow", category: "Presentations & Diagrams",
        summary: "From a messy executive ask to a decision-ready board deck.",
        source: { type: "local", label: "this repo" }, status: "installed",
        date_added: "2026-09-18", date_updated: "2026-09-18",
        steps: [
          { name: "Research & Inputs", uses: prod.slice(0, 2) },
          { name: "Narrative Architecture", uses: prod.slice(2, 4).length ? prod.slice(2, 4) : prod.slice(0, 1) },
          { name: "Visual Development", uses: pres.slice(0, 3) },
          { name: "Build", uses: pres.slice(3, 4).length ? pres.slice(3, 4) : pres.slice(0, 1) },
          { name: "QA", uses: design.slice(0, 1) },
        ],
      },
      {
        id: "workflow:redesign-page", name: "redesign-page", title: "Redesign a Page",
        kind: "workflow", category: "Design & Frontend",
        summary: "Audit an existing page and rebuild it to the design standards.",
        source: { type: "local", label: "this repo" }, status: "installed",
        date_added: "2026-09-18", date_updated: "2026-09-18",
        steps: [
          { name: "Audit", uses: design.slice(0, 1) },
          { name: "Direction", uses: design.slice(1, 3) },
          { name: "Build & QA", uses: design.slice(0, 2) },
        ],
      },
    ];
    for (const w of workflows) {
      if (w.description == null) w.description = w.summary;
      w.best_use = w.best_use || ""; w.watch_outs = w.watch_outs || ""; w.command = w.command || "";
      w.depends_on = w.depends_on || []; w.references = w.references || []; w.enabled_in = w.enabled_in || [];
      const used = [];
      for (const st of w.steps) {
        for (const nm of st.uses) {
          used.push(nm);
          if (byName[nm] && !byName[nm].used_by.includes(w.title)) byName[nm].used_by.push(w.title);
        }
      }
      w.uses_list = Array.from(new Set(used)).sort();
      w.installed_in = w.installed_in || ["Cursor", "Claude Code"];
      items.push(w);
    }

    const refs = [
      ["slide-layout-patterns", "Slide Layout Patterns", "Presentations & Diagrams", "Approved slide layouts and when to use each."],
      ["chart-patterns", "Chart Patterns", "Data Visualization", "Chart types mapped to the insight they communicate best."],
      ["design-tokens", "Design Tokens", "Design & Frontend", "The canonical palette, type, spacing and motion (see DESIGN.md)."],
      ["persona-library", "Persona Library", "Research", "Reusable proto-personas for discovery and messaging."],
    ];
    for (const [nm, tt, c, d] of refs) {
      items.push({
        id: `reference:${nm}`, name: nm, title: tt, kind: "reference", category: c,
        summary: d, description: d, best_use: "", watch_outs: "", command: "",
        source: { type: "local", label: "this repo" }, status: "installed",
        date_added: "2026-09-18", date_updated: "2026-09-18",
        installed_in: ["Cursor"],
        depends_on: [], used_by: [], references: [], enabled_in: [],
      });
    }

    const tools = [
      ["ai-lib", "ai-lib Installer", "Setup & Install", "Classifies and routes external sources into the toolkit."],
      ["skills-db", "Skills Catalog", "Engineering Workflow", "Generates the searchable toolkit index."],
      ["library-add", "Add to Library", "Setup & Install", "The single add-path (/add-to-library)."],
    ];
    for (const [nm, tt, c, d] of tools) {
      items.push({
        id: `tool:${nm}`, name: nm, title: tt, kind: "tool", category: c,
        summary: d, description: d, best_use: "", watch_outs: "", command: "",
        source: { type: "local", label: "this repo" }, status: "installed",
        date_added: "2026-09-18", date_updated: "2026-09-18",
        installed_in: ["Cursor", "Claude Code"],
        depends_on: [], used_by: [], references: [], enabled_in: [],
      });
    }

    const hero = pres[0] || (items[0] && items[0].name);
    if (hero && byName[hero]) {
      byName[hero].depends_on = design.slice(0, 2);
      byName[hero].references = ["Slide Layout Patterns", "Design Tokens"];
      byName[hero].enabled_in = ["Advertiser Experience Deck", "Q4 Launch"];
    }

    const projects = [
      {
        id: "advertiser-deck", name: "Advertiser Experience Deck",
        skills: pres.concat(design.slice(0, 1)), workflows: ["Build Executive Presentation"],
        references: ["Slide Layout Patterns", "Chart Patterns"],
        integrations: { "Cursor": "synced", "Claude Code": "synced", "Codex": "not synced" },
      },
      {
        id: "q4-launch", name: "Q4 Launch",
        skills: prod, workflows: ["Build Executive Presentation"],
        references: ["Persona Library"],
        integrations: { "Cursor": "synced", "Claude Code": "not synced", "Codex": "not synced" },
      },
    ];
    for (const p of projects) {
      for (const nm of p.skills) {
        if (byName[nm] && !byName[nm].enabled_in.includes(p.name)) byName[nm].enabled_in.push(p.name);
      }
    }

    const skillCount = items.filter(i => i.kind === "skill").length;
    const integrations = [
      { id: "cursor", name: "Cursor", status: "connected", count: skillCount, last_synced: "12 min ago" },
      { id: "claude-code", name: "Claude Code", status: "connected", count: 28, last_synced: "yesterday" },
      { id: "codex", name: "Codex", status: "not configured", count: 0, last_synced: null },
    ];
    const inbox = [
      { name: "animation-patterns", detected: "reference", category: "Presentations & Diagrams",
        reason: "Could also be classified as a Skill", source: "github.com/example/motion", read: false },
      { name: "deck-linting", detected: "prompt", category: "Presentations & Diagrams",
        reason: "Low category confidence", source: "pasted", read: false },
      { name: "slide-linter", detected: "prompt", category: "Presentations & Diagrams",
        reason: "Filed from an earlier review", source: "pasted", read: true, filedAs: "prompt" },
    ];
    const updates = [
      { name: pres[0] || "presentation-design", kind: "skill", note: "Source has changed", has_local: true },
      { name: "chart-patterns", kind: "reference", note: "2 files updated upstream", has_local: false },
    ];
    const health = {
      ok: ["Registry healthy", "Integrations connected", "References resolved"],
      issues: [
        { type: "Broken reference", detail: `${pres[0] ? titleOf(pres[0]) : "A skill"} → old-layout-patterns` },
        { type: "Duplicate candidate", detail: "Visual QA / Presentation QA" },
      ],
    };
    const activity = [
      { action: "Installed", target: "Add to Toolkit", when: "just now" },
      { action: "Updated", target: workflows[0].title, when: "15 min ago" },
      { action: "Enabled", target: `${prod[0] ? titleOf(prod[0]) : "a skill"} · Q4 Launch`, when: "1 h ago" },
      { action: "Classification changed", target: "deck-linting → Prompt", when: "2 h ago" },
    ];

    const counts = {};
    for (const i of items) counts[i.kind] = (counts[i.kind] || 0) + 1;
    const collMap = {};
    for (const i of items) collMap[i.category] = (collMap[i.category] || 0) + 1;
    const collections = Object.keys(collMap)
      .filter(k => k !== "Uncategorized")
      .map(k => ({ name: k, count: collMap[k] }))
      .sort((a, b) => b.count - a.count);

    return {
      generated: "library-ui/data-live.js",
      items, counts, collections, projects, integrations, inbox, updates, health, activity,
    };
  }

  return buildLibraryData;
});
