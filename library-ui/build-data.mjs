#!/usr/bin/env node
/* Render library-ui/data.js — the committed fallback snapshot.

   The app reads the real catalog live at runtime; this snapshot is only used
   when that fetch is unavailable (file://, offline, or a server rooted inside
   library-ui). It shares data-live.js so the snapshot can never drift from the
   live view. Regenerate: node library-ui/build-data.mjs */
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join, relative } from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const buildLibraryData = require("./data-live.js");

const here = dirname(fileURLToPath(import.meta.url));
const root = dirname(here);
const catalog = JSON.parse(readFileSync(join(root, "catalog", "skills-index.json"), "utf8"));
const data = buildLibraryData(catalog);

const out = join(here, "data.js");
writeFileSync(out, "window.LIBRARY_DATA = " + JSON.stringify(data) + ";\n", "utf8");
console.log(`Wrote ${relative(root, out)} — ${data.items.length} items (${JSON.stringify(data.counts)})`);
