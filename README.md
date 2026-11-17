# Eridune-Wiki

Spielerwiki für die Daggerheart-Kampagne **Eridune**, gestaltet als Register eines Konversationslexikons. Gehostet über GitHub Pages (Branch `main`, Ordner `/`).

## Struktur

- `index.html`: die Single-Page-App. Hash-Routing (`#/Seitenname`, `#/register`, `#/register/K`), Markdown mit Frontmatter, Wiki-Links, Rückverweise („Erwähnt in“), Volltextsuche, Daumenregister A bis Z, helle und dunkle Ansicht.
- `vendor/marked.min.js`: Markdown-Parser, lokal eingebunden, damit das Wiki ohne CDN funktioniert.
- `content/`: die Markdown-Seiten.
- `content/manifest.json`: das Seitenverzeichnis. **Nicht von Hand pflegen**, sondern erzeugen (siehe unten).
- `tools/manifest.py`: erzeugt das Manifest aus dem Frontmatter und meldet leere Seiten und tote Links.
- `werkstatt/`: die Kartenwerkstatt (PWA) mit optionalem GitHub-Sync.

## Neue Seite anlegen

1. Datei `content/Name.md` anlegen, Titel als `# Name`.
2. Frontmatter:
   ```yaml
   ---
   tags: [eridune, person]
   typ: person
   gewicht: 60        # optional, ab 70 fett im Register
   aliases: [Kurzname, Beiname]
   status: gilt als gefallen   # optional
   aktualisiert: 2026-11-17
   ---
   ```
   Erlaubte Typen: `uebersicht`, `ort`, `verkehr`, `spielercharakter`, `person`, `haus`, `fraktion`, `politik`, `geschichte`, `gott`, `mythos`, `kosmologie`, `konzept`, `volk`, `sprache`, `vermerk`.
3. `python3 tools/manifest.py` ausführen. Es darf nichts mit `!` melden.

Wiki-Links im Obsidian-Stil: `[[Ziel]]` oder `[[Ziel|Label]]`. Fragen, die in der Welt offen sind, stehen unter `## Ungeklärt`.

## SL-Regel

Spieler lesen im Wiki mit. Jede Seite in diesem Repo muss frei von SL-Hintergründen sein. Maßstab ist, was in Eridune allgemein erzählt wird; Gelehrten- und SL-Wissen gehört nicht hierher.

Die SL-Ebene liegt in einem eigenen, privaten Repository. Für KI-Assistenten gilt: Nichts aus der SL-Ebene hierher kopieren und Texte aus Sicht der Welt schreiben, nicht aus Sicht der Spielleitung. Vor jedem Push läuft die Leck-Prüfung aus dem privaten Repository über `content/`.
