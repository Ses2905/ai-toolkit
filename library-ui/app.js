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
  let toolkitHome = (() => { try { return localStorage.getItem("ai-toolkit-home"); } catch (e) { return null; } })() || "$AI_TOOLKIT_HOME (~/.ai-toolkit)";

  /* ---------- Persistence layer ----------
     The library data is rebuilt from the catalog on every load, so any user
     action (setting up/syncing an integration, pushing an item, syncing a
     project, triaging the inbox, renaming) would otherwise reset on reload.
     We keep a single versioned localStorage store of those mutations, keyed by
     stable ids/names, and re-apply it after the catalog loads. All access is
     guarded so a corrupt/blocked store never breaks the live-catalog load or
     the snapshot fallback. Write-through: action handlers call persist* below. */
  const STORE_KEY = "ai-toolkit-state-v1";
  function loadStore() {
    try {
      const raw = localStorage.getItem(STORE_KEY);
      if (!raw) return {};
      const parsed = JSON.parse(raw);
      return (parsed && typeof parsed === "object") ? parsed : {};
    } catch (e) { return {}; }
  }
  let store = loadStore();
  function persistStore() { try { localStorage.setItem(STORE_KEY, JSON.stringify(store)); } catch (e) { /* ignore quota/denied */ } }
  function persistIntegration(name, patch) {
    store.integrations = store.integrations || {};
    store.integrations[name] = Object.assign({}, store.integrations[name], patch);
    persistStore();
  }
  function persistItemInstall(id, plat) {
    store.installs = store.installs || {};
    const arr = store.installs[id] = store.installs[id] || [];
    if (!arr.includes(plat)) arr.push(plat);
    persistStore();
  }
  function persistProjectIntegration(projId, name, stateVal) {
    store.projectIntegrations = store.projectIntegrations || {};
    const p = store.projectIntegrations[projId] = store.projectIntegrations[projId] || {};
    p[name] = stateVal;
    persistStore();
  }
  function persistInbox(name, patch) {
    store.inbox = store.inbox || {};
    store.inbox[name] = Object.assign({}, store.inbox[name], patch);
    persistStore();
  }
  function persistRename(origId, title) {
    store.renames = store.renames || {};
    store.renames[origId] = { title };
    persistStore();
  }
  // Re-apply persisted user mutations onto a freshly built D, merging by stable
  // ids/names so it stays correct if the catalog changes underneath us.
  function applyPersistedState() {
    if (!store || typeof store !== "object") return;
    // Renames first, so id-keyed installs below line up with post-rename ids.
    if (store.renames && typeof store.renames === "object") {
      for (const origId of Object.keys(store.renames)) {
        const r = store.renames[origId];
        if (r && r.title) applyRename(origId, r.title);
      }
    }
    if (store.integrations && Array.isArray(D.integrations)) {
      for (const integ of D.integrations) {
        const saved = store.integrations[integ.name];
        if (!saved) continue;
        if (saved.status) integ.status = saved.status;
        if ("last_synced" in saved) integ.last_synced = saved.last_synced;
        if (typeof saved.count === "number") integ.count = saved.count;
      }
    }
    if (store.installs && typeof store.installs === "object") {
      for (const id of Object.keys(store.installs)) {
        const it = byId[id];
        if (!it || !Array.isArray(store.installs[id])) continue;
        it.installed_in = it.installed_in || [];
        for (const plat of store.installs[id]) if (!it.installed_in.includes(plat)) it.installed_in.push(plat);
      }
    }
    if (store.projectIntegrations && Array.isArray(D.projects)) {
      for (const p of D.projects) {
        const saved = store.projectIntegrations[p.id];
        if (!saved) continue;
        p.integrations = p.integrations || {};
        for (const k of Object.keys(saved)) p.integrations[k] = saved[k];
      }
    }
    if (store.inbox && Array.isArray(D.inbox)) {
      const kept = [];
      for (const it of D.inbox) {
        const saved = store.inbox[it.name];
        if (saved) {
          if (saved.deleted) continue;
          if ("read" in saved) it.read = saved.read;
          if ("filedAs" in saved) it.filedAs = saved.filedAs;
        }
        kept.push(it);
      }
      D.inbox = kept;
    }
  }

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
  // Naming conventions: "&" becomes "+" everywhere; kebab domains render Title Case.
  const plusify = s => String(s == null ? "" : s).replace(/&/g, "+");
  const titleCase = s => String(s).replace(/[-_]/g, " ").replace(/\b\w/g, c => c.toUpperCase());
  const catLabel = c => plusify(/\s/.test(c) ? c : titleCase(c));

  // Domain (category) definitions surfaced as hover tooltips.
  const DOMAIN_DEFS = {
    "Product & Discovery": "Frame problems, run discovery, and shape product strategy before building.",
    "Design & Frontend": "Distinctive UI, design systems, typography, and visual direction.",
    "Motion & Animation": "Add, audit, and review motion with a real craft bar for animation.",
    "Presentations & Diagrams": "Build editable decks, HTML presentations, and self-contained diagrams.",
    "Engineering Workflow": "Plan, debug from evidence, review the diff, ship a clean commit, and hand off.",
    "Setup & Install": "Install the toolkit and pull in external skill catalogs and tools.",
    "Data Visualization": "Chart and data-display patterns that communicate the insight clearly.",
    "Research": "Discovery inputs — personas, interviews, and evidence to draw on.",
    "agent-tools": "Executable helpers that install, index, and route toolkit content.",
  };
  const domainDef = c => DOMAIN_DEFS[c] || "";
  const tipAttr = c => (domainDef(c) ? ` data-tip="${esc(domainDef(c))}"` : "");
  const h = (html) => { const t = document.createElement("template"); t.innerHTML = html.trim(); return t.content.firstElementChild; };
  const kindsPresent = () => KIND_ORDER.filter(k => ITEMS.some(i => i.kind === k));
  const cats = () => Array.from(new Set(ITEMS.map(i => i.category))).sort();

  const state = { kind: "all", cat: "All", source: "All", sort: "name", view: "list", q: "" };

  // Environments the library can install/sync into (from the integrations tier).
  const platforms = () => (D.integrations || []).map(x => x.name);
  // Destinations an asset can be made available in. Kept as a reusable array so
  // more targets can be added without touching the availability rendering.
  const DESTINATIONS = ["Cursor", "Claude Code", "Codex", "ChatGPT"];
  // Curated, real outbound resources for finding new skills/prompts/workflows.
  // These are honest external links — not fabricated "recommended for you" items.
  const DISCOVER_LINKS = [
    { name: "Cursor Directory", url: "https://cursor.directory", desc: "Community-curated rules, MCP servers and prompts for Cursor." },
    { name: "awesome-cursorrules", url: "https://github.com/PatrickJS/awesome-cursorrules", desc: "A large, curated collection of .cursorrules files to adapt." },
    { name: "Anthropic Cookbook", url: "https://github.com/anthropics/anthropic-cookbook", desc: "Official Claude recipes, prompt patterns and agent skills." },
    { name: "OpenAI Cookbook", url: "https://github.com/openai/openai-cookbook", desc: "Example code and guides for building with OpenAI models." },
  ];
  // Best-effort docs surfaces for "where my synced assets live in each tool".
  // These are public documentation pages, not fabricated in-app deep links.
  const TOOL_DOCS = {
    "Cursor": { url: "https://docs.cursor.com/context/rules", label: "Open Cursor rules" },
    "Claude Code": { url: "https://docs.anthropic.com/en/docs/claude-code/memory", label: "Open Claude Code memory" },
    "Codex": { url: "https://platform.openai.com/docs", label: "Open Codex docs" },
    "ChatGPT": { url: "https://platform.openai.com/docs", label: "Open OpenAI docs" },
  };
  // A contained code region with a Copy button that writes to the clipboard.
  let SNIP_SEQ = 0;
  function codeSnippet(text, label) {
    const id = "snip-" + (++SNIP_SEQ);
    return `<div class="snippet"><code id="${id}" class="snipcode">${esc(text)}</code><button class="btn sm snipcopy" data-action="copy-snippet" data-target="${id}" data-label="${esc(label || "")}" title="Copy">Copy</button></div>`;
  }
  function copySnippet(targetId, label) {
    const el = document.getElementById(targetId); if (!el) return;
    const text = el.textContent || "";
    const done = () => toast((label ? label + " " : "") + "Copied");
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(text).then(done, () => fallbackCopy(text, done)); }
      else fallbackCopy(text, done);
    } catch (_e) { fallbackCopy(text, done); }
  }
  function fallbackCopy(text, done) {
    try { const ta = document.createElement("textarea"); ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0"; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); done(); } catch (_e) { done(); }
  }

  /* ---------- Shell ---------- */
  function shell() {
    const item = (route, ic, label, badge) => `<a href="#/${route}" data-route="${route}"><span class="ic">${ic}</span>${esc(label)}${badge != null ? `<span class="count">${badge}</span>` : ""}</a>`;
    const subs = kindsPresent().map(k => `<a href="#/library/${k}" data-route="library/${k}"><span class="ic">${KIND[k].glyph}</span>${KIND[k].plural}<span class="count">${D.counts[k] || 0}</span></a>`).join("");
    document.getElementById("app").innerHTML = `
      <div class="shell">
        <aside class="sidebar" id="sidebar">
          <div class="brand"><span class="mark" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8v11"/><path d="M12 8a4 4 0 0 0-4-4H3.6A1.6 1.6 0 0 0 2 5.6V17a1.6 1.6 0 0 0 1.6 1.6H8a3.4 3.4 0 0 1 4 1.8"/><path d="M12 8a4 4 0 0 1 4-4h4.4A1.6 1.6 0 0 1 22 5.6V17a1.6 1.6 0 0 1-1.6 1.6H16a3.4 3.4 0 0 0-4 1.8"/><path d="M18.4 1l.55 1.45L20.4 3l-1.45.55L18.4 5l-.55-1.45L16.4 3l1.45-.55z" fill="currentColor" stroke="none"/></svg></span> AI Toolkit<span class="src-pill" data-src="${dataSource}" title="${dataSource === "live" ? "Reading the live catalog" : "Using the bundled snapshot"}">${dataSource}</span></div>
          <nav class="nav">
            ${item("home", "⌂", "Home")}
            <div class="group">AI Toolkit</div>
            ${item("library", "▤", "All", ITEMS.length)}
            <div class="sub">${subs}</div>
            <div class="group">Manage</div>
            ${item("discover", "◎", "Discover")}
            ${item("projects", "▦", "Projects")}
            ${item("integrations", "⇄", "Integrations")}
            ${item("settings", "⚙", "Settings")}
          </nav>
        </aside>
        <div class="main">
          <div class="topbar"><div class="topbar-inner">
            <button class="btn sm hamburger" id="ham">≡</button>
            <label class="topsearch"><span>⌕</span><input id="q" type="search" placeholder="Search your toolkit…" aria-label="Search your toolkit" /><span class="kbd">⌘K</span></label>
            <span class="spacer"></span>
            <button class="btn iconbtn bell" id="bell" aria-label="Notifications" aria-haspopup="true" aria-expanded="false"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>${bellBadgeHtml()}</button>
            <button class="btn" id="new">+ New</button>
            <button class="btn primary" id="add">+ Add to Toolkit</button>
          </div></div>
          <div id="notif" class="notif" hidden></div>
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
    notifOpen = false;
    document.getElementById("bell").onclick = (e) => { e.stopPropagation(); toggleNotif(); };
  }

  /* ---------- Notification center (topbar bell) ---------- */
  let notifOpen = false;
  const unreadInbox = () => (D.inbox || []).filter(x => !x.read);
  const bellBadgeHtml = () => { const n = unreadInbox().length; return n ? `<span class="badge">${n > 9 ? "9+" : n}</span>` : ""; };
  function updateBellBadge() {
    const b = document.getElementById("bell"); if (!b) return;
    const n = unreadInbox().length;
    let badge = b.querySelector(".badge");
    if (n) { const txt = n > 9 ? "9+" : String(n); if (badge) badge.textContent = txt; else b.insertAdjacentHTML("beforeend", `<span class="badge">${txt}</span>`); }
    else if (badge) badge.remove();
  }
  function notifPanelContent() {
    const un = unreadInbox();
    const head = `<div class="notif-head"><strong>Notifications</strong>${un.length ? `<span class="notif-count">${un.length} unread</span>` : ""}</div>`;
    const body = un.length
      ? `<div class="notif-list">${un.map(x => `<div class="notif-item">
          <div class="ni-top"><span class="kind" data-k="${x.detected}"><span class="g">${(KIND[x.detected] || KIND.reference).glyph}</span></span><span class="ni-name">${esc(x.name)}</span></div>
          <div class="ni-sub">Suggested: ${esc(x.detected)} · ${esc(catLabel(x.category))} — ${esc(x.reason)}</div>
          <div class="ni-actions"><button class="btn sm primary" data-nact="review" data-name="${esc(x.name)}">Review</button><button class="btn sm" data-nact="mark-read" data-name="${esc(x.name)}">Mark read</button><button class="btn sm danger" data-nact="delete" data-name="${esc(x.name)}">Delete</button></div>
        </div>`).join("")}</div>`
      : `<div class="notif-empty"><p>You're all caught up — inbox zero.</p></div>`;
    const foot = `<div class="notif-foot"><a href="#/inbox" data-nact="viewall">View all →</a></div>`;
    return head + body + foot;
  }
  function renderNotifPanel() {
    const p = document.getElementById("notif"); if (!p) return;
    p.innerHTML = notifPanelContent();
    p.querySelectorAll("[data-nact]").forEach(b => b.onclick = (e) => {
      const act = b.dataset.nact, name = b.dataset.name;
      if (act === "viewall") { closeNotif(); return; }
      e.preventDefault();
      if (act === "review") { closeNotif(); return openInboxReview(name); }
      if (act === "mark-read") { const it = (D.inbox || []).find(x => x.name === name); if (it) { it.read = true; it.filedAs = undefined; persistInbox(name, { read: true, filedAs: undefined }); addActivity("Marked read", name); } toast(name + " marked read"); return afterNotifMutate(); }
      if (act === "delete") { D.inbox = (D.inbox || []).filter(x => x.name !== name); persistInbox(name, { deleted: true }); addActivity("Deleted", name + " (inbox)"); toast("Deleted " + name); return afterNotifMutate(); }
    });
  }
  function afterNotifMutate() { updateBellBadge(); renderNotifPanel(); if (currentRoute().startsWith("inbox")) rerenderView(); }
  function openNotif() { notifOpen = true; const p = document.getElementById("notif"); if (!p) return; p.hidden = false; renderNotifPanel(); const b = document.getElementById("bell"); if (b) b.setAttribute("aria-expanded", "true"); }
  function closeNotif() { notifOpen = false; const p = document.getElementById("notif"); if (p) p.hidden = true; const b = document.getElementById("bell"); if (b) b.setAttribute("aria-expanded", "false"); }
  function toggleNotif() { notifOpen ? closeNotif() : openNotif(); }

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
    const stats = KIND_ORDER.filter(k => c[k]).map(k => `<button class="statcard" data-nav="library/${k}"><span class="sc-ic kind" data-k="${k}"><span class="g">${KIND[k].glyph}</span></span><span class="sc-n">${c[k] || 0}</span><span class="sc-l">${KIND[k].plural}</span></button>`).join("");
    const unread = (D.inbox || []).filter(x => !x.read).length;
    const att = [];
    if (unread) att.push([`${unread} item${unread > 1 ? "s" : ""} need classification`, "inbox"]);
    if ((D.updates || []).length) att.push([`${D.updates.length} upstream update${D.updates.length > 1 ? "s" : ""} available`, "health"]);
    (D.health.issues || []).forEach(i => att.push([`${i.type}: ${i.detail}`, "health"]));
    const attHtml = att.length ? att.map(([t, r]) => `<div class="att"><span class="dot"></span><span>${esc(t)}</span><button class="btn sm go" data-nav="${r}">Review</button></div>`).join("") : `<div class="att info"><span class="dot"></span><span>Everything looks healthy — nothing needs your attention.</span></div>`;
    const cols = (D.collections || []).slice(0, 10).map(x => `<button class="chip" data-nav="library/all"${tipAttr(x.name)}>${esc(catLabel(x.name))}<span class="c">${x.count}</span></button>`).join("");
    const resources = DISCOVER_LINKS.map(r => `<a class="res-row" href="${esc(r.url)}" target="_blank" rel="noopener">
        <span class="res-ic" aria-hidden="true">◎</span>
        <span class="res-main"><span class="res-name">${esc(r.name)}<span class="ext" aria-hidden="true">↗</span></span><span class="res-sub">${esc(r.desc)}</span></span>
      </a>`).join("");
    return `
      <div class="page home">
        <div class="page-head"><h1>Your AI Toolkit</h1><p>Everything you can compose — skills, prompts, workflows, tools and references — in one place.</p></div>
        <div class="home-hero">
          <label class="topsearch home-search"><span>⌕</span><input placeholder="Search your toolkit…" onkeydown="if(event.key==='Enter'){location.hash='#/search?q='+encodeURIComponent(this.value)}"/></label>
        </div>
        <div class="section"><h2>Discover more</h2><p class="muted lead">Places to discover new skills, prompts and workflows to add.</p><div class="reslist">${resources}</div></div>
        <div class="section"><h2>AI Toolkit summary</h2><div class="statgrid">${stats}</div></div>
        <div class="section"><h2>Needs attention</h2><div class="attention">${attHtml}</div></div>
        <div class="section"><h2>Browse by domain</h2><div class="chips">${cols}</div></div>
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
  const platInitial = p => ({ "Cursor": "Cu", "Claude Code": "Cl", "Claude": "Cl", "Codex": "Cx", "ChatGPT": "Gp" }[p] || String(p).slice(0, 2));
  // Monochrome brand marks (inherit currentColor so they take the palette).
  const PLAT_LOGOS = {
    "Cursor": '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><path d="M5 2.6l14.2 8.2a.6.6 0 0 1-.13 1.1l-6 1.72 2.98 5.86a.6.6 0 0 1-.27.8l-1.9.96a.6.6 0 0 1-.8-.27l-2.98-5.86-4.63 4.2a.6.6 0 0 1-1-.45V3.1a.6.6 0 0 1 .9-.5z"/></svg>',
    "Claude Code": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2.5v19M2.5 12h19M5.2 5.2l13.6 13.6M18.8 5.2L5.2 18.8"/></svg>',
    "Codex": '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><circle cx="12" cy="4.6" r="2.3"/><circle cx="12" cy="19.4" r="2.3"/><circle cx="5.6" cy="8.3" r="2.3"/><circle cx="18.4" cy="8.3" r="2.3"/><circle cx="5.6" cy="15.7" r="2.3"/><circle cx="18.4" cy="15.7" r="2.3"/></svg>',
    "ChatGPT": '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round" aria-hidden="true"><path d="M4 5.5h16a1.5 1.5 0 0 1 1.5 1.5v8A1.5 1.5 0 0 1 20 16.5H9l-4.5 3.5v-3.5H4A1.5 1.5 0 0 1 2.5 15V7A1.5 1.5 0 0 1 4 5.5z"/></svg>',
  };
  PLAT_LOGOS["Claude"] = PLAT_LOGOS["Claude Code"];
  const platLogo = p => PLAT_LOGOS[p] || `<i class="plchar">${esc(platInitial(p))}</i>`;

  function installDots(i) {
    const inn = i.installed_in || [];
    const pl = platforms();
    return `<span class="insti">${pl.map(p => { const on = inn.includes(p); const t = `${p}: ${on ? "installed" : "not installed"}`; return `<span class="idot ${on ? "on" : ""}" title="${esc(t)}" aria-label="${esc(t)}">${platLogo(p)}</span>`; }).join("")}</span>`;
  }
  function card(i, showKind = true) {
    const top = showKind ? `<div class="top">${kindTag(i.kind)}${installDots(i)}</div>` : `<div class="top solo">${installDots(i)}</div>`;
    return `<div class="card" data-item="${esc(i.id)}">
      ${top}
      <div class="name">${esc(i.title)}</div>
      <div class="meta"><span class="tag"${tipAttr(i.category)}>${esc(catLabel(i.category))}</span><span>${i.command ? "/" + esc(i.command) : (i.used_by && i.used_by.length ? "Used by " + i.used_by.length : "")}</span></div>
    </div>`;
  }
  function listRow(i, showKind = true) {
    return `<div class="row" data-item="${esc(i.id)}">
      <span class="kind" data-k="${i.kind}"><span class="g">${KIND[i.kind].glyph}</span></span>
      <span class="nmwrap"><span class="nm">${esc(i.title)}</span>${showKind ? `<span class="kpill" data-k="${i.kind}">${KIND[i.kind].label}</span>` : ""}</span>
      <span class="sub cat"${tipAttr(i.category)}>${esc(catLabel(i.category))}</span>
      ${installDots(i)}
      <span class="sub date">${esc(i.date_updated || "")}</span>
    </div>`;
  }
  const listHeaderRow = () => `<div class="row lhead" aria-hidden="true"><span></span><span>Name</span><span>Domain</span><span>Availability</span><span class="date">Updated</span></div>`;
  function libResults() {
    const list = filtered();
    if (!list.length) return `<div id="libresults"><div class="empty"><h3>Nothing matches</h3><p>Try clearing a filter or searching a different term.</p></div></div>`;
    const showKind = state.kind === "all";
    const body = state.view === "list"
      ? `<div class="list sticky-head">${listHeaderRow()}${list.map(i => listRow(i, showKind)).join("")}</div>`
      : `<div class="grid">${list.map(i => card(i, showKind)).join("")}</div>`;
    return `<div id="libresults"><div class="count-line">${list.length} of ${ITEMS.length} items</div>${body}</div>`;
  }
  function viewLibrary(kind) {
    state.kind = kind || "all";
    const tabs = ["all", ...kindsPresent()].map(k => `<button data-kindtab="${k}" class="${state.kind === k ? "active" : ""}">${k === "all" ? "All" : KIND[k].plural}</button>`).join("");
    const catOpts = ['<option value="All">All domains</option>'].concat(cats().map(c => `<option value="${esc(c)}" ${state.cat === c ? "selected" : ""}>${esc(catLabel(c))}</option>`)).join("");
    const chips = [];
    if (state.kind !== "all") chips.push(`<span class="chipf">${KIND[state.kind].plural}<button data-clearf="kind">×</button></span>`);
    if (state.cat !== "All") chips.push(`<span class="chipf">${esc(catLabel(state.cat))}<button data-clearf="cat">×</button></span>`);
    const active = state.kind !== "all" && KIND[state.kind];
    const heading = active ? KIND[state.kind].plural : "AI Toolkit";
    const subtitle = active ? KIND[state.kind].desc : "Browse and manage everything you've installed.";
    return `<div class="page">
      <div class="page-head"><h1>${esc(heading)}</h1><p>${esc(subtitle)}</p></div>
      <label class="topsearch" style="max-width:none"><span>⌕</span><input id="libsearch" placeholder="Search your toolkit…" value="${esc(state.q)}"/></label>
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
    const head = `<div class="page-head"><h1>Search</h1><p>${qq ? `Results for “${esc(q)}” — ${hits.length} items across your toolkit.` : "Type to search skills, prompts, workflows, tools + references."}</p></div>`;
    if (!qq) return `<div class="page">${head}</div>`;
    if (!hits.length) return `<div class="page">${head}<div class="empty"><h3>Nothing found</h3><p>Nothing in your toolkit matches “${esc(q)}”. Try a broader term, or add something new.</p><button class="btn primary" data-add>+ Add to Toolkit</button></div></div>`;
    const groups = KIND_ORDER.map(k => {
      const g = hits.filter(i => i.kind === k);
      if (!g.length) return "";
      return `<div class="section"><h2>${KIND[k].plural}</h2><div class="list">${g.map(listRow).join("")}</div></div>`;
    }).join("");
    return `<div class="page">${head}${groups}</div>`;
  }

  /* ---------- Item detail (drawer) ---------- */
  // Skills count as "enabled" once they're active in at least one project.
  const isEnabled = i => i.kind === "skill" && Array.isArray(i.enabled_in) && i.enabled_in.length > 0;
  const splitBest = s => String(s || "").split(/[;·,]/).map(t => t.trim()).filter(Boolean);
  function resolveRel(n) {
    return byTitle[n] || byId[n] || byId["skill:" + n] || byId["reference:" + n] || byId["workflow:" + n] || byId["tool:" + n] || null;
  }
  function relChip(n, withKind) {
    const it = resolveRel(n);
    const label = it ? it.title : n;
    const kb = (withKind && it) ? `<span class="relk kind" data-k="${it.kind}"><span class="g">${KIND[it.kind].glyph}</span></span>` : "";
    return it ? `<a class="relchip" href="#/item/${encodeURIComponent(it.id)}">${kb}${esc(label)}</a>` : `<span class="relchip disabled">${esc(label)}</span>`;
  }
  function relGroup(label, names, opts) {
    if (!names || !names.length) return "";
    const o = opts || {};
    const note = o.note ? `<span class="rel-note">${esc(o.note)}</span>` : "";
    return `<div class="field relgroup"><h4>${label}${note}</h4><div class="rellist">${names.map(n => relChip(n, o.withKind)).join("")}</div></div>`;
  }
  function availInGroup(i) {
    const inn = i.installed_in || [];
    if (!inn.length) return "";
    return `<div class="field relgroup"><h4>Available in</h4><div class="rellist">${inn.map(p => `<span class="relchip plat"><span class="rlogo">${platLogo(p)}</span>${esc(p)}</span>`).join("")}</div></div>`;
  }
  function bestForField(i) {
    const parts = splitBest(i.best_use);
    if (!parts.length) return "";
    return `<div class="field"><h4>Best for</h4><div class="chips bestfor">${parts.map(p => `<span class="chip xs">${esc(p)}</span>`).join("")}</div></div>`;
  }
  // Reusable Availability list across destinations (installed ✓ or Push).
  function availabilityPanel(i) {
    const inn = i.installed_in || [];
    const rows = DESTINATIONS.map(p => {
      const on = inn.includes(p);
      return `<div class="instrow"><span class="idot ${on ? "on" : ""}">${platLogo(p)}</span><span class="ip-name">${esc(p)}</span><span class="ip-status ${on ? "on" : ""}">${on ? "Installed" : "Not installed"}</span>${on ? `<span class="ip-check" aria-hidden="true">✓</span>` : `<button class="btn sm" data-action="push-item" data-id="${esc(i.id)}" data-plat="${esc(p)}">Push</button>`}</div>`;
    }).join("");
    return `<div class="field"><h4>Availability</h4><div class="instlist">${rows}</div></div>`;
  }
  function overviewPane(i) {
    const desc = i.description || "";
    const summ = i.summary || "";
    const whatBlock = (desc && desc !== summ) ? `<div class="field"><h4>What it does</h4><p>${esc(desc)}</p></div>` : "";
    const useWhen = i.best_use ? `<div class="field"><h4>Use when</h4><p>${esc(i.best_use)}</p></div>` : "";
    return bestForField(i) + whatBlock + useWhen + availabilityPanel(i);
  }
  // Render an argument hint, highlighting placeholder tokens (<...> [...] {...}).
  function renderArgHint(hint) {
    const parts = String(hint).split(/(\s+)/).map(tok => {
      if (/^[<\[{].*[>\]}]$/.test(tok.trim()) && tok.trim()) return `<span class="vartoken">${esc(tok)}</span>`;
      return esc(tok);
    });
    return `<div class="varline">${parts.join("")}</div>`;
  }
  function pathLink(i, label) {
    return `<a class="pathlink" href="${esc(pathOf(i))}" target="_blank" rel="noopener noreferrer">${esc(label)} ↗</a>`;
  }
  function howtoPane(i) {
    const section = (label, body) => `<div class="field"><h4>${label}</h4>${body}</div>`;
    if (i.kind === "workflow") {
      return section("Step sequence", `<div class="steps">${workflowStepsInner(i)}</div>`);
    }
    if (i.kind === "prompt") {
      const inv = i.command ? codeSnippet("/" + i.command, "Invocation") : `<p class="muted">Model-invoked (no slash command)</p>`;
      const vars = i.argument_hint ? section("Variables", renderArgHint(i.argument_hint)) : "";
      const what = i.description ? section("What it does", `<p>${esc(i.description)}</p>`) : "";
      return section("Invocation", inv) + vars + what + section("Full prompt", `<div class="pathrow">${codeSnippet(pathOf(i), "Path")}${pathLink(i, "View full prompt")}</div>`);
    }
    if (i.kind === "tool") {
      const what = i.description ? section("What it does", `<p>${esc(i.description)}</p>`) : "";
      const usedBy = relGroup("Used by", i.used_by, { withKind: true });
      return what + usedBy + section("Capabilities", `<p class="muted empty-note">No capability metadata yet.</p>`);
    }
    if (i.kind === "reference") {
      const what = i.description ? section("What it does", `<p>${esc(i.description)}</p>`) : "";
      const useWhen = i.best_use ? section("Use when", `<p>${esc(i.best_use)}</p>`) : "";
      const related = ITEMS.filter(x => x.category === i.category && x.id !== i.id).slice(0, 5).map(x => x.title);
      return what + useWhen + relGroup("Related", related, { withKind: true, note: "Same domain" });
    }
    // skill (default)
    const inv = i.command ? codeSnippet("/" + i.command, "Invocation") : `<p class="muted">Model-invoked (no slash command)</p>`;
    const vars = i.argument_hint ? section("Variables", renderArgHint(i.argument_hint)) : "";
    const preview = i.description || i.summary || "";
    const instrBody = preview
      ? `<p class="instr-preview">${esc(preview)}</p><div class="pathrow">${codeSnippet(pathOf(i), "Path")}${pathLink(i, "View full instructions")}</div>`
      : `<div class="pathrow">${codeSnippet(pathOf(i), "Path")}${pathLink(i, "View full instructions")}</div>`;
    return section("Invocation", inv) + vars + section("Instructions", instrBody) + section("Usage examples", `<p class="muted empty-note">No usage examples yet.</p>`);
  }
  function relationshipsPane(i) {
    const worksWith = ITEMS.filter(x => x.category === i.category && x.id !== i.id).slice(0, 5).map(x => x.title);
    const groups = [
      relGroup("Used by", i.used_by, { withKind: true }),
      relGroup("Works with", worksWith, { withKind: true, note: "Related by domain" }),
      relGroup("Depends on", i.depends_on, { withKind: true }),
      relGroup("References", i.references, { withKind: true }),
      availInGroup(i),
    ].filter(Boolean);
    if (!groups.length) return `<div class="rel-empty"><p>No relationships recorded yet.</p></div>`;
    const mapCta = `<div class="rel-mapcta"><button class="btn sm" disabled title="Coming soon">View relationship map →</button></div>`;
    return groups.join("") + mapCta;
  }
  function sourcePane(i) {
    const label = (i.source && i.source.label) || "this repo";
    const looksRepo = /github\.com|gitlab\.com|bitbucket\.org|^https?:\/\//i.test(label);
    const originLink = looksRepo ? ` <a class="pathlink" href="${esc(/^https?:/i.test(label) ? label : "https://" + label)}" target="_blank" rel="noopener noreferrer">Open repository ↗</a>` : "";
    const origin = `<div class="field"><h4>Origin</h4><p>${esc(label)}${originLink}</p></div>`;
    const localPath = `<div class="field"><h4>Local path</h4>${codeSnippet(pathOf(i), "Path")}</div>`;
    const hist = [];
    if (i.date_updated) hist.push(`Updated ${esc(i.date_updated)}`);
    if (i.date_added) hist.push(`Added ${esc(i.date_added)}`);
    const history = hist.length ? `<div class="field"><h4>History</h4><p>${hist.join(" · ")}</p></div>` : "";
    const advRows = [
      `Id: <span class="mono">${esc(i.id)}</span>`,
      `Kind: ${esc(i.kind)}`,
      `Domain: ${esc(catLabel(i.category))}`,
      i.status ? `Status: ${esc(i.status)}` : "",
      i.command ? `Invocation: <span class="mono">/${esc(i.command)}</span>` : "",
    ].filter(Boolean).map(r => `<p>${r}</p>`).join("");
    const advanced = `<details class="advanced"><summary>Advanced · technical details</summary><div class="adv-body">${advRows}</div></details>`;
    return origin + localPath + history + advanced;
  }
  function openItem(id) {
    const i = byId[id]; if (!i) { location.hash = "#/library"; return; }
    const dr = document.getElementById("drawer");
    const enabled = isEnabled(i);
    const enableCtrl = enabled
      ? `<span class="enabled-state" title="Active in ${esc((i.enabled_in || []).join(", "))}">Enabled ✓</span>`
      : `<button class="btn primary" data-action="enable-item" data-id="${esc(i.id)}">${i.kind === "skill" ? "Enable" : "Use"}</button>`;
    const metaParts = [];
    if (enabled) metaParts.push("Enabled");
    if (i.date_updated) metaParts.push("Updated " + i.date_updated);
    const metaLine = metaParts.length ? `<div class="dmeta">${esc(metaParts.join(" · "))}</div>` : "";
    dr.innerHTML = `
      <div class="dhead">
        <div class="crumb">Library / ${KIND[i.kind].plural} / ${esc(i.title)}</div>
        ${kindTag(i.kind)}
        <h2>${esc(i.title)}</h2>
        <p class="muted">${esc(i.summary || i.description)}</p>
        ${metaLine}
        <div class="dactions">
          <div class="dactions-l">
            ${enableCtrl}
            <button class="btn" data-action="edit-item" data-id="${esc(i.id)}">Edit</button>
            <div class="overflow">
              <button class="btn iconbtn" id="dmore" aria-haspopup="true" aria-expanded="false" aria-label="More actions">•••</button>
              <div class="ovmenu" id="ovmenu" hidden>
                <button data-action="rename-item" data-id="${esc(i.id)}">Rename</button>
                <button data-action="duplicate-item" data-id="${esc(i.id)}">Duplicate</button>
                <button data-action="export-item" data-id="${esc(i.id)}">Export</button>
                <button class="danger" data-action="delete-item" data-id="${esc(i.id)}">Delete</button>
              </div>
            </div>
          </div>
          <button class="iconx" id="drclose" aria-label="Close" title="Close"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
        </div>
      </div>
      <div class="dtabs">
        <button data-dt="ov" class="active">Overview</button>
        <button data-dt="howto">How to Use</button>
        <button data-dt="rel">Relationships</button>
        <button data-dt="src">Source</button>
      </div>
      <div class="dbody" id="dbody"></div>`;
    dr.setAttribute("aria-hidden", "false");
    dr.classList.add("show"); document.getElementById("scrim").classList.add("show");
    const panes = { ov: overviewPane, howto: howtoPane, rel: relationshipsPane, src: sourcePane };
    const wireActions = () => dr.querySelectorAll(".dbody [data-action]").forEach(x => x.onclick = (e) => { e.stopPropagation(); handleAction(x.dataset.action, x.dataset); });
    const showPane = key => { document.getElementById("dbody").innerHTML = panes[key](i); wireActions(); };
    dr.querySelectorAll("[data-dt]").forEach(b => b.onclick = () => {
      dr.querySelectorAll("[data-dt]").forEach(x => x.classList.remove("active")); b.classList.add("active");
      showPane(b.dataset.dt);
    });
    showPane("ov");
    // Overflow menu (Rename / Duplicate / Export / Delete)
    const more = dr.querySelector("#dmore"), menu = dr.querySelector("#ovmenu");
    const closeMenu = () => { menu.hidden = true; more.setAttribute("aria-expanded", "false"); };
    more.onclick = (e) => { e.stopPropagation(); const open = menu.hidden; menu.hidden = !open; more.setAttribute("aria-expanded", String(open)); };
    menu.querySelectorAll("[data-action]").forEach(x => x.onclick = (e) => { e.stopPropagation(); closeMenu(); handleAction(x.dataset.action, x.dataset); });
    dr.addEventListener("click", e => { if (!e.target.closest(".overflow")) closeMenu(); });
    document.getElementById("drclose").onclick = () => history.length > 1 ? history.back() : (location.hash = "#/library");
    // Header actions (Enable/Use, Edit) live outside .dbody.
    dr.querySelectorAll(".dactions-l > [data-action]").forEach(b => b.onclick = (e) => { e.stopPropagation(); handleAction(b.dataset.action, b.dataset); });
  }
  function pathOf(i) {
    if (i.kind === "skill") return `skills/${i.name}/SKILL.md`;
    if (i.kind === "prompt") return `prompts/commands/${i.name}.md`;
    if (i.kind === "workflow") return `workflows/${i.name}/WORKFLOW.md`;
    if (i.kind === "reference") return `references/${i.name}.md`;
    return `tools/${i.name}/`;
  }
  function workflowStepsInner(w) {
    return (w.steps || []).map((s, idx) => {
      const uses = (s.uses || []).map(n => { const it = byTitle[byTitleKey(n)] || byId["skill:" + n]; return `<a class="tag" href="#/item/${encodeURIComponent(it ? it.id : "skill:" + n)}">${esc(it ? it.title : n)}</a>`; }).join("");
      return `${idx ? '<div class="stepconn"></div>' : ""}<div class="step"><div class="sn"><span class="num">${idx + 1}</span><strong>${esc(s.name)}</strong></div>${uses ? `<div class="uses">${uses}</div>` : ""}</div>`;
    }).join("");
  }
  function byTitleKey(name) { const it = byId["skill:" + name]; return it ? it.title : name; }

  /* ---------- Discover / Projects / Integrations / Inbox / Activity / Health / Settings ---------- */
  function viewDiscover() {
    const colls = (D.collections || []).slice(0, 12).map(c => `<button class="chip" data-nav="library/all"${tipAttr(c.name)}>${esc(catLabel(c.name))}<span class="c">${c.count}</span></button>`).join("");
    return `<div class="page">
      <div class="page-head"><h1>Discover</h1><p>What you could add. External discovery isn't wired up yet — this is the architecture. Hover a domain for what it covers.</p></div>
      <label class="topsearch" style="max-width:none"><span>⌕</span><input placeholder="Search skills, prompts, workflows + tools to add…"/></label>
      <div class="section"><h2>Browse by domain</h2><div class="chips">${colls}</div></div>
      <div class="section"><h2>From sources</h2><div class="list">
        <div class="row" data-add><span class="kind" data-k="tool"><span class="g">⚙</span></span><span><div class="nm">GitHub</div><div class="sub">Install a repo by URL — inspected + routed automatically</div></span><span class="sub">source</span><span class="btn sm">Add</span></div>
        <div class="row"><span class="kind"><span class="g">◎</span></span><span><div class="nm">Community catalogs</div><div class="sub">Curated catalogs (coming soon)</div></span><span class="sub">registry</span><span class="sub faint">soon</span></div>
      </div></div>
      <div class="empty" style="margin-top:24px"><h3>Discovery feed coming soon</h3><p>When registries are connected, recommended skills, prompts and workflows will appear here.</p><button class="btn primary" data-add>+ Add from GitHub</button></div>
    </div>`;
  }
  function viewProjects() {
    const rows = (D.projects || []).map(p => `<div class="row" data-nav="project/${encodeURIComponent(p.id)}"><span class="kind"><span class="g">▦</span></span>
      <span><div class="nm">${esc(p.name)}</div><div class="sub">${p.skills.length} skills · ${p.workflows.length} workflows · ${p.references.length} references</div></span>
      <span class="sub">${Object.values(p.integrations).filter(v => v === "synced").length}/${Object.keys(p.integrations).length} agents synced</span><span class="btn sm">Open</span></div>`).join("");
    return `<div class="page"><div class="page-head"><h1>Projects</h1><p>What parts of your toolkit are active in each project, and which agents they're synced to.</p></div><div class="list">${rows}</div></div>`;
  }
  function viewProject(id) {
    const p = (D.projects || []).find(x => x.id === id); if (!p) return viewProjects();
    const caps = p.skills.map(n => { const it = byId["skill:" + n]; return `<div class="row" ${it ? `data-item="skill:${esc(n)}"` : ""}><span class="kind" data-k="skill"><span class="g">◇</span></span><span><div class="nm">${esc(it ? it.title : n)}</div></span><span class="sub">enabled</span><button class="btn sm" data-action="disable-cap" data-proj="${esc(p.id)}" data-name="${esc(n)}">Disable</button></div>`; }).join("");
    const wfs = p.workflows.map(n => `<span class="tag">${esc(n)}</span>`).join(" ");
    const refs = p.references.map(n => `<span class="tag">${esc(n)}</span>`).join(" ");
    const integ = Object.entries(p.integrations).map(([k, v]) => `<div class="row"><span class="kind"><span class="g">⇄</span></span><span><div class="nm">${esc(k)}</div><div class="sub">${v === "synced" ? "This project's items are live in " + esc(k) : "Not synced to " + esc(k) + " yet"}</div></span><span class="sub">${v === "synced" ? "Synced" : "Not synced"}</span><button class="btn sm ${v === "synced" ? "" : "primary"}" data-action="sync-project-integration" data-proj="${esc(p.id)}" data-name="${esc(k)}">${v === "synced" ? "Re-sync" : "Sync"}</button></div>`).join("");
    return `<div class="page">
      <div class="crumb" style="margin-bottom:8px"><a href="#/projects">Projects</a> / ${esc(p.name)}</div>
      <div class="page-head"><h1>${esc(p.name)}</h1><p>${p.skills.length} skills · ${p.workflows.length} workflows · ${p.references.length} references enabled.</p></div>
      <div class="section"><h2>Enabled capabilities</h2><div class="list">${caps}</div><div style="margin-top:10px"><button class="btn" data-nav="library/skill">+ Enable from toolkit</button></div></div>
      <div class="section"><h2>Workflows</h2><div class="chips">${wfs || '<span class="faint">None yet</span>'}</div></div>
      <div class="section"><h2>References</h2><div class="chips">${refs || '<span class="faint">None yet</span>'}</div></div>
      <div class="section"><div class="sec-head"><h2>Sync to agents</h2></div><p class="muted" style="margin:-4px 0 12px">Your toolkit is the source of truth. Sync copies this project's enabled items into each agent (Cursor, Claude Code, Codex).</p><div class="list">${integ}</div></div>
    </div>`;
  }
  function viewIntegrations() {
    const c = D.counts || {};
    const byKind = KIND_ORDER.filter(k => c[k]).map(k => `${c[k]} ${KIND[k].plural.toLowerCase()}`).join(" · ");
    const total = ITEMS.length;
    const rows = (D.integrations || []).map(x => {
      const doc = TOOL_DOCS[x.name];
      const openLink = (x.status === "connected" && doc) ? `<a class="btn sm openin" href="${esc(doc.url)}" target="_blank" rel="noopener noreferrer" title="${esc(doc.label)} (opens in a new tab)">${esc(doc.label)} ↗</a>` : "";
      return `<div class="row"><span class="kind integ-logo"><span class="g">${platLogo(x.name)}</span></span>
      <span><div class="nm">${esc(x.name)}</div><div class="sub">${x.status === "connected" ? `${total} items synced — ${byKind} · last synced ${esc(x.last_synced)}` : "Not configured"}</div></span>
      <span class="sub">${x.status === "connected" ? "Connected" : "—"}</span>
      <span class="integ-actions">${openLink}${x.status === "connected" ? `<button class="btn sm" data-action="sync-integration" data-name="${esc(x.name)}">Sync</button>` : `<button class="btn sm primary" data-action="setup-integration" data-name="${esc(x.name)}">Set up</button>`}</span></div>`;
    }).join("");
    return `<div class="page"><div class="page-head"><h1>Integrations</h1><p>Use your toolkit across AI coding environments. The toolkit is the source of truth; each agent syncs from it — skills, prompts, workflows, tools + references.</p></div><div class="list">${rows}</div></div>`;
  }
  function viewInbox() {
    const all = D.inbox || [];
    const head = `<div class="page-head"><h1>Inbox</h1><p>Items the router couldn't confidently classify. Review to file one into your toolkit, or delete what you don't need — this is a staging area, not a second toolkit.</p></div>`;
    if (!all.length) return `<div class="page">${head}<div class="empty"><h3>Inbox is clear</h3><p>Nothing waiting. New unclassified items will show up here.</p></div></div>`;
    const unread = all.filter(x => !x.read), read = all.filter(x => x.read);
    const rowU = x => `<div class="row inbox-row"><span class="kind" data-k="${x.detected}"><span class="g">${(KIND[x.detected] || KIND.reference).glyph}</span></span>
      <span><div class="nm">${esc(x.name)}</div><div class="sub">Suggested: ${esc(x.detected)} · ${esc(catLabel(x.category))} — ${esc(x.reason)}</div></span>
      <span class="inbox-actions"><button class="btn sm primary" data-action="review-inbox" data-name="${esc(x.name)}">Review</button><button class="btn sm" data-action="mark-read" data-name="${esc(x.name)}">Mark read</button><button class="btn sm danger" data-action="delete-inbox" data-name="${esc(x.name)}">Delete</button></span></div>`;
    const rowR = x => `<div class="row inbox-row read"><span class="kind" data-k="${x.filedAs || x.detected}"><span class="g">${(KIND[x.filedAs || x.detected] || KIND.reference).glyph}</span></span>
      <span><div class="nm">${esc(x.name)}</div><div class="sub">${x.filedAs ? "Filed as " + esc(x.filedAs) : "Marked read"}${x.category ? " · " + esc(catLabel(x.category)) : ""}</div></span>
      <span class="inbox-actions"><button class="btn sm" data-action="unread-inbox" data-name="${esc(x.name)}">Mark unread</button><button class="btn sm danger" data-action="delete-inbox" data-name="${esc(x.name)}">Delete</button></span></div>`;
    return `<div class="page">${head}
      <div class="section"><div class="sec-head"><h2>Unread${unread.length ? " · " + unread.length : ""}</h2></div>${unread.length ? `<div class="list">${unread.map(rowU).join("")}</div>` : `<p class="faint">Nothing unread — inbox zero.</p>`}</div>
      ${read.length ? `<div class="section"><div class="sec-head"><h2>Read · ${read.length}</h2></div><div class="list">${read.map(rowR).join("")}</div></div>` : ""}
    </div>`;
  }
  function viewActivity() {
    const rows = (D.activity || []).map(a => `<div class="a"><strong>${esc(a.action)}</strong><span>${esc(a.target)}</span><span class="w">${esc(a.when)}</span></div>`).join("");
    return `<div class="page"><div class="page-head"><h1>Activity</h1><p>What changed across your toolkit.</p></div><div class="actlist">${rows}</div></div>`;
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
    return `<div class="page"><div class="page-head"><h1>Settings</h1><p>Where your toolkit lives, what's in it, and what's changed.</p></div>
      <div class="section"><h2>Global toolkit</h2><div class="list">
        <div class="row settings-row"><span class="kind"><span class="g">⌂</span></span><span><div class="nm">Toolkit home</div><div class="sub mono">${esc(toolkitHome)}</div><div class="sub">The folder that holds every skill, prompt, workflow, tool + reference. Agents sync from here.</div></span><span></span><button class="btn sm" data-action="change-home">Change</button></div>
        <div class="row settings-row"><span class="kind"><span class="g">▤</span></span><span><div class="nm">Contents</div><div class="sub">${esc(plusify(totals) || "empty")}</div></span><span></span><button class="btn sm" data-nav="library">Open toolkit</button></div>
      </div></div>
      <div class="section"><div class="sec-head"><h2>Activity</h2><button class="btn sm" data-nav="activity">View all</button></div><div class="actlist">${recent}</div></div>
    </div>`;
  }

  /* ---------- Overlays: Add / Create / Palette ---------- */
  function overlay(html) { document.getElementById("overlay").innerHTML = html; }
  function closeOverlay() { document.getElementById("overlay").innerHTML = ""; }
  function closeDrawerOnly() { const dr = document.getElementById("drawer"); if (dr) { dr.classList.remove("show"); dr.setAttribute("aria-hidden", "true"); } document.getElementById("scrim") && document.getElementById("scrim").classList.remove("show"); }
  function closeAll() { closeDrawerOnly(); closeOverlay(); closeNotif(); }

  const add = { step: "source", src: "github" };
  function openAdd() { add.step = "source"; renderAdd(); }
  function renderAdd() {
    let body = "", foot = "", title = "Add to Toolkit";
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
    ["Search Toolkit", () => location.hash = "#/library"],
    ["Add to Toolkit", openAdd], ["Install from GitHub", () => { openAdd(); add.step = "input"; renderAdd(); }],
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
      case "mark-read": return setInboxRead(ds.name, true);
      case "unread-inbox": return setInboxRead(ds.name, false);
      case "delete-inbox": return deleteInbox(ds.name);
      case "change-home": return openChangeHome();
      case "copy-snippet": return copySnippet(ds.target, ds.label);
      case "duplicate-item": return toast("Duplicate isn't wired up in this prototype");
      case "export-item": return toast("Export isn't wired up in this prototype");
      case "delete-item": return toast("Delete isn't wired up in this prototype");
      default: return undefined;
    }
  }

  function setInboxRead(name, read) {
    const it = (D.inbox || []).find(x => x.name === name); if (!it) return;
    it.read = read; if (!read) it.filedAs = undefined;
    persistInbox(name, { read: read, filedAs: read ? it.filedAs : undefined });
    addActivity(read ? "Marked read" : "Marked unread", name);
    toast(name + (read ? " marked read" : " moved back to unread")); rebuildAll();
  }
  function deleteInbox(name) {
    D.inbox = (D.inbox || []).filter(x => x.name !== name);
    persistInbox(name, { deleted: true });
    addActivity("Deleted", name + " (inbox)"); toast("Deleted " + name); rebuildAll();
  }
  function openChangeHome() {
    overlay(`<div class="modal"><div class="box"><div class="mhead"><h2>Toolkit home</h2><button class="btn sm" data-x>×</button></div><div class="mbody">
      <div class="field"><h4>Folder</h4><input class="input" id="th-home" value="${esc(toolkitHome)}" autocomplete="off" /></div>
      <p class="muted">Where the toolkit is stored on disk. Skills, prompts, workflows, tools + references live here, and every agent syncs from it.</p>
    </div><div class="mfoot"><button class="btn" data-x>Cancel</button><button class="btn primary" id="th-save">Save</button></div></div></div>`);
    const ov = document.getElementById("overlay");
    ov.querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
    ov.querySelector("#th-save").onclick = () => {
      const v = ov.querySelector("#th-home").value.trim(); if (!v) { closeOverlay(); return; }
      toolkitHome = v; try { localStorage.setItem("ai-toolkit-home", v); } catch (e) {}
      addActivity("Changed", "Toolkit home → " + v); closeOverlay(); toast("Toolkit home set"); rerenderView();
    };
    ov.querySelector("#th-home").focus();
  }

  function pushItem(id, plat) {
    const it = byId[id]; if (!it) return;
    it.installed_in = it.installed_in || [];
    if (!it.installed_in.includes(plat)) it.installed_in.push(plat);
    persistItemInstall(id, plat);
    addActivity("Installed", it.title + " → " + plat);
    toast("Pushed " + it.title + " to " + plat);
    openItem(id); // refresh drawer so status + push buttons update
  }

  /* Rename an item — propagates the new name across every in-memory reference,
     then re-syncs the environments it's installed in. (Persisting to disk /
     the real tool integrations needs a backend; this is the front-end path.) */
  // Core in-memory rename + reference propagation. Returns { oldTitle, newId }
  // or null when nothing changed. Kept side-effect-free (no UI/persist/history)
  // so it can also run at boot when re-applying persisted renames.
  function applyRename(id, newTitle) {
    const it = byId[id]; if (!it) return null;
    newTitle = String(newTitle).trim(); if (!newTitle || newTitle === it.title) return null;
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
    return { oldTitle, newId };
  }
  function renameItem(id, newTitle) {
    const before = byId[id]; if (!before) return;
    const t = String(newTitle).trim();
    if (!t || t === before.title) { if (t === before.title) location.hash = "#/item/" + encodeURIComponent(id); return; }
    const res = applyRename(id, t); if (!res) return;
    persistRename(id, t);
    addActivity("Renamed", res.oldTitle + " → " + t);
    const it = byId[res.newId];
    const where = (it && it.installed_in || []).join(", ");
    toast("Renamed to “" + t + "”" + (where ? " · re-synced " + where : ""));
    location.hash = "#/item/" + encodeURIComponent(res.newId); // reopen drawer at new id
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
      persistIntegration(name, { status: it.status, last_synced: it.last_synced, count: it.count });
      toast(name + " synced");
      if (currentRoute().startsWith("integrations")) rerenderView();
    }, 700);
  }
  function setupIntegration(name) {
    const it = (D.integrations || []).find(x => x.name === name); if (!it) return;
    it.status = "connected"; it.count = ITEMS.filter(x => x.kind === "skill").length; it.last_synced = "just now";
    persistIntegration(name, { status: "connected", count: it.count, last_synced: it.last_synced });
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
    p.integrations[name] = "synced"; persistProjectIntegration(projId, name, "synced"); addActivity("Synced", name + " · " + p.name); toast(name + " synced"); rerenderView();
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
      <p class="muted">Suggested: <strong>${esc(it.detected)}</strong> · ${esc(catLabel(it.category))} — ${esc(it.reason)}</p>
      <div class="field"><h4>File as</h4><div class="chips" id="ib-kinds">${opts}</div></div>
      <div class="field"><h4>Source</h4><p class="mono">${esc(it.source)}</p></div>
    </div><div class="mfoot"><button class="btn danger" data-del>Delete</button><div style="display:flex;gap:8px"><button class="btn" data-x>Cancel</button><button class="btn primary" data-file>File + mark read</button></div></div></div></div>`);
    const ov = document.getElementById("overlay");
    let chosen = it.detected;
    ov.querySelectorAll("#ib-kinds .chip").forEach(c => c.onclick = () => { ov.querySelectorAll("#ib-kinds .chip").forEach(x => x.classList.remove("active")); c.classList.add("active"); chosen = c.dataset.k; });
    ov.querySelectorAll("[data-x]").forEach(b => b.onclick = closeOverlay);
    ov.querySelector("[data-del]").onclick = () => { closeOverlay(); deleteInbox(name); };
    ov.querySelector("[data-file]").onclick = () => {
      it.read = true; it.filedAs = chosen;
      persistInbox(name, { read: true, filedAs: chosen });
      addActivity("Filed", name + " → " + chosen); closeOverlay(); toast("Filed " + name + " as " + chosen + " · re-synced"); rebuildAll();
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

  /* ---------- Tooltips (delegated; the tip element lives on <body>) ---------- */
  function initTooltips() {
    let tip = document.getElementById("tip");
    if (!tip) { tip = document.createElement("div"); tip.id = "tip"; tip.className = "tip"; tip.setAttribute("role", "tooltip"); document.body.appendChild(tip); }
    const show = el => {
      const text = el.getAttribute("data-tip"); if (!text) return;
      tip.textContent = text;
      const r = el.getBoundingClientRect();
      tip.style.left = Math.round(r.left + r.width / 2) + "px";
      tip.style.top = Math.round(r.bottom + 8) + "px";
      tip.classList.add("show");
    };
    const hide = () => tip.classList.remove("show");
    document.addEventListener("mouseover", e => { const el = e.target.closest("[data-tip]"); if (el) show(el); });
    document.addEventListener("mouseout", e => { const el = e.target.closest("[data-tip]"); if (el) hide(); });
    document.addEventListener("focusin", e => { const el = e.target.closest("[data-tip]"); if (el) show(el); });
    document.addEventListener("focusout", hide);
    window.addEventListener("scroll", hide, true);
  }

  /* ---------- Boot ---------- */
  window.addEventListener("keydown", e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") { e.preventDefault(); openPalette(); }
    else if (e.key === "Escape") closeAll();
  });
  window.addEventListener("hashchange", router);
  document.addEventListener("click", e => {
    if (!notifOpen) return;
    if (e.target.closest("#notif") || e.target.closest("#bell")) return;
    closeNotif();
  });

  (async function boot() {
    await loadLiveData(); // falls back to the bundled snapshot on failure
    applyPersistedState(); // re-apply persisted user mutations before first render
    shell();
    router();
    initTooltips();
  })();
})();
