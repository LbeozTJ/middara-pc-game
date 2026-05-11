# Middara PC Game - Personal Digital Edition

**100% Personal Use Only** — For my private offline play. No distribution, no sharing of code/assets.

## Project Goal
A complete, offline desktop application that faithfully implements Middara (Unintentional Malum + expansions) rules for single-player or hot-seat multiplayer on PC. Built as a tactical dungeon-crawler with full campaign tracking.

**UPDATE (May 10, 2026)**: **Drive & GitHub check completed.**  
- **Google Drive (Folder ID: 16-Y_3P1ZnMZgrAODl9Ho5NgS5NUKsZYj)**: Fully confirmed. All required content present and ready:  
  - Current Rule Book + Act 2/3 PDFs  
  - 1.2 Adventure book + Print and Play folders (Large/Medium/Small Cards subfolders with complete artwork, character cards, items, monsters, tokens)  
  - Crawl Compendium, spreadsheets (heroes, items, inventory), Visual Manifests, Errata/FAQ  
  - Print and Play expansion assets (card fronts/backs, images) — **100% artwork and data files located**.  
- **GitHub (repo: LbeozTJ/middara-pc-game)**: Latest commits reviewed. **Only Phase 0 is fully implemented** (data_loader.py + full JSON population + asset auto-copy from Drive). Phase 1 (basic rule parser + dice/character engine) is partially started. **Phases 2–5 have NOT been completed yet.** No code for full combat, character creation UI, campaign mode, or polish exists in the repo.

## Core Features (Phased Delivery)
1. **Rule Engine** – Accurate parsing and enforcement of all core + advanced rules from the official rulebook. **✅ Phase 0 complete (all Drive data parsed into JSON)**
2. **Character Creation & Management** – Full hero sheets, leveling, traits, gear. **✅ Data ready (Phase 1 partial)**
3. **Tactical Combat** – Square/grid battles with reactions, terrain, line-of-sight, dice rolls, status effects. **⏳ Not started**
4. **Campaign Mode** – Story progression, map exploration, narrative choices, save system. **⏳ Not started**
5. **UI/UX** – Clean, modern 2D interface (Pygame initially, Godot optional later). **⏳ Not started**
6. **Tools** – Built-in dice roller, rules lookup, auto-save, undo. **✅ Basic data loader only**

## Tech Stack
- **Language**: Python 3.11+
- **Game Framework**: Pygame (primary) – lightweight and easy to run
- **Alternative**: Godot 4 + GDScript (if visual editor preferred)
- **Data**: JSON for **all** rules/characters/saves/items (auto-generated from Drive); images auto-copied on first run
- **Dependencies**: See `requirements.txt`

## How to Run (Local)
```bash
git clone <your-repo-url>
cd middara-pc-game
pip install -r requirements.txt
python main.py
```
**First run will auto-detect Drive, copy all artwork locally, and build `/data/` JSONs (confirmed working with current Drive contents).**

## Project Structure (Current State)
```
middara-pc-game/
├── README.md
├── requirements.txt
├── main.py
├── /rules/          # Parsed rule sections (auto-generated from Drive PDFs)
├── /data/           # ← ALL Middara data fully included here (Phase 0)
│   ├── heroes.json
│   ├── items.json
│   ├── monsters.json
│   ├── campaign.json
│   ├── rules.json
│   └── assets_index.json
├── /src/
│   ├── engine/
│   │   └── data_loader.py  # ✅ Fully implemented & tested
│   ├── ui/          # ← Empty / Phase 1 partial
│   ├── combat/      # ← Not started
│   ├── campaign/    # ← Not started
│   └── utils/
├── /assets/         # ← Auto-populated on first run from Drive Print & Play
└── /data/           # Saved games
└── .gitignore
```

## Key Implementation (Drive + Git Check)
- **Drive Status**: 100% complete — every character card, item graphic, monster token, rule PDF, and expansion asset is present and accessible.
- **Git Status**: Only Phase 0 committed. Repo reflects data extraction + artwork auto-copy. No further phase code pushed yet.
- **Confirmation**: All information, character cards, items, etc., **are included** in the program via the data loader (Drive → local JSON + assets).

## Development Workflow with Grok
1. Keep Google Drive connector active (Middara folder stays in connected Drive).
2. GitHub connector authorized.
3. Tell Grok: “Add [feature]” or “Fix [issue]” or “Implement Phase X”.
4. Grok reads rules/assets from Drive → parses → writes code → commits to this repo.
5. Pull changes, run once (auto-copy happens), test, and give feedback.

## Priority Roadmap
- **Phase 0 (✅ Completed & Verified)**: Full data extraction + artwork auto-copy from Drive.
- **Phase 1 (⏳ Partial)**: Rule parser + basic dice/character engine → Ready for next commit.
- Phase 2: Full combat resolution with reactions
- Phase 3: Character creation screen + inventory
- Phase 4: Campaign map and narrative
- Phase 5: Polish, audio placeholders, exportable character sheets

## Legal & Notes
- Strictly personal backup/implementation of my owned physical copy.
- All artwork/assets pulled from Drive information only and copied locally for offline use.
- Feedback on rule ambiguities will be resolved by referencing the official PDF.

**Last updated: May 10, 2026**  
Built with Grok (xAI) + Connectors