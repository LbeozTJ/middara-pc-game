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
7. **Debug & Flagging UI** – Toggleable debug overlay (F12 hotkey) showing live game state, rule engine traces, entity properties, dice history, and terrain/line-of-sight visuals. "Flag Issue" button captures current context (JSON snapshot + placeholder screenshot), auto-generates a structured debug report in `/data/debug_logs/`, and offers one-click template for Grok-assisted troubleshooting or rule discrepancy review. All flags remain 100% local.

## Tech Stack
- **Language**: Python 3.11+
- **Game Framework**: Pygame (primary) – lightweight and easy to run
- **Alternative**: Godot 4 + GDScript (if visual editor preferred)
- **Data**: JSON for rules/characters/saves; PDF rulebook parsed on load
- **Dependencies**: See `requirements.txt` (includes pygame, pillow for debug screenshots)

## How to Run (Local)
```bash
git clone https://github.com/LbeozTJ/middara-pc-game.git
cd middara-pc-game
pip install -r requirements.txt
python main.py
```
Press **F12** in-game to toggle Debug & Flagging panel. Use "Flag Issue" anytime to log state for later review.

## Project Structure
```
middara-pc-game/
├── README.md
├── requirements.txt
├── main.py
├── /rules/          # Parsed rule sections (auto-generated)
├── /src/
│   ├── engine/      # Rules, dice, state machine
│   ├── ui/          # Interface, rendering, debug_panel.py
│   ├── combat/      # Battle logic (Phase 2 stub tested)
│   ├── campaign/    # Story and progression (stub)
│   └── utils/       # Logging, screenshot helpers
├── /debug/          # Auto-generated debug reports & logs
├── /assets/         # Placeholders (replace with your scans or free assets)
├── /data/           # Saved games + debug_logs/
└── .gitignore
```

## Development Workflow with Grok
1. Keep Google Drive connector active (rulebook PDF must stay in connected folder).
2. GitHub connector authorized.
3. Tell Grok: “Add [feature]” or “Fix [issue]” or “Implement Phase X”.
4. Grok reads rules → writes code → commits to this repo.
5. Pull changes, test, and give feedback.
6. Use the in-game **Flag Issue** button to instantly capture context and share relevant debug JSON with Grok for faster fixes.

## Priority Roadmap
- **Phase 1**: Rule parser + basic dice/character engine + **Debug & Flagging UI** (COMPLETE - fully tested and verified May 2026)
- **Phase 2**: Full combat resolution with reactions + advanced rule enforcement (STUB IMPLEMENTED & TESTED - dice/character integrated; full LOS/terrain/reactions next)
- Phase 3: Character creation screen + inventory + gear management (core Character class ready)
- Phase 4: Campaign map, exploration, and narrative choices (stub ready)
- Phase 5: Polish, audio placeholders, exportable character sheets, and expanded debug tools

## Testing Summary (May 10, 2026)
All phases tested via automated harness (press 'T' in-game):
- Phase 1: Rule loading, dice rolls (d6/d20/custom), skill/attack checks, full character lifecycle (level, equip/exhaust/flip, inventory, consumables) - ALL PASS
- Phase 2: Combat attack resolution with symbol output - PASS
- Higher phases: Stubs functional
No bugs found. Ready for full Phase 2 implementation on next request.

## Legal & Notes
- Strictly personal backup/implementation of my owned physical copy.
- All artwork/assets are placeholders until replaced by user-provided files.
- Debug & Flagging tools are for personal troubleshooting and rule clarification only; all reports and logs stay local.
- Feedback on rule ambiguities will be resolved by referencing the official PDF + in-game flag reports.

Last updated: May 10, 2026  
Built with Grok (xAI) + Connectors
