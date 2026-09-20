/* Library UI — functional wireframe. Reads the live catalog at runtime via
   buildLibraryData() (data-live.js), falling back to the bundled window.LIBRARY_DATA
   snapshot (data.js) when the catalog isn't reachable. Real skills + prompts come
   from the catalog; workflows/references/tools/projects/integrations/inbox are
   synthesized. Focus: information architecture, navigation, flows. */
(function () {
  "use strict";
  const EMPTY = { items: [], counts: {}, collections: [], projects: [], integrations: [], inbox: [], updates: [], health: { ok: [], issues: [] }, activity: [] };
  let D = window.LIBRARY_DATA || EMPTY;
  let ITEMS = D.items;
  let byId = Object.fromEntries(ITEMS.map(i => [i.id, i]));
  let byTitle = Object.fromEntries(ITEMS.map(i => [i.title, i]));
  let dataSource = "snapshot"; // "live" once the real catalog is loaded

  function setData(data, source) {
    D = data || EMPTY;
    ITEMS = D.items || [];
    byId = Object.fromEntries(ITEMS.map(i => [i.id, i]));
    byTitle = Object.fromEntries(ITEMS.map(i => [i.title, i]));
    dataSource = source;
  }

  // Load the canonical catalog at runtime so the Library never drifts from the
  // real skills/prompts index. Falls back to the committed snapshot (data.js)
  // when the catalog isn't reachable (file://, offline, or served from within
  // library-ui/). Candidate paths cover serving from the repo root or a parent.
  async function loadLiveData() {
    if (typeof window.buildLibraryData !== "function" || typeof fetch !== "function") return false;
    const candidates = ["../catalog/skills-index.json", "catalog/skills-index.json", "./catalog/skills-index.json"];
    for (const url of candidates) {
      try {
        const res = await fetch(url, { cache: "no-store" });
        if (!res.ok) continue;
        const catalog = await res.json();
        if (!catalog || !Array.isArray(catalog.skills)) continue;
        setData(window.buildLibraryData(catalog), "live");
        return true;
      } catch (_e) { /* try next candidate, then fall back */ }
    }
    return false;
  }

  const KIND = {
    skill:     { label: "Skill",     glyph: "◇", plural: "Skills",     blurb: "Reusable capability",       desc: "Reusable capabilities an agent invokes by name to do a focused job well." },
    prompt:    { label: "Prompt",    glyph: "▤", plural: "Prompts",    blurb: "Task instruction",          desc: "One-shot task instructions you run with a slash command." },
    workflow:  { label: "Workflow",  glyph: "→", plural: "Workflows",  blurb: "Multi-step process",        desc: "Multi-step processes that chain skills and prompts into an outcome." },
    tool:      { label: "Tool",      glyph: "⚙", plural: "Tools",       blurb: "Executable capability",     desc: "Executable helpers that install, index, and route library content." },
    reference: { label: "Reference", glyph: "▱", plural: "References",  blurb: "Supporting knowledge",      desc: "Supporting knowledge and patterns your skills and prompts draw on." },
    template:  { label: "Template",  glyph: "□", plural: "Templates",   blurb: "Reusable starting point",   desc: "Reusable starting points you copy and fill in." },
  };
  const KIND_ORDER = ["skill", "prompt", "workflow", "tool", "reference", "template"];

  const esc = s => (s == null ? "" : String(s)).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const kebab = s => String(s).toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  const h = (html) => { const t = document.createElement("template"); t.innerHTML = html.trim(); return t.content.firstElementChild; };
  const kindsPresent = () => KIND_ORDER.filter(k => ITEMS.some(i => i.kind === k));
  const cats = () => Array.from(new Set(ITEMS.map(i => i.category))).sort();

  const state = { kind: "all", cat: "All", source: "All", sort: "name", view: "list", q: "" };

  // Environments the library can install/sync into (from the integrations tier).
  const platforms = () => (D.integrations || []).map(x => x.name);

  /* ---------- Shell ---------- */
  function shell() {
    const item = (route, ic, label, badge) => `<a href="#/${route}" data-route="${route}"><span class="ic">${ic}</span>${esc(label)}${badge != null ? `<span class="count">${badge}</span>` : ""}</a>`;
    const subs = kindsPresent().map(k => `<a href="#/library/${k}" data-route="library/${k}"><span class="ic">${KIND[k].glyph}</span>${KIND[k].plural}<span class="count">${D.counts[k] || 0}</span></a>`).join("");
    document.getElementById("app").innerHTML = `
      <div class="shell">
        <aside class="sidebar" id="sidebar">
          <div class="brand"><span class="mark"></span> Library<span class="src-pill" data-src="${dataSource}" title="${dataSource === "live" ? "Reading the live catalog" : "Using the bundled snapshot"}">${dataSource}</span></div>
          <nav class="nav">
            ${item("home", "⌂", "Home")}
            <div class="group">Library</div>
            ${item("library", "▤", "All", ITEMS.length)}
            <div class="sub">${subs}</div>
            <div class="group">Manage</div>
            ${item("inbox", "▧", "Inbox", (D.inbox || []).length)}
            ${item("discover", "◎", "Discover")}
            ${item("projects", "▦", "Projects")}
            ${item("integrations", "⇄", "Integrations")}
            ${item("settings", "⚙", "Settings")}
          </nav>
        </aside>
        <div class="main">
          <div class="topbar"><div class="topbar-inner">
            <button class="btn sm hamburger" id="ham">≡</button>
            <label class="topsearch"><span>⌕</span><input id="q" type="search" placeholder="Search the library…" aria-label="Search the library" /><span class="kbd">⌘K</span></label>
            <span class="spacer"></span>
            <button class="btn" id="new">+ New</button>
            <button class="btn primary" id="add">+ Add to Library</button>
          </div></div>
          <div id="view"></div>
        </div>
      </div>
      <div class="scrim" id="scrim"></div>
      <div class="drawer" id="drawer" aria-hidden="true"></div>
      <div id="overlay"></div>`;
    document.getElementById("q").addEventListener("input", e => { location.hash = "#/search?q=" + encodeURIComponent(e.target.value); });
    document.getElementById("add").onclick = openAdd;
    document.getElementById("new").onclick = openCreate;
    document.getElementById("ham").onclick = () => document.getElementById("sidebar").classList.toggle("show");
    document.getElementById("scrim").onclick = closeAll;
  }

  function setActiveNav(route) {
    document.querySelectorAll(".nav a").forEach(a => a.classList.toggle("active", a.dataset.route === route));
  }

  /* ---------- Router ---------- */
  function router() {
    const raw = location.hash.replace(/^#\/?/, "") || "home";
    const [path, query] = raw.split("?");
    const parts = path.split("/");
    const view = document.getElementById("view");
    closeDrawerOnly();
    if (parts[0] === "item") return openItem(decodeURIComponent(parts.slice(1).join("/")));
    setActiveNav(path.startsWith("library") ? path : parts[0]);
    const q = new URLSearchParams(query || "");
    if (parts[0] === "home") view.innerHTML = viewHome();
    else if (parts[0] === "library") view.innerHTML = viewLibrary(parts[1] || "all");
    else if (parts[0] === "search") { document.getElementById("q").value = q.get("q") || ""; view.innerHTML = viewSearch(q.get("q") || ""); }
    else if (parts[0] === "discover") view.innerHTML = viewDiscover();
    else if (parts[0] === "projects") view.innerHTML = viewProjects();
    else if (parts[0] === "project") view.innerHTML = viewProject(decodeURIComponent(parts[1] || ""));
    else if (parts[0] === "integrations") view.innerHTML = viewIntegrations();
    else if (parts[0] === "inbox") view.innerHTML = viewInbox();
    else if (parts[0] === "activity") view.innerHTML = viewActivity();
    else if (parts[0] === "health") view.innerHTML = viewHealth();
    else if (parts[0] === "settings") view.innerHTML = viewSettings();
    else view.innerHTML = viewHome();
    wireView();
    window.scrollTo(0, 0);
  }

  function wireView() {
    document.querySelectorAll("[data-item]").forEach(el => el.onclick = () => { location.hash = "#/item/" + encodeURIComponent(el.dataset.item); });
    document.querySelectorAll("[data-kindtab]").forEach(b => b.onclick = () => { location.hash = "#/library/" + b.dataset.kindtab; });
    document.querySelectorAll("[data-filter]").forEach(sel => sel.onchange = () => { state[sel.dataset.filter] = sel.value; rerenderLibrary(); });
    document.querySelectorAll("[data-view]").forEach(b => b.onclick = () => { state.view = b.dataset.view; rerenderLibrary(); });
    document.querySelectorAll("[data-clearf]").forEach(b => b.onclick = () => { state[b.dataset.clearf] = b.dataset.clearf === "kind" ? "all" : "All"; if (b.dataset.clearf === "kind") location.hash = "#/library/all"; else rerenderLibrary(); });
    const ls = document.getElementById("libsearch");
    if (ls) ls.oninput = () => { state.q = ls.value; rerenderList(); };
    document.querySelectorAll("[data-nav]").forEach(b => b.onclick = () => { location.hash = "#/" + b.dataset.nav; });
    document.querySelectorAll("[data-add]").forEach(b => b.onclick = openAdd);
    document.querySelectorAll("[data-create]").forEach(b => b.onclick = openCreate);
    document.querySelectorAll("[data-action]").forEach(b => b.onclick = (e) => { e.stopPropagation(); handleAction(b.dataset.action, b.dataset); });
  }
  function rerenderLibrary() { document.getElementById("view").innerHTML = viewLibrary(state.kind); wireView(); }
  function rerenderList() { const host = document.getElementById("libresults"); if (host) { host.outerHTML = libResults(); wireView(); } }

  /* ---------- Kind label ---------- */
  const kindTag = k => `<span class="kind" data-k="${k}"><span class="g">${KIND[k].glyph}</span>${KIND[k].label}</span>`;

  /* ---------- Home ---------- */
  function viewHome() {
    const c = D.counts;
    const summary = ["skill", "prompt", "workflow", "reference"].map(k => `<div class="s"><span class="n">${c[k] || 0}</span><span class="l">${KIND[k].plural}</span></div>`).join("");
    const att = [];
    if ((D.inbox || []).length) att.push(["", `${D.inbox.length} items need classification`, "inbox"]);
    if ((D.updates || []).length) att.push(["", `${D.updates.length} upstream updates available`, "health"]);
    (D.health.issues || []).forEach(i => att.push(["", `${i.type}: ${i.detail}`, "health"]));
    const attHtml = att.length ? att.map(([_, t, r]) => `<div class="att"><span class="dot"></span><span>${esc(t)}</span><button class="btn sm go" data-nav="${r}">Review</button></div>`).join("") : `<div class="att info"><span class="dot"></span><span>Everything looks healthy.</span></div>`;
    const recent = (D.activity || []).slice(0, 5).map(a => `<div class="a"><strong>${esc(a.action)}</strong><span>${esc(a.target)}</span><span class="w">${esc(a.when)}</span></div>`).join("");
    const cols = (D.collections || []).slice(0, 8).map(x => `<button class="chip" data-nav="library/all">${esc(x.name)}<span class="c">${x.count}</span></button>`).join("");
    return `
      <div class="page">
        <div class="page-head"><h1>Your AI Library</h1><p>Everything you can compose — skills, prompts, workflows and references — in one place.</p></div>
        <label class="topsearch" style="max-width:none"><span>⌕</span><input placeholder="Search all skills, prompts, workflows & references…" onkeydown="if(event.key==='Enter'){location.hash='#/search?q='+encodeURIComponent(this.value)}"/></label>
        <div style="display:flex;gap:10px;margin-top:14px"><button class="btn primary" data-add>+ Add to Library</button><button class="btn" data-nav="discover">Browse / Discover</button></div>
        <div class="section"><h2>Library summary</h2><div class="summary">${summary}</div></div>
        <div class="section"><h2>Needs attention</h2><div class="attention">${attHtml}</div></div>
        <div class="section"><h2>Your collections</h2><div class="chips">${cols}</div></div>
        <div class="section"><h2>Recent activity</h2><div class="actlist">${recent}</div></div>
      </div>`;
  }

  /* ---------- Library browse ---------- */
  function filtered() {
    let list = ITEMS.slice();
    if (state.kind !== "all") list = list.filter(i => i.kind === state.kind);
    if (state.cat !== "All") list = list.filter(i => i.category === state.cat);
    if (state.q.trim()) { const q = state.q.toLowerCase(); list = list.filter(i => (i.title + " " + i.name + " " + i.summary + " " + i.category).toLowerCase().includes(q)); }
    if (state.sort === "name") list.sort((a, b) => a.title.localeCompare(b.title));
    else list.sort((a, b) => (b.date_updated || "").localeCompare(a.date_updated || "") || a.title.localeCompare(b.title));
    return list;
  }
  const platInitial = p => ({ "Cursor": "Cu", "Claude Code": "Cl", "Codex": "Cx" }[p] || String(p).slice(0, 2));
  function installDots(i) {
    const inn = i.installed_in || [];
    const pl = platforms();
    const title = pl.map(p => `${p}: ${inn.includes(p) ? "installed" : "not installed"}`).join(" · ");
    return `<span class="insti" title="${esc(title)}" aria-label="${esc(title)}">${pl.map(p => `<span class="idot ${inn.includes(p) ? "on" : ""}"><i>${esc(platInitial(p))}</i></span>`).join("")}</span>`;
  }
  function card(i) {
    return `<div class="card" data-item="${esc(i.id)}">
      <div class="top">${kindTag(i.kind)}${installDots(i)}</div>
      <div class="name">${esc(i.title)}</div>
      <div class="meta"><span class="tag">${esc(i.category)}</span><span>${i.command ? "/" + esc(i.command) : (i.used_by && i.used_by.length ? "Used by " + i.used_by.length : "")}</span></div>
    </div>`;
  }
  function listRow(i) {
    return `<div class="row" data-item="${esc(i.id)}">
      <span class="kind" data-k="${i.kind}"><span class="g">${KIND[i.kind].glyph}</span></span>
      <span class="nmwrap"><span class="nm">${esc(i.title)}</span><span class="kpill" data-k="${i.kind}">${KIND[i.kind].label}</span></span>
      <span class="sub cat">${esc(i.category)}</span>
      ${installDots(i)}
      <span class="sub date">${esc(i.date_updated || "")}</span>
    </div>`;
  }
  function libResults() {
    const list = filtered();
    if (!list.length) return `<div id="libresults"><div class="empty"><h3>Nothing matches</h3><p>Try clearing a filter or searching a different term.</p></div></div>`;
    const body = state.view === "list" ? `<div class="list">${list.map(listRow).join("")}</div>` : `<div class="grid">${list.map(card).join("")}</div>`;
    return `<div id="libresults"><div class="count-line">${list.length} of ${ITEMS.length} items</div>${body}</div>`;
  }
  function viewLibrary(kind) {
    state.kind = kind || "all";
    const tabs = ["all", ...kindsPresent()].map(k => `<button data-kindtab="${k}" class="${state.kind === k ? "active" : ""}">${k === "all" ? "All" : KIND[k].plural}</button>`).join("");
    const catOpts = ['<option value="All">All categories</option>'].concat(cats().map(c => `<option value="${esc(c)}" ${state.cat === c ? "selected" : ""}>${esc(c)}</option>`)).join("");
    const chips = [];
    if (state.kind !== "all") chips.push(`<span class="chipf">${KIND[state.kind].plural}<button data-clearf="kind">×</button></span>`);
    if (state.cat !== "All") chips.push(`<span class="chipf">${esc(state.cat)}<button data-clearf="cat">×</button></span>`);
    const active = state.kind !== "all" && KIND[state.kind];
    const heading = active ? KIND[state.kind].plural : "Library";
    const subtitle = active ? KIND[state.kind].desc : "Browse and manage everything you've installed.";
    return `<div class="page">
      <div class="page-head"><h1>${esc(heading)}</h1><p>${esc(subtitle)}</p></div>
      <label class="topsearch" style="max-width:none"><span>⌕</span><input id="libsearch" placeholder="Search the library…" value="${esc(state.q)}"/></label>
      <div class="filterbar"><div class="tabs">${tabs}</div></div>
      <div class="filterbar">
        <select class="f" data-filter="cat">${catOpts}</select>
        <select class="f" data-filter="sort"><option value="recent" ${state.sort==="recent"?"selected":""}>Recently updated</option><option value="name" ${state.sort==="name"?"selected":""}>Name</option></select>
        ${chips.join("")}
        <span class="spacer"></span>
        <div class="tabs"><button data-view="cards" class="${state.view==="cards"?"active":""}">Cards</button><button data-view="list" class="${state.view==="list"?"active":""}">List</button></div>
      </div>
      ${libResults()}
    </div>`;
  }

  /* ---------- Search (grouped) ---------- */
  function viewSearch(q) {
    const qq = (q || "").toLowerCase().trim();
    const hits = qq ? ITEMS.filter(i => (i.title + " " + i.name + " " + i.summary + " " + i.category).toLowerCase().includes(qq)) : [];
    const head = `<div class="page-head"><h1>Search</h1><p>${qq ? `Results for “${esc(q)}” — ${hits.length} items across the library.` : "Type to search skills, prompts, workflows & references."}</p></div>`;
    if (!qq) return `<div class="page">${head}</div>`;
    if (!hits.length) return `<div class="page">${head}<div class="empty"><h3>Nothing found</h3><p>No library items match “${esc(q)}”. Try a broader term, or add something new.</p><button class="btn primary" data-add>+ Add to Library</button></div></div>`;
    const groups = KIND_ORDER.map(k => {
      const g = hits.filter(i => i.kind === k);
      if (!g.length) return "";
      return `<div class="section"><h2>${KIND[k].plural}</h2><div class="list">${g.map(listRow).join("")}</div></div>`;
    }).join("");
    return `<div class="page">${head}${groups}</div>`;
  }

  /* ---------- Item detail (drawer) ---------- */
  function relRow(label, names) {
    if (!names || !names.length) return "";
    const links = names.map(n => { const it = byTitle[n] || byId["skill:" + n] || byId["reference:" + n]; return it ? `<a href="#/item/${encodeURIComponent(it.id)}">${esc(it.title)}</a>` : `<a>${esc(n)}</a>`; }).join("");
    return `<div class="field"><h4>${label}</h4><div class="rellist">${links}</div></div>`;
  }
  function openItem(id) {
    const i = byId[id]; if (!i) { location.hash = "#/library"; return; }
    const dr = document.getElementById("drawer");
    const isWf = i.kind === "workflow";
    const overview = (isWf ? workflowSteps(i) : `
      <div class="field"><h4>What it is</h4><p>${esc(i.description || i.summary)}</p></div>
      ${i.best_use ? `<div class="field"><h4>Activate when</h4><p>${esc(i.best_use)}</p></div>` : ""}
      ${relRow("Used by", i.used_by)}
      ${relRow("Depends on", i.depends_on)}
      ${relRow("References", i.references)}
      ${relRow("Enabled in", i.enabled_in)}`) + installPanel(i);
    const related = ITEMS.filter(x => x.category === i.category && x.id !== i.id).slice(0, 4).map(x => x.title);
    const rels = `<div class="relmap">
        ${i.depends_on && i.depends_on.length ? `<div class="up">${i.depends_on.map(esc).join(" · ")}<div class="arr">▲</div></div>` : ""}
        <div class="center">${esc(i.title)}</div>
        <div class="faint">${related.length ? "related · " + related.map(esc).join(" · ") : "no direct relations yet"}</div>
        ${i.used_by && i.used_by.length ? `<div class="down"><div class="arr">▼</div>${i.used_by.map(esc).join(" · ")}</div>` : ""}
      </div><p class="faint" style="margin-top:10px">USES · USED BY · DEPENDS ON · REFERENCES · ENABLED IN</p>`;
    const source = `
      <div class="field"><h4>Source</h4><p>${esc(i.source && i.source.label || "this repo")}</p></div>
      <div class="field"><h4>Updated</h4><p>${esc(i.date_updated)} · added ${esc(i.date_added)}</p></div>
      <div class="field"><h4>Invocation</h4><p>${i.command ? "<span class='mono'>/" + esc(i.command) + "</span>" : "model-invoked"}</p></div>
      <details class="advanced"><summary>Advanced · technical details</summary><div class="adv-body">
        <p>Path: <span class="mono">${esc(pathOf(i))}</span></p>
        <p>Kind: ${esc(i.kind)} · Category: ${esc(i.category)} · Status: ${esc(i.status)}</p>
      </div></details>`;
    dr.innerHTML = `
      <div class="dhead">
        <div class="crumb">Library / ${KIND[i.kind].plural} / ${esc(i.title)}</div>
        ${kindTag(i.kind)}
        <h2>${esc(i.title)}</h2>
        <p class="muted">${esc(i.summary || i.description)}</p>
        <div class="dactions"><button class="btn primary" data-action="enable-item" data-id="${esc(i.id)}">${i.kind === "skill" ? "Enable" : "Use"}</button><button class="btn" data-action="rename-item" data-id="${esc(i.id)}">Rename</button><button class="btn" data-action="edit-item" data-id="${esc(i.id)}">Edit</button><button class="btn" id="drclose">Close</button></div>
      </div>
      <div class="dtabs">
        <button data-dt="ov" class="active">Overview</button>
        <button data-dt="rel">Relationships</button>
        <button data-dt="src">Source</button>
      </div>
      <div class="dbody" id="dbody">${overview}</div>`;
    dr.setAttribute("aria-hidden", "false");
    dr.classList.add("show"); document.getElementById("scrim").classList.add("show");
    const panes = { ov: overview, rel: rels, src: source };
    dr.querySelectorAll("[data-dt]").forEach(b => b.onclick = () => {
      dr.querySelectorAll("[data-dt]").forEach(x => x.classList.remove("active")); b.classList.add("active");
      document.getElementById("dbody").innerHTML = panes[b.dataset.dt];
      dr.querySelectorAll("[data-action]").forEach(x => x.onclick = () => handleAction(x.dataset.action, x.dataset));
    });
    document.getElementById("drclose").onclick = () => history.length > 1 ? history.back() : (location.hash = "#/library");
    dr.querySelectorAll("[data-action]").forEach(b => b.onclick = () => handleAction(b.dataset.action, b.dataset));
  }
  function pathOf(i) {
    if (i.kind === "skill") return `skills/${i.name}/SKILL.md`;
    if (i.kind === "prompt") return `prompts/commands/${i.name}.md`;
    if (i.kind === "workflow") return `workflows/${i.name}/WORKFLOW.md`;
    if (i.kind === "reference") return `references/${i.name}.md`;
    return `tools/${i.name}/`;
  }
  function workflowSteps(w) {
    const steps = (w.steps || []).map((s, idx) => {
      const uses = (s.uses || []).map(n => { const it = byTitle[byTitleKey(n)] || byId["skill:" + n]; return `<a class="tag" href="#/item/${encodeURIComponent(it ? it.id : "skill:" + n)}">${esc(it ? it.title : n)}</a>`; }).join("");
      return `${idx ? '<div class="stepconn"></div>' : ""}<div class="step"><div class="sn"><span class="num">${idx + 1}</span><strong>${esc(s.name)}</strong></div>${uses ? `<div class="uses">${uses}</div>` : ""}</div>`;
    }).join("");
    return `<div class="field"><h4>What it is</h4><p>${esc(w.description || w.summary)}</p></div><div class="field"><h4>Steps</h4><div class="steps">${steps}</div></div>`;
  }
  function byTitleKey(name) { const it = byId["skill:" + name]; return it ? it.title : name; }

  /* ---------- Discover / Projects / Integrations / Inbox / Activity / Health / Settings ---------- */
  function viewDiscover() {
    const colls = (D.collections || []).slice(0, 8).map(c => `<button class="chip" data-nav="library/all">${esc(c.name)}</button>`).join("");
    return `<div class="page">
      <div class="page-head"><h1>Discover</h1><p>What you could add. External discovery isn't wired up yet — this is the architecture.</p></div>
      <label class="topsearch" style="max-width:none"><span>⌕</span><input placeholder="Search skills, prompts, workflows & tools to add…"/></label>
      <div class="section"><h2>Browse by domain</h2><div class="chips">${colls}</div></div>
      <div class="section"><h2>From sources</h2><div class="list">
        <div class="row" data-add><span class="kind" data-k="tool"><span class="g">⚙</span></span><span><div class="nm">GitHub</div><div class="sub">Install a repo by URL — inspected & routed automatically</div></span><span class="sub">source</span><span class="btn sm">Add</span></div>
        <div class="row"><span class="kind"><span class="g">◎</span></span><span><div class="nm">Community libraries</div><div class="sub">Curated catalogs (coming soon)</div></span><span class="sub">registry</span><span class="sub faint">soon</span></div>
      </div></div>
      <div class="empty" style="margin-top:24px"><h3>Discovery feed coming soon</h3><p>When registries are connected, recommended skills, prompts and workflows will appear here.</p><button class="btn primary" data-add>+ Add from GitHub</button></div>
    </div>`;
  }
  function viewProjects() {
    const rows = (D.projects || []).map(p => `<div class="row" data-nav="project/${encodeURIComponent(p.id)}"><span class="kind"><span class="g">▦</span></span>
      <span><div class="nm">${esc(p.name)}</div><div class="sub">${p.skills.length} skills · ${p.workflows.length} workflows · ${p.references.length} references</div></span>
      <span class="sub">${Object.values(p.integrations).filter(v => v === "synced").length}/${Object.keys(p.integrations).length} integrations synced</span><span class="btn sm">Open</span></div>`).join("");
    return `<div class="page"><div class="page-head"><h1>Projects</h1><p>What parts of your global library are active where.</p></div><div class="list">${rows}</div></div>`;
  }
  function viewProject(id) {
    const p = (D.projects || []).find(x => x.id === id); if (!p) return viewProjects();
    const caps = p.skills.map(n => { const it = byId["skill:" + n]; return `<div class="row" ${it ? `data-item="skill:${esc(n)}"` : ""}><span class="kind" data-k="skill"><span class="g">◇</span></span><span><div class="nm">${esc(it ? it.title : n)}</div></span><span class="sub">enabled</span><button class="btn sm" data-action="disable-cap" data-proj="${esc(p.id)}" data-name="${esc(n)}">Disable</button></div>`; }).join("");
    const wfs = p.workflows.map(n => `<span class="tag">${esc(n)}</span>`).join(" ");
    const refs = p.references.map(n => `<span class="tag">${esc(n)}</span>`).join(" ");
    const integ = Object.entries(p.integrations).map(([k, v]) => `<div class="row"><span class="kind"><span class="g">⇄</span></span><span><div class="nm">${esc(k)}</div></span><span class="sub">${v === "synced" ? "Synced" : "Not synced"}</span><button class="btn sm" data-action="sync-project-integration" data-proj="${esc(p.id)}" data-name="${esc(k)}">${v === "synced" ? "Re-sync" : "Sync"}</button></div>`).join("");
    return `<div class="page">
      <div class="crumb" style="margin-bottom:8px"><a href="#/projects">Projects</a> / ${esc(p.name)}</div>
      <div class="page-head"><h1>${esc(p.name)}</h1><p>${p.skills.length} skills · ${p.workflows.length} workflows · ${p.references.length} references enabled.</p></div>
      <div class="section"><h2>Enabled capabilities</h2><div class="list">${caps}</div><div style="margin-top:10px"><button class="btn" data-nav="library/skills">+ Enable from Library</button></div></div>
      <div class="section"><h2>Workflows</h2><div class="chips">${wfs || '<span class="faint">None yet</span>'}</div></div>
      <div class="section"><h2>References</h2><div class="chips">${refs || '<span class="faint">None yet</span>'}</div></div>
      <div class="section"><h2>Integrations</h2><div class="list">${integ}</div></div>
    </div>`;
  }
  function viewIntegrations() {
    const rows = (D.integrations || []).map(x => `<div class="row"><span class="kind"><span class="g">⇄</span></span>
      <span><div class="nm">${esc(x.name)}</div><div class="sub">${x.status === "connected" ? `${x.count} skills available · last synced ${esc(x.last_synced)}` : "Not configured"}</div></span>
      <span class="sub">${x.status === "connected" ? "Connected" : "—"}</span>
      <span>${x.status === "connected" ? `<button class="btn sm" data-action="sync-integration" data-name="${esc(x.name)}">Sync</button>` : `<button class="btn sm primary" data-action="setup-integration" data-name="${esc(x.name)}">Set up</button>`}</span></div>`).join("");
    return `<div class="page"><div class="page-head"><h1>Integrations</h1><p>Use your global library across AI coding environments. The library is the source of truth; each tool syncs from it.</p></div><div class="list">${rows}</div>
      <details class="advanced" style="margin-top:16px"><summary>Advanced · how syncing works</summary><div class="adv-body">Each integration maps the global library into that tool's expected structure (generated indexes / links). You don't manage symlinks by hand.</div></details></div>`;
  }
  function viewInbox() {
    const rows = (D.inbox || []).map(x => `<div class="row"><span class="kind" data-k="${x.detected}"><span class="g">${(KIND[x.detected] || KIND.reference).glyph}</span></span>
      <span><div class="nm">${esc(x.name)}</div><div class="sub">Suggested: ${esc(x.detected)} · ${esc(x.category)} — ${esc(x.reason)}</div></span>
      <span class="sub">${esc(x.source)}</span><button class="btn sm" data-action="review-inbox" data-name="${esc(x.name)}">Review</button></div>`).join("");
    if (!(D.inbox || []).length) return `<div class="page"><div class="page-head"><h1>Inbox</h1></div><div class="empty"><h3>Inbox is clear</h3><p>Items the router can't confidently classify land here for a quick decision.</p></div></div>`;
    return `<div class="page"><div class="page-head"><h1>Inbox</h1><p>${D.inbox.length} items need review. This is a staging area — not a second library.</p></div><div class="list">${rows}</div></div>`;
  }
  function viewActivity() {
    const rows = (D.activity || []).map(a => `<div class="a"><strong>${esc(a.action)}</strong><span>${esc(a.target)}</span><span class="w">${esc(a.when)}</span></div>`).join("");
    return `<div class="page"><div class="page-head"><h1>Activity</h1><p>What changed across your library.</p></div><div class="actlist">${rows}</div></div>`;
  }
  function viewHealth() {
    const ok = (D.health.ok || []).map(t => `<div class="att info"><span class="dot"></span><span>${esc(t)}</span></div>`).join("");
    const iss = (D.health.issues || []).map((i, ix) => `<div class="att"><span class="dot"></span><span><strong>${esc(i.type)}</strong> — ${esc(i.detail)}</span><button class="btn sm go" data-action="review-issue" data-i="${ix}">Review</button></div>`).join("");
    return `<div class="page"><div class="page-head"><h1>Library health</h1><p>Is everything wired up correctly?</p></div>
      <div class="section"><h2>Healthy</h2><div class="attention">${ok}</div></div>
      ${iss ? `<div class="section"><h2>${D.health.issues.length} need attention</h2><div class="attention">${iss}</div></div>` : ""}
      <details class="advanced" style="margin-top:16px"><summary>Advanced · doctor output</summary><div class="adv-body mono">$ ai-lib doctor<br/>registry: ok · integrations: ok · references: 1 broken · duplicates: 1 candidate</div></details></div>`;
  }
  function viewSettings() {
    const recent = (D.activity || []).slice(0, 6).map(a => `<div class="a"><strong>${esc(a.action)}</strong><span>${esc(a.target)}</span><span class="w">${esc(a.when)}</span></div>`).join("") || `<div class="a"><span class="faint">No activity yet.</span></div>`;
    const c = D.counts || {};
    const totals = KIND_ORDER.filter(k => c[k]).map(k => `${c[k]} ${c[k] === 1 ? KIND[k].label.toLowerCase() : KIND[k].plural.toLowerCase()}`).join(" · ");
    return `<div class="page"><div class="page-head"><h1>Settings</h1><p>Where your library lives, what's in it, and what's changed.</p></div>
      <div class="section"><h2>Global library</h2><div class="list">
        <div class="row settings-row"><span class="kind"><span class="g">⌂</span></span><span><div class="nm">Library home</div><div class="sub mono">$AI_LIBRARY_HOME (~/.ai-library)</div></span><span></span><button class="btn sm" data-action="change-home">Change</button></div>
        <div class="row settings-row"><span class="kind"><span class="g">▤</span></span><span><div class="nm">Contents</div><div class="sub">${esc(totals || "empty")}</div></span><span></span><button class="btn sm" data-nav="library">Open library</button></div>
      </div></div>
      <div class="section"><div class="sec-head"><h2>Activity</h2><button class="btn sm" data-nav="activity">View all</button></div><div class="actlist">${recent}</div></div>
    </div>`;
  }

  /* ---------- Overlays: Add / Create / Palette ---------- */
  function overlay(html) { document.getElementById("overlay").innerHTML = html; }
  function closeOverlay() { document.getElementById("overlay").innerHTML = ""; }
  function closeDrawerOnly() { const dr = document.getElementById("drawer"); if (dr) { dr.classList.remove("show"); dr.setAttribute("aria-hidden", "true"); } document.getElementById("scrim") && document.getElementById("scrim").classList.remove("show"); }
  function closeAll() { closeDrawerOnly(); closeOverlay(); }

  const add = { step: "source", src: "github" };
  function openAdd() { add.step = "source"; renderAdd(); }
  function renderAdd() {
    let body = "", foot = "", title = "Add to Library";
    if (add.step === "source") {
      body = `<p class="muted">Where is it coming from?</p><div class="srcgrid">
        ${[["github", "GitHub URL", "Install a public repo"], ["zip", "Upload ZIP", "A downloaded archive"], ["local", "Local File / Folder", "Something on disk"], ["paste", "Paste Content", "A prompt or skill you copied"]].map(([k, t, d]) => `<button class="srcopt" data-src="${k}"><div class="t">${t}</div><div class="d">${d}</div></button>`).join("")}
      </div>`;
      foot = `<button class="btn" data-x>Cancel</button><span></span>`;
    } else if (add.step === "input") {
      body = `<p class="muted">Paste a GitHub URL — we'll inspect and propose where each piece goes before anything is installed.</p>
        <input class="input" id="ghurl" placeholder="https://github.com/example/presentation-toolkit" value="https://github.com/example/presentation-toolkit"/>`;
      foot = `<button class="btn" data-back>Back</button><button class="btn primary" data-inspect>Inspect</button>`;
    } else if (add.step === "inspecting") {
      title = "Inspecting repository";
      const stages = ["Downloaded metadata", "Found 31 files", "Classifying contents", "Checking for duplicates", "Preparing routing plan"];
      body = `<div>${stages.map((s, idx) => `<div class="stage ${idx < add.prog ? "done" : idx === add.prog ? "active" : ""}"><span class="m">${idx < add.prog ? "✓" : idx === add.prog ? "→" : "○"}</span>${esc(s)}</div>`).join("")}</div>`;
      foot = `<span class="faint">Working…</span><span></span>`;
    } else if (add.step === "review") {
      title = "Review installation";
      const routes = [
        ["skill", "Presentation Design", "Presentation", "skills/presentation-design/", "high"],
        ["prompt", "Slide Review", "Presentation", "prompts/presentation/slide-review.md", "high"],
        ["workflow", "Build Deck", "Presentation", "workflows/build-presentation/", "high"],
        ["reference", "Chart Examples", "Data Visualization", "references/chart-patterns/", "review"],
      ];
      body = `<p class="muted"><strong>Presentation Toolkit</strong> · github.com/example/presentation-toolkit</p>
        <p class="muted">We found <strong>3 skills · 8 prompts · 1 workflow · 17 references</strong>.</p>
        <div class="section" style="margin-top:14px"><h2>Recommended routing</h2>
        ${routes.map(([k, n, c, p, cf]) => `<div class="route"><span>${cf === "high" ? "✓" : "⚠"}</span><span><div>${kindTag(k)} <strong>${esc(n)}</strong></div><div class="path mono">${esc(p)}</div></span><span class="conf ${cf}">${cf === "high" ? "High confidence" : "Needs review"}</span></div>`).join("")}
        </div>
        <div class="conflict"><strong>⚠ Possible overlap.</strong> Incoming <em>Presentation Design</em> may overlap with an existing skill. <button class="btn sm" data-compare>Compare</button></div>`;
      foot = `<button class="btn" data-x>Cancel</button><button class="btn primary" data-install>Install 29 items</button>`;
    } else if (add.step === "installing") {
      title = "Installing"; body = `<div class="stage active"><span class="m">→</span>Installing 29 items…</div>`; foot = `<span></span><span></span>`;
    } else if (add.step === "done") {
      title = "Install complete";
      body = `<p class="muted"><strong>29 items added</strong></p><div class="summary" style="margin:10px 0"><div class="s"><span class="n">3</span><span class="l">Skills</span></div><div class="s"><span class="n">8</span><span class="l">Prompts</span></div><div class="s"><span class="n">1</span><span class="l">Workflow</span></div><div class="s"><span class="n">17</span><span class="l">References</span></div></div>
        <p class="muted">Added to <span class="tag">Presentation</span> <span class="tag">Data Visualization</span></p>`;
      foot = `<button class="btn" data-nav-close="library/all">View installed items</button><div style="display:flex;gap:8px"><button class="btn" data-nav-close="projects">Enable for project</button><button class="btn primary" data-x>Done</button></div>`;
    }
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>${title}</h2><button class="btn sm" data-x>×</button></div><div class="mbody">${body}</div><div class="mfoot">${foot}</div></div></div>`);
    const ov = document.getElementById("overlay");
    ov.querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
    ov.querySelectorAll("[data-src]").forEach(b => b.onclick = () => { add.src = b.dataset.src; add.step = b.dataset.src === "github" ? "input" : "input"; renderAdd(); });
    const back = ov.querySelector("[data-back]"); if (back) back.onclick = () => { add.step = "source"; renderAdd(); };
    const ins = ov.querySelector("[data-inspect]"); if (ins) ins.onclick = () => { add.step = "inspecting"; add.prog = 0; renderAdd(); tickInspect(); };
    const inst = ov.querySelector("[data-install]"); if (inst) inst.onclick = () => { add.step = "installing"; renderAdd(); setTimeout(() => { add.step = "done"; renderAdd(); }, 900); };
    const cmp = ov.querySelector("[data-compare]"); if (cmp) cmp.onclick = openCompare;
    ov.querySelectorAll("[data-nav-close]").forEach(b => b.onclick = () => { closeOverlay(); location.hash = "#/" + b.dataset.navClose; });
  }
  function tickInspect() { const iv = setInterval(() => { add.prog++; if (add.step !== "inspecting") { clearInterval(iv); return; } if (add.prog > 5) { clearInterval(iv); add.step = "review"; } renderAdd(); }, 500); }

  function openCompare() {
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>Compare</h2><button class="btn sm" data-x>×</button></div><div class="mbody">
      <div class="compare">
        <div class="col"><div class="crumb">Existing</div><strong>Presentation Design</strong><div class="field"><h4>Unique</h4><p>Layout rules · Typography</p></div></div>
        <div class="col"><div class="crumb">Incoming</div><strong>Presentation Visual Design</strong><div class="field"><h4>Unique</h4><p>Motion patterns · Diagram selection</p></div></div>
      </div>
      <div class="field" style="margin-top:14px"><h4>Shared concepts</h4><p>Hierarchy · Whitespace · Slide composition</p></div>
    </div><div class="mfoot"><button class="btn" data-back-review>Keep existing</button><div style="display:flex;gap:8px"><button class="btn" data-back-review>Install separately</button><button class="btn" data-back-review>Merge unique</button><button class="btn" data-back-review>Replace</button></div></div></div></div>`);
    const ov = document.getElementById("overlay");
    ov.querySelectorAll("[data-x],[data-back-review]").forEach(b => b.onclick = () => { add.step = "review"; renderAdd(); });
  }

  function openCreate() {
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>New item</h2><button class="btn sm" data-x>×</button></div><div class="mbody">
      <p class="muted">What are you creating?</p>
      <div class="chips" style="margin-bottom:14px">${["Skill", "Prompt", "Workflow", "Reference", "Template"].map(t => `<button class="chip">${t}</button>`).join("")}</div>
      <div class="filterbar" style="margin:0 0 12px"><div class="tabs"><button class="active">Form</button><button>Markdown</button></div></div>
      <div class="field"><h4>Name</h4><input class="input" placeholder="e.g. Presentation QA"/></div>
      <div class="field"><h4>Purpose</h4><input class="input" placeholder="What reusable capability does this provide?"/></div>
      <div class="field"><h4>Activate when</h4><input class="input" placeholder="Explicit trigger conditions…"/></div>
      <div class="field"><h4>Category</h4><select class="f">${cats().map(c => `<option>${esc(c)}</option>`).join("")}</select></div>
    </div><div class="mfoot"><button class="btn" data-x>Cancel</button><button class="btn primary" data-x>Create</button></div></div></div>`);
    document.getElementById("overlay").querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
  }

  /* ---------- Command palette ---------- */
  const COMMANDS = [
    ["Search Library", () => location.hash = "#/library"],
    ["Add to Library", openAdd], ["Install from GitHub", () => { openAdd(); add.step = "input"; renderAdd(); }],
    ["Create Skill", openCreate], ["Create Prompt", openCreate], ["Create Workflow", openCreate],
    ["Open Inbox", () => location.hash = "#/inbox"], ["Review Updates", () => location.hash = "#/health"],
    ["Sync Cursor", () => toast("Syncing Cursor…")], ["Sync Claude Code", () => toast("Syncing Claude Code…")],
    ["Run Doctor", () => location.hash = "#/health"], ["Open Projects", () => location.hash = "#/projects"],
  ];
  function openPalette() {
    overlay(`<div class="palette"><div class="box"><input id="palq" placeholder="Type a command or search…" autocomplete="off"/><div class="results" id="palr"></div></div></div>`);
    const inp = document.getElementById("palq"), res = document.getElementById("palr");
    let sel = 0, list = COMMANDS.slice();
    const draw = () => { res.innerHTML = list.map((c, i) => `<div class="pi ${i === sel ? "sel" : ""}" data-i="${i}"><span>${esc(c[0])}</span><span class="k kbd">↵</span></div>`).join(""); res.querySelectorAll(".pi").forEach(el => el.onclick = () => run(+el.dataset.i)); };
    const run = i => { const c = list[i]; closeOverlay(); if (c) c[1](); };
    inp.oninput = () => { const q = inp.value.toLowerCase(); const items = COMMANDS.filter(c => c[0].toLowerCase().includes(q)); const hits = ITEMS.filter(it => it.title.toLowerCase().includes(q)).slice(0, 6).map(it => [`Open: ${it.title}`, () => location.hash = "#/item/" + encodeURIComponent(it.id)]); list = q ? items.concat(hits) : COMMANDS.slice(); sel = 0; draw(); };
    inp.onkeydown = e => { if (e.key === "ArrowDown") { sel = Math.min(sel + 1, list.length - 1); draw(); e.preventDefault(); } else if (e.key === "ArrowUp") { sel = Math.max(sel - 1, 0); draw(); e.preventDefault(); } else if (e.key === "Enter") run(sel); else if (e.key === "Escape") closeOverlay(); };
    draw(); inp.focus();
  }
  function toast(msg) { const t = h(`<div class="toast">${esc(msg)}</div>`); document.body.appendChild(t); setTimeout(() => t.remove(), 1600); }

  /* ---------- Actions (optimistic; this is a front-end prototype) ---------- */
  function addActivity(action, target) { (D.activity = D.activity || []).unshift({ action, target, when: "just now" }); }
  function currentRoute() { return location.hash.replace(/^#\/?/, "").split("?")[0]; }
  function rerenderView() { const y = window.scrollY; router(); window.scrollTo(0, y); }
  function rebuildAll() { const y = window.scrollY; shell(); router(); window.scrollTo(0, y); }

  function handleAction(action, ds) {
    switch (action) {
      case "sync-integration": return syncIntegration(ds.name);
      case "setup-integration": return setupIntegration(ds.name);
      case "review-inbox": return openInboxReview(ds.name);
      case "review-issue": return openIssueReview(+ds.i);
      case "disable-cap": return disableCap(ds.proj, ds.name);
      case "sync-project-integration": return syncProjectIntegration(ds.proj, ds.name);
      case "enable-item": return enableItem(ds.id);
      case "edit-item": return openCreate();
      case "rename-item": return openRename(ds.id);
      case "push-item": return pushItem(ds.id, ds.plat);
      case "change-home": return toast("Choose a library folder…");
      default: return undefined;
    }
  }

  /* Installed-in panel (drawer) + push to an environment it's not in yet. */
  function installPanel(i) {
    const inn = i.installed_in || [];
    const rows = platforms().map(p => {
      const on = inn.includes(p);
      return `<div class="instrow"><span class="idot ${on ? "on" : ""}"><i>${esc(platInitial(p))}</i></span><span class="ip-name">${esc(p)}</span><span class="ip-status ${on ? "on" : ""}">${on ? "Installed" : "Not installed"}</span>${on ? "" : `<button class="btn sm" data-action="push-item" data-id="${esc(i.id)}" data-plat="${esc(p)}">Push</button>`}</div>`;
    }).join("");
    return `<div class="field"><h4>Installed in</h4><div class="instlist">${rows}</div></div>`;
  }
  function pushItem(id, plat) {
    const it = byId[id]; if (!it) return;
    it.installed_in = it.installed_in || [];
    if (!it.installed_in.includes(plat)) it.installed_in.push(plat);
    addActivity("Installed", it.title + " → " + plat);
    toast("Pushed " + it.title + " to " + plat);
    openItem(id); // refresh drawer so status + push buttons update
  }

  /* Rename an item — propagates the new name across every in-memory reference,
     then re-syncs the environments it's installed in. (Persisting to disk /
     the real tool integrations needs a backend; this is the front-end path.) */
  function renameItem(id, newTitle) {
    const it = byId[id]; if (!it) return;
    newTitle = newTitle.trim(); if (!newTitle || newTitle === it.title) { if (newTitle === it.title) location.hash = "#/item/" + encodeURIComponent(id); return; }
    const oldTitle = it.title, oldName = it.name, newName = kebab(newTitle) || oldName, newId = it.kind + ":" + newName;
    it.title = newTitle; it.name = newName; it.id = newId;
    const swap = (arr, from, to) => { if (arr) arr.forEach((v, ix) => { if (v === from) arr[ix] = to; }); };
    ITEMS.forEach(x => {
      swap(x.depends_on, oldName, newName); swap(x.uses_list, oldName, newName);
      swap(x.used_by, oldTitle, newTitle); swap(x.references, oldTitle, newTitle);
      if (x.steps) x.steps.forEach(s => swap(s.uses, oldName, newName));
    });
    (D.projects || []).forEach(p => { swap(p.skills, oldName, newName); swap(p.workflows, oldTitle, newTitle); swap(p.references, oldTitle, newTitle); });
    byId = Object.fromEntries(ITEMS.map(x => [x.id, x]));
    byTitle = Object.fromEntries(ITEMS.map(x => [x.title, x]));
    addActivity("Renamed", oldTitle + " → " + newTitle);
    const where = (it.installed_in || []).join(", ");
    toast("Renamed to “" + newTitle + "”" + (where ? " · re-synced " + where : ""));
    location.hash = "#/item/" + encodeURIComponent(newId); // reopen drawer at new id
  }
  function openRename(id) {
    const it = byId[id]; if (!it) return;
    const label = KIND[it.kind] ? KIND[it.kind].label.toLowerCase() : "item";
    const where = (it.installed_in && it.installed_in.length) ? it.installed_in.join(", ") : "no environments yet";
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>Rename ${esc(label)}</h2><button class="btn sm" data-x>×</button></div><div class="mbody">
      <div class="field"><h4>Display name</h4><input class="input" id="rn-name" value="${esc(it.title)}" autocomplete="off" /></div>
      <p class="muted">Updates every reference to this ${esc(label)} and re-syncs the environments it's installed in (${esc(where)}). The on-disk id becomes <span class="mono" id="rn-id"></span>.</p>
    </div><div class="mfoot"><button class="btn" data-x>Cancel</button><button class="btn primary" id="rn-save">Rename &amp; sync</button></div></div></div>`);
    const ov = document.getElementById("overlay");
    const input = ov.querySelector("#rn-name"), idEl = ov.querySelector("#rn-id");
    const upd = () => { idEl.textContent = it.kind + ":" + (kebab(input.value) || "…"); };
    input.oninput = upd; upd();
    ov.querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
    ov.querySelector("#rn-save").onclick = () => { const v = input.value; closeOverlay(); renameItem(id, v); };
    input.focus(); input.select();
  }

  function syncIntegration(name) {
    const it = (D.integrations || []).find(x => x.name === name); if (!it) return;
    toast("Syncing " + name + "…");
    setTimeout(() => {
      it.last_synced = "just now"; addActivity("Synced", name);
      toast(name + " synced");
      if (currentRoute().startsWith("integrations")) rerenderView();
    }, 700);
  }
  function setupIntegration(name) {
    const it = (D.integrations || []).find(x => x.name === name); if (!it) return;
    it.status = "connected"; it.count = ITEMS.filter(x => x.kind === "skill").length; it.last_synced = "just now";
    addActivity("Connected", name); toast(name + " connected"); rerenderView();
  }
  function disableCap(projId, name) {
    const p = (D.projects || []).find(x => x.id === projId); if (!p) return;
    p.skills = p.skills.filter(s => s !== name);
    const it = byId["skill:" + name]; if (it && it.enabled_in) it.enabled_in = it.enabled_in.filter(x => x !== p.name);
    addActivity("Disabled", name + " · " + p.name); toast("Disabled " + name); rerenderView();
  }
  function syncProjectIntegration(projId, name) {
    const p = (D.projects || []).find(x => x.id === projId); if (!p) return;
    p.integrations[name] = "synced"; addActivity("Synced", name + " · " + p.name); toast(name + " synced"); rerenderView();
  }
  function enableItem(id) {
    const it = byId[id]; if (!it) return;
    const proj = (D.projects || [])[0];
    if (it.kind === "skill" && proj) {
      if (!proj.skills.includes(it.name)) proj.skills.push(it.name);
      it.enabled_in = it.enabled_in || []; if (!it.enabled_in.includes(proj.name)) it.enabled_in.push(proj.name);
      addActivity("Enabled", it.title + " · " + proj.name); toast("Enabled " + it.title + " in " + proj.name);
      openItem(id); // refresh the drawer so "Enabled in" reflects the change
    } else {
      addActivity("Used", it.title); toast(it.title + " ready to use");
    }
  }

  function openInboxReview(name) {
    const it = (D.inbox || []).find(x => x.name === name); if (!it) return;
    const opts = ["skill", "prompt", "workflow", "reference", "template"]
      .map(k => `<button class="chip ${k === it.detected ? "active" : ""}" data-k="${k}">${KIND[k] ? KIND[k].label : k}</button>`).join("");
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>Review · ${esc(it.name)}</h2><button class="btn sm" data-x>×</button></div><div class="mbody">
      <p class="muted">Suggested: <strong>${esc(it.detected)}</strong> · ${esc(it.category)} — ${esc(it.reason)}</p>
      <div class="field"><h4>File as</h4><div class="chips" id="ib-kinds">${opts}</div></div>
      <div class="field"><h4>Source</h4><p class="mono">${esc(it.source)}</p></div>
    </div><div class="mfoot"><button class="btn" data-x>Cancel</button><button class="btn primary" data-file>File item</button></div></div></div>`);
    const ov = document.getElementById("overlay");
    let chosen = it.detected;
    ov.querySelectorAll("#ib-kinds .chip").forEach(c => c.onclick = () => { ov.querySelectorAll("#ib-kinds .chip").forEach(x => x.classList.remove("active")); c.classList.add("active"); chosen = c.dataset.k; });
    ov.querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
    ov.querySelector("[data-file]").onclick = () => {
      D.inbox = (D.inbox || []).filter(x => x.name !== name);
      addActivity("Filed", name + " → " + chosen); closeOverlay(); toast("Filed " + name + " as " + chosen); rebuildAll();
    };
  }

  function suggestFix(type) {
    if (/reference/i.test(type)) return "Repoint the reference to an existing item, or remove it.";
    if (/duplicate/i.test(type)) return "Compare the two items, then merge unique content or keep them separate.";
    return "Review the details and update the affected item.";
  }
  function openIssueReview(ix) {
    const iss = (D.health.issues || [])[ix]; if (!iss) return;
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>${esc(iss.type)}</h2><button class="btn sm" data-x>×</button></div><div class="mbody">
      <p class="muted">${esc(iss.detail)}</p>
      <div class="field"><h4>Suggested fix</h4><p>${esc(suggestFix(iss.type))}</p></div>
    </div><div class="mfoot"><button class="btn" data-x>Dismiss</button><button class="btn primary" data-resolve>Mark resolved</button></div></div></div>`);
    const ov = document.getElementById("overlay");
    ov.querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
    ov.querySelector("[data-resolve]").onclick = () => {
      D.health.issues = (D.health.issues || []).filter((_, i) => i !== ix);
      (D.health.ok = D.health.ok || []).push(iss.type + " resolved");
      addActivity("Resolved", iss.type); closeOverlay(); toast("Marked resolved"); rerenderView();
    };
  }

  /* ---------- Boot ---------- */
  window.addEventListener("keydown", e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") { e.preventDefault(); openPalette(); }
    else if (e.key === "Escape") closeAll();
  });
  window.addEventListener("hashchange", router);

  (async function boot() {
    await loadLiveData(); // falls back to the bundled snapshot on failure
    shell();
    router();
  })();
})();
