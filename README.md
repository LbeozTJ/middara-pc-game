# Middara PC Game - Personal Digital Edition
**100% Personal Use Only** — For my private offline play. No distribution, no sharing of code/assets.

## Project Goal
A complete, offline desktop application that faithfully implements Middara (Unintentional Malum + expansions) rules for single-player or hot-seat multiplayer on PC. Built as a tactical dungeon-crawler with full campaign tracking.

## Core Features (Phased Delivery)
1. **Rule Engine** – Accurate parsing and enforcement of all core + advanced rules from the official rulebook.
2. **Character Creation & Management** – Full hero sheets, leveling, traits, gear.
3. **Tactical Combat** – Hex/grid battles with reactions, terrain, line-of-sight, dice rolls, status effects.
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
├── /rules/ # Parsed rule sections (auto-generated)
├── /src/
│ ├── engine/ # Rules, dice, state machine
│ ├── ui/ # Interface and rendering
│ ├── combat/ # Battle logic
│ ├── campaign/ # Story and progression
│ └── utils/
├── /assets/ # Placeholders (replace with your scans or free assets)
├── /data/ # Saved games
└── .gitignore
```

## Development Workflow with Grok
1. Keep Google Drive connector active (rulebook PDF must stay in connected folder).
2. GitHub connector authorized.
3. Tell Grok: “Add [feature]” or “Fix [issue]” or “Implement Phase X”.
4. Grok reads rules → writes code → commits to this repo.
5. Pull changes, test, and give feedback.

## Priority Roadmap
- Phase 1: Rule parser + basic dice/character engine
- Phase 2: Full combat resolution with reactions
- Phase 3: Character creation screen + inventory
- Phase 4: Campaign map and narrative
- Phase 5: Polish, audio placeholders, exportable character sheets

## Legal & Notes
- Strictly personal backup/implementation of my owned physical copy.
- All artwork/assets are placeholders until replaced by user-provided files.
- Feedback on rule ambiguities will be resolved by referencing the official PDF.

Last updated: May 2026
Built with Grok (xAI) + Connectors