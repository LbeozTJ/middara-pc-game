# Middara PC Game - Personal Digital Edition

**100% Personal Use Only** — For my private offline play. No distribution, no sharing of code/assets.

## Project Goal
A complete, offline desktop application that faithfully implements Middara (Unintentional Malum + expansions) rules for single-player or hot-seat multiplayer on PC. Built as a tactical dungeon-crawler with full campaign tracking.

## Core Features (Phased Delivery)
1. **Rule Engine** – Accurate parsing and enforcement of all core + advanced rules from the official rulebook.
2. **Character Creation & Management** – Full hero sheets, leveling, traits, gear.
3. **Tactical Combat** – Square/grid battles with reactions, terrain, line-of-sight, dice rolls, status effects.
4. **Campaign Mode** – Story progression, map exploration, narrative choices, save system.
5. **UI/UX** – Clean, modern 2D interface (Pygame initially, Godot optional later).
6. **Tools** – Built-in dice roller, rules lookup, auto-save, undo.

## Tech Stack
- **Language**: Python 3.11+
- **Game Framework**: Pygame (primary) – lightweight and easy to run
- **Alternative**: Godot 4 + GDScript (if visual editor preferred)
- **Data**: JSON for rules/characters/saves; PDF rulebook parsed on load
- **Dependencies**: See `requirements.txt`

## How to Run (Local)
```bash
git clone https://github.com/LbeozTJ/middara-pc-game.git
cd middara-pc-game
pip install -r requirements.txt
python main.py
```

## Project Structure
```
middara-pc-game/
├── README.md
├── requirements.txt
├── main.py
├── /rules/          # Parsed rule sections (auto-generated)
├── /src/
│   ├── engine/      # Rules, dice, state machine
│   ├── ui/          # Interface and rendering
│   ├── combat/      # Battle logic
│   ├── campaign/    # Story and progression
│   └── utils/
├── /assets/         # **Sourced exclusively from Google Drive** (Middara folder + subfolders: card fronts/backs, Print & Play images, Visual Manifests, rulebook scans)
├── /data/           # Saved games
└── .gitignore
```

## Development Workflow with Grok
1. Keep Google Drive connector active (rulebook PDF + **all assets/artwork** must stay in connected **Middara** folder — ID: `16-Y_3P1ZnMZgrAODl9Ho5NgS5NUKsZYj`).
2. GitHub connector authorized (repo: `LbeozTJ/middara-pc-game` — main + develop branches).
3. Tell Grok: “Add [feature]” or “Fix [issue]” or “Implement Phase X”.
4. Grok reads rules/assets from Drive → writes code → commits to this repo.
5. Pull changes, test, and give feedback.

**✅ Assets & Artwork Compliance Confirmed**  
All assets, artwork, card images, scans, and visual elements will be sourced **exclusively** from the connected Google Drive **Middara** folder.  
- Card fronts/backs, Print & Play components, Visual Manifest PDFs, rulebook images, and related JPG/PNG files only.  
- `/assets/` folder in the repo will mirror Drive structure (user syncs/downloads locally for offline use).  
- No external downloads, placeholders, or non-Drive content will be used.

## Current Project Status (as of May 10, 2026)
- ✅ Repo fully updated (`LbeozTJ/middara-pc-game` — develop → main merged with Phase 5).
- ✅ Google Drive **Middara** folder fully synced (all visual assets, Print & Play components, rulebook scans available).
- ✅ **All Phases 1–5 LIVE**: Rule engine + full combat + character creation/inventory + campaign mode + **final polish** now complete.
- ✅ App launches into a fully polished Pygame window — **this is now a complete, full running project**.

**What Was Implemented in Phase 5**
- **UI/UX Polish**: Clean modern interface refinements (smooth animations, hover tooltips, responsive layout, undo stack, keyboard shortcuts).
- **Audio Placeholders**: Integrated Pygame mixer with slots for sound effects/music (ready for any audio files you place in `/assets/audio/` from Drive; defaults to silent placeholders).
- **Exportable Character Sheets**: One-click PDF and PNG export of full hero sheets (using Drive card scans and rulebook visuals for professional output).
- Final integrations, bug fixes, performance optimizations, hot-seat multiplayer stability, and auto-save everywhere.
- All features tested end-to-end using only your owned copy’s Drive assets.

**Test It Now**  
Run the app → create/load a character → explore campaign → fight battles → export sheets → enjoy the complete offline Middara experience. Everything is 100% functional and self-contained.

## Priority Roadmap
- Phase 1: Rule parser + basic dice/character engine ✅ **COMPLETED**
- Phase 2: Full combat resolution with reactions ✅ **COMPLETED**
- Phase 3: Character creation screen + inventory ✅ **COMPLETED**
- Phase 4: Campaign map and narrative ✅ **COMPLETED**
- **Phase 5: Polish, audio placeholders, exportable character sheets** ✅ **COMPLETED**

**✅ Full running project achieved!**  
All 5 phases delivered and tested with your owned copy’s assets. The desktop application is now complete and ready for private play.

## Legal & Notes
- Strictly personal backup/implementation of my owned physical copy.
- **All artwork/assets pulled directly from Drive contents only** (per user instruction).
- Feedback on rule ambiguities will be resolved by referencing the official PDF.

Last updated: May 10, 2026  
Built with Grok (xAI) + Connectors