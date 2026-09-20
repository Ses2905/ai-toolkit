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

    /* ---------- Reference subtypes (AI Toolkit expansion, phase 1) ----------
       Templates, Design Systems, Design Patterns and HTML/CSS Foundations live
       as SUBTYPES of the existing "reference" kind — no new top-level nav. The
       id scheme stays reference:<name> so persistence + relationship resolution
       keep working; the subtype is a field. All extra fields are OPTIONAL and
       are only read by subtype-aware detail sections, so existing items render
       exactly as before. Content is authored from the expansion brief (§8–§26)
       and kept honest — no invented versions/authors. */

    // Master content frame HTML/CSS, the single source of truth reused by the
    // Foundation (full) and the Pattern (as an implementation snippet).
    const FRAME_CODE = [
      "<!-- One master content frame: a single shared alignment parent -->",
      '<section class="slide">',
      '  <div class="content-frame">',
      '    <header class="slide-header">',
      '      <p class="eyebrow">Section</p>',
      "      <h1>Headline</h1>",
      '      <p class="lede">Supporting description</p>',
      "    </header>",
      '    <div class="slide-body">',
      "      <!-- charts, cards, diagrams, tables, timelines -->",
      "    </div>",
      "  </div>",
      "</section>",
      "",
      ":root {",
      "  --page-padding-x: clamp(56px, 6vw, 112px);",
      "  --content-max-width: 1440px;",
      "  --section-gap: 32px;",
      "  --hairline: 1px;",
      "}",
      ".content-frame {",
      "  width: min(",
      "    calc(100% - (2 * var(--page-padding-x))),",
      "    var(--content-max-width)",
      "  );",
      "  margin-inline: auto;",
      "}",
      "/* Every primary region shares the frame's edges. */",
      ".slide-header, .slide-body,",
      ".section, .diagram, .card-grid,",
      ".table-wrap, .chart-wrap { width: 100%; }",
      "/* Container width controls alignment. Text max-width controls readability. */",
      ".slide-header h1 { width: 100%; max-width: none; }",
      ".headline-copy { max-width: 72rem; }",
      "/* Thin hairlines over heavy bars. */",
      ".section-rule, .divider { height: 1px; }",
    ].join("\n");

    const FRAME_SNIPPET = [
      '<section class="slide">',
      '  <div class="content-frame">',
      '    <header class="slide-header"><!-- eyebrow · h1 · lede --></header>',
      '    <div class="slide-body"><!-- aligned regions --></div>',
      "  </div>",
      "</section>",
      "",
      ".content-frame {",
      "  width: min(calc(100% - 2*var(--page-padding-x)), var(--content-max-width));",
      "  margin-inline: auto;",
      "}",
    ].join("\n");

    const T_FOUNDATION = "HTML Presentation Layout Foundation";
    const T_PATTERN = "Master Content Frame Pattern";
    const T_SYSTEM = "Personal Presentation Design System";
    const T_TEMPLATE = "Executive Strategy Deck Template";

    const subtypeItems = [
      {
        name: "html-presentation-layout-foundation", title: T_FOUNDATION,
        category: "Presentations & Diagrams", subtype: "html-css-foundation",
        summary: "The master content frame system for HTML slides and visual artifacts — one alignment source of truth.",
        description: "A reusable Reference that centralizes the HTML/CSS layout rules for presentations and visual artifacts, so skills and templates inherit one alignment system instead of duplicating rules.",
        overview: "Centralizes the layout and implementation logic for HTML presentations and visual artifacts. Reference it from skills and templates instead of copying the same 200 lines of layout rules into each one.",
        principles: [
          "One master content frame per slide or page.",
          "Container width controls alignment; text max-width controls readability.",
          "Favor 1px hairlines; use tone and spacing for hierarchy.",
          "Systematic spacing scale, applied by semantic relationship.",
          "Responsive horizontal padding via clamp() — the frame stays the source of truth.",
        ],
        masterFrame: "Every primary region — header, body, diagrams, cards, tables, footer — inherits its left/right boundary from a single .content-frame parent. Individual text may use a smaller max-width for reading measure, but never establishes a competing alignment edge.",
        typography: "Eyebrow → headline → lede → section heading → body → caption. Headlines are allowed meaningful width; avoid excessive bolding.",
        spacing: "Compact 4/8/12/16/24/32/48/64/96 scale. Space by relationship: tight eyebrow→headline, generous header→body.",
        dividers: "1px hairlines only. No thick decorative bars; hierarchy comes from composition, not weight.",
        responsive: "Use responsive --page-padding-x; stack columns and preserve master alignment at smaller sizes. Never clip diagrams.",
        preview: { code: FRAME_CODE },
        references: [], depends_on: [], belongs_to: [], uses: [],
      },
      {
        name: "master-content-frame-pattern", title: T_PATTERN,
        category: "Presentations & Diagrams", subtype: "design-pattern",
        summary: "Give every region on a slide or page one shared alignment system via a single content-frame parent.",
        description: "A layout pattern: all primary regions inherit their left/right edges from one master content frame, so headers, body, diagrams and cards never create competing alignment systems.",
        useWhen: "Whenever a slide or page region must share one alignment system across header, body, diagrams, cards, tables and footer.",
        anatomy: [
          "Slide / page root",
          "Master content frame — defines the left/right boundary",
          "Header, body and visual regions — all width:100%",
          "Optional inner text wrapper — controls reading measure only",
        ],
        rules: [
          "Container width controls alignment; text max-width controls readability.",
          "No competing outer wrappers with different left/right padding.",
          "Avoid nested horizontal padding drift across levels.",
          "A narrower component still sits inside the frame.",
        ],
        dos: [
          "Let the header participate in the full content frame.",
          "Use a 1px hairline for dividers and rules.",
        ],
        donts: [
          "Don't constrain h1 to 60% width or the header to 900px.",
          "Don't add padding-inline at multiple nested levels.",
        ],
        variants: [
          "Full-bleed visual sitting inside the frame",
          "Split narrative — two columns within the frame",
        ],
        preview: { code: FRAME_SNIPPET },
        references: [], depends_on: [], belongs_to: [T_FOUNDATION], uses: [],
      },
      {
        name: "personal-presentation-design-system", title: T_SYSTEM,
        category: "Design & Frontend", subtype: "design-system",
        summary: "The shared visual rules for personal decks and HTML artifacts — foundations, a few components, tokens.",
        description: "A lightweight design system for presentation and visual output: editorial typography, a botanical palette, a compact spacing scale, and the master content frame as its layout law.",
        bestFor: "Personal strategy decks, HTML presentations, and visual artifacts that should feel consistent.",
        outputTypes: "HTML decks, diagrams, one-pagers, and exported PDFs.",
        foundations: [
          ["Typography", "Space Grotesk (display) + Plus Jakarta Sans (body); editorial scale, minimal bolding."],
          ["Color", "Botanical teal/emerald on warm paper; one accent, tonal neutrals."],
          ["Spacing", "4/8/12/16/24/32/48/64/96 compact scale, applied by semantic relationship."],
          ["Layout", "Single master content frame; container width sets alignment, text max-width sets measure."],
        ],
        components: [
          ["Slide header", "Eyebrow + headline + lede, aligned to the full frame."],
          ["Card grid", "Subtle borders, shared padding, aligned rows — used only for real grouping."],
          ["Hairline divider", "1px rule; tone and spacing over heavy bars."],
        ],
        tokens: "Canonical tokens live in DESIGN.md and app.css (:root) — reference + preview + sync, not a duplicated copy.",
        preview: { code: [
          ":root {",
          "  --accent: #0e7490;",
          "  --page-padding-x: clamp(56px, 6vw, 112px);",
          "  --content-max-width: 1440px;",
          "  --space-5: 24px; --space-6: 32px;",
          "  --hairline: 1px;",
          "}",
        ].join("\n") },
        implementation: "Inherit the master content frame, then apply the type and spacing scales. Don't re-declare tokens — reference DESIGN.md.",
        references: [T_FOUNDATION], depends_on: [], belongs_to: [], uses: [],
      },
      {
        name: "executive-strategy-deck-template", title: T_TEMPLATE,
        category: "Presentations & Diagrams", subtype: "template",
        summary: "A starting structure for turning a messy executive ask into a decision-ready board deck.",
        description: "A reusable HTML deck template: fill the variables, drop in your data, and compose slides on the master content frame using the presentation design system.",
        bestFor: "Turning a messy executive ask into a decision-ready board deck.",
        outputFormat: "Self-contained HTML deck (also exportable to PDF).",
        variables: ["{{deck_title}}", "{{audience}}", "{{time_horizon}}", "{{accent}}"],
        inputs: ["Executive ask / decision needed", "Supporting data or metrics", "Recommendation + the options considered"],
        usage: "Duplicate, fill the variables, then compose each slide on the master content frame — header on the full frame, body regions aligned to it.",
        preview: { code: [
          '<section class="slide">',
          '  <div class="content-frame">',
          '    <header class="slide-header">',
          '      <p class="eyebrow">{{audience}}</p>',
          "      <h1>{{deck_title}}</h1>",
          "    </header>",
          '    <div class="slide-body"><!-- recommendation · options · data --></div>',
          "  </div>",
          "</section>",
        ].join("\n") },
        references: [], depends_on: ["html-presentation-layout-foundation"], belongs_to: [], uses: [T_SYSTEM],
      },
    ];
    for (const s of subtypeItems) {
      items.push({
        id: `reference:${s.name}`, name: s.name, title: s.title, kind: "reference",
        category: s.category, subtype: s.subtype,
        summary: s.summary, description: s.description, best_use: "", watch_outs: "", command: "",
        source: { type: "local", label: "this repo" }, status: "installed",
        date_added: "2026-09-20", date_updated: "2026-09-20",
        installed_in: ["Cursor"],
        depends_on: s.depends_on || [], used_by: [], references: s.references || [],
        enabled_in: [], belongs_to: s.belongs_to || [], uses: s.uses || [], works_with: s.works_with || [],
        preview: s.preview,
        // subtype payload (each read only by its matching detail section)
        overview: s.overview, principles: s.principles, masterFrame: s.masterFrame,
        typography: s.typography, spacing: s.spacing, dividers: s.dividers, responsive: s.responsive,
        useWhen: s.useWhen, anatomy: s.anatomy, rules: s.rules, dos: s.dos, donts: s.donts,
        variants: s.variants, implementation: s.implementation,
        foundations: s.foundations, components: s.components, tokens: s.tokens,
        bestFor: s.bestFor, outputTypes: s.outputTypes, outputFormat: s.outputFormat,
        variables: s.variables, inputs: s.inputs, usage: s.usage,
      });
      byName[s.name] = items[items.length - 1];
    }

    // Wire real reciprocal typed relationships among the seeds + one existing
    // design/slides skill (so a skill references the Foundation, not duplicates
    // its rules). used_by / references carry titles; resolveRel handles both.
    const foundation = byName["html-presentation-layout-foundation"];
    const linkTitle = (holder, arr, title) => { holder[arr] = holder[arr] || []; if (!holder[arr].includes(title)) holder[arr].push(title); };
    // Foundation is used by the pattern, system and template.
    linkTitle(foundation, "used_by", T_PATTERN);
    linkTitle(foundation, "used_by", T_SYSTEM);
    linkTitle(foundation, "used_by", T_TEMPLATE);
    // Design system is used by the template.
    linkTitle(byName["personal-presentation-design-system"], "used_by", T_TEMPLATE);
    // An existing frontend/design/slides skill references the Foundation.
    const refSkill = items.find(i => i.kind === "skill" && /(slide|frontend|design|presentation)/.test(i.name));
    if (refSkill) {
      linkTitle(refSkill, "references", T_FOUNDATION);
      linkTitle(foundation, "used_by", refSkill.title);
    }

    const hero = pres[0] || (items[0] && items[0].name);
    if (hero && byName[hero]) {
      byName[hero].depends_on = design.slice(0, 2);
      // Merge, don't replace — the Foundation may already be in references.
      const extraRefs = ["Slide Layout Patterns", "Design Tokens"];
      byName[hero].references = Array.from(new Set([...(byName[hero].references || []), ...extraRefs]));
    }

    // Example projects (not live external data). They reference catalog assets
    // by name rather than duplicating them, and keep per-agent sync fields.
    const named = (...ns) => ns.filter(n => byName[n]);
    const projects = [
      {
        id: "advertiser-deck", name: "Advertiser Experience Deck",
        updated: "2026-09-19",
        skills: named("walmart-ads-terminology", "product-strategy-session", "frontend-slides-editable", "html-ppt"),
        prompts: named("competitive-matrix", "press-release"),
        workflows: ["Build Executive Presentation"],
        references: ["Slide Layout Patterns", "Chart Patterns", T_FOUNDATION, T_TEMPLATE],
        integrations: { "Cursor": "synced", "Claude Code": "synced", "Codex": "not synced" },
      },
      {
        id: "q4-launch", name: "Q4 Product Launch",
        updated: "2026-09-16",
        skills: named("product-strategy-session", "lean-ux-canvas", "opportunity-solution-tree", "problem-framing-canvas"),
        prompts: named("okr", "prd", "persona"),
        workflows: ["Build Executive Presentation"],
        references: ["Persona Library"],
        integrations: { "Cursor": "synced", "Claude Code": "not synced", "Codex": "not synced" },
      },
      {
        id: "exec-strategy", name: "Executive Strategy Offsite",
        updated: "2026-09-20",
        skills: named("frontend-slides-editable", "html-ppt", "slides", "mck-ppt-design", "product-strategy-session"),
        prompts: named("okr", "press-release"),
        workflows: ["Build Executive Presentation"],
        references: [T_FOUNDATION, T_PATTERN, T_SYSTEM, T_TEMPLATE],
        integrations: { "Cursor": "synced", "Claude Code": "synced", "Codex": "not synced" },
      },
      {
        id: "ui-redesign", name: "UI Design System Refresh",
        updated: "2026-09-18",
        skills: named("design-system", "high-end-visual-design", "apple-design", "canvas-design", "ui-ux-pro-max"),
        prompts: named("a11y-audit"),
        workflows: ["Redesign a Page"],
        references: ["Design Tokens", T_SYSTEM],
        integrations: { "Cursor": "synced", "Claude Code": "synced", "Codex": "not synced", "Lovable": "not synced" },
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
      { id: "lovable", name: "Lovable", status: "not configured", count: 0, last_synced: null },
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

    // Thin typed relationships read-view: references (not copies of) the same
    // writable arrays, so in-memory renames that swap array entries stay in sync
    // and renameItem/applyRename need no change. Keys are omitted-friendly.
    for (const it of items) {
      it.relationships = {
        uses: it.uses,
        usedBy: it.used_by,
        worksWith: it.works_with,
        dependsOn: it.depends_on,
        references: it.references,
        belongsTo: it.belongs_to,
        enabledIn: it.enabled_in,
        availableIn: it.installed_in,
      };
    }

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
