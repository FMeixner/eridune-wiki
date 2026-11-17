#!/usr/bin/env python3
"""Erzeugt content/manifest.json aus dem Frontmatter der Seiten und prüft Wiki-Links.

Aufruf (im Repo-Wurzelverzeichnis):  python3 tools/manifest.py
Jede Seite in content/ braucht im Frontmatter `typ:`; optional `gewicht:` (0–100,
steuert Reihenfolge und Startseite) und `aliases: [...]`. Der Titel ist die erste
Überschrift `# …`, sonst der Dateiname.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TYPEN = {"uebersicht", "ort", "verkehr", "spielercharakter", "person", "haus", "fraktion",
         "politik", "geschichte", "gott", "mythos", "kosmologie", "konzept", "volk",
         "sprache", "vermerk"}

def frontmatter(text):
    fm, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            for line in text[4:end].splitlines():
                m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
                if m:
                    fm[m.group(1)] = m.group(2).strip()
            body = text[end + 4:]
    al = fm.get("aliases", "")
    fm["aliases"] = [a.strip() for a in al.strip("[]").split(",") if a.strip()] if al else []
    return fm, body

seiten, probleme, namen = [], [], {}
for p in sorted(CONTENT.glob("*.md")):
    text = p.read_text(encoding="utf-8")
    fm, body = frontmatter(text)
    if not body.strip():
        probleme.append(f"leer: {p.stem}")
    typ = fm.get("typ", "")
    if typ not in TYPEN:
        probleme.append(f"typ fehlt/unbekannt in {p.stem}: {typ!r}")
    h1 = re.search(r"^#\s+(.+)$", body, flags=re.M)
    eintrag = {"path": p.stem, "title": h1.group(1).strip() if h1 else p.stem, "type": typ}
    if fm.get("gewicht"):
        eintrag["w"] = int(fm["gewicht"])
    if fm["aliases"]:
        eintrag["aliases"] = fm["aliases"]
    if fm.get("kurz"):
        eintrag["kurz"] = fm["kurz"]
    seiten.append(eintrag)
    for n in [p.stem] + fm["aliases"]:
        namen[n.lower()] = p.stem

for p in sorted(CONTENT.glob("*.md")):
    for ziel in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", p.read_text(encoding="utf-8")):
        if ziel.strip().lower() not in namen:
            probleme.append(f"toter Link in {p.stem}: [[{ziel}]]")

seiten.sort(key=lambda s: (s["path"] != "index", s["path"] != "Eridune", -s.get("w", 0), s["title"]))
manifest = {"coverage": f"{len(seiten)} Einträge", "pages": seiten}
(CONTENT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"manifest.json: {len(seiten)} Seiten")
for x in probleme:
    print("  !", x)
sys.exit(1 if probleme else 0)
