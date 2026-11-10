# Eridune-Wiki

Single-Page-Wiki für die Daggerheart-Kampagne **Eridune** — gehostet via GitHub Pages (Branch `main`, Ordner `/ (root)`).

## Struktur

- `index.html` — die SPA: Hash-Routing (`#/seitenname`), rendert Markdown + Frontmatter, automatische Backlinks, Volltextsuche, Link-Wolken.
- `content/` — die Markdown-Seiten.
- `content/manifest.json` — das Seitenverzeichnis. **Pflicht:** Jede neue Seite braucht einen Eintrag hier, sonst erscheint sie nicht in Navigation, Suche und Backlinks.
- `werkstatt/` — die Kartenwerkstatt v4 (PWA): Marker mit Wiki-Links, JSON-Import/Export, optionaler GitHub-Sync (Repo `eridune-wiki`, Branch `main`, Pfad `werkstatt/werkstatt-daten.json`).
- `.nojekyll` — verhindert die Jekyll-Verarbeitung auf Pages.

## Seiten-Pflichten

- Frontmatter: `tags`, `aliases` (Liste), `status`, `kurz`, `aktualisiert`.
- Wiki-Links im Obsidian-Stil: `[[Ziel]]` oder `[[Ziel|Label]]`.
- Manifest-Typen: `uebersicht`, `ort`, `person`, `spielercharakter`, `fraktion`, `konzept`, `verkehr`, `mythus`, `volk`, `sprache`, `kreatur`, `artefakt`, `tier`, `vorlage`, `sl_werkzeug`, `timeline`, `fortschritt`.

## SL-Regel

Spieler lesen im Wiki mit. Jede Seite in diesem Repo muss deshalb frei von SL-Hintergründen sein; SL-interne Dateien werden **nicht** committet und leben nur lokal.
