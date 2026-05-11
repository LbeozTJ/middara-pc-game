import sys
import pygame
import json
import os
from src.engine.dice import DiceRoller
from src.engine.character import Character
from src.engine.rules_parser import load_rules

# Initialize Pygame
pygame.init()
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Middara PC Game - Character Placemat & Equipped Cards (Phase 2 UI)')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (200, 200, 200)
GOLD = (218, 165, 32)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
RED = (178, 34, 34)
CARD_BG = (245, 245, 220)  # Beige for cards
SLOT_BG = (60, 60, 80)

# Fonts
font_large = pygame.font.SysFont('arial', 28, bold=True)
font_medium = pygame.font.SysFont('arial', 20)
font_small = pygame.font.SysFont('arial', 16)
font_tiny = pygame.font.SysFont('arial', 14)

# Load rules and sample items
rules = load_rules()
sample_items = rules.get('sample_items', {})

# Create character with placemat support
char = Character('Rook the Warrior', 'Warrior')

# Demo: Pre-equip a couple items to show
char.equip_item('weapon', sample_items['iron_sword'])
char.equip_item('core', sample_items['guardian_core'])

# UI State
selected_slot = None
message_log = ["Welcome to Middara PC Game Placemat! Equip cards to see tactics update live."]
clock = pygame.time.Clock()

def draw_text(surface, text, x, y, font=font_small, color=WHITE, center=False):
    """Helper to draw text."""
    rendered = font.render(text, True, color)
    if center:
        rect = rendered.get_rect(center=(x, y))
        surface.blit(rendered, rect)
    else:
        surface.blit(rendered, (x, y))

def draw_card(surface, x, y, width, height, item_data, is_selected=False):
    """Draw a digital item card with image placeholder, type, abilities, exhaust/flip state."""
    # Card border and bg
    border_color = GOLD if is_selected else LIGHT_GRAY
    pygame.draw.rect(surface, border_color, (x-3, y-3, width+6, height+6), 0, 8)
    pygame.draw.rect(surface, CARD_BG, (x, y, width, height), 0, 8)
    pygame.draw.rect(surface, DARK_GRAY, (x, y, width, height), 2, 8)

    if item_data['name'] == 'Empty Slot':
        # Empty slot placeholder
        draw_text(surface, item_data['type'], x + width//2, y + 30, font_medium, DARK_GRAY, center=True)
        draw_text(surface, "[Click to Equip]", x + width//2, y + 60, font_tiny, DARK_GRAY, center=True)
        return

    # Load real artwork from Drive-synced assets if available, else placeholder
    img_loaded = False
    if 'image' in item_data and os.path.exists(item_data['image']):
        try:
            img = pygame.image.load(item_data['image'])
            img = pygame.transform.scale(img, (width - 20, 90))
            surface.blit(img, (x + 10, y + 10))
            img_loaded = True
        except Exception as e:
            pass  # fallback to placeholder on error

    if not img_loaded:
        # Digital image placeholder (colored rect representing the card art)
        img_rect = pygame.Rect(x + 10, y + 10, width - 20, 90)
        # Assign color based on type for visual distinction
        type_colors = {'Weapon': (139, 69, 19), 'Core': (70, 130, 180), 'Relic': (148, 0, 211), 'Accessory': (50, 205, 50)}
        img_color = type_colors.get(item_data['type'], LIGHT_GRAY)
        pygame.draw.rect(surface, img_color, img_rect, 0, 5)
        pygame.draw.rect(surface, BLACK, img_rect, 1, 5)
        # Fake "image" text or icon
        draw_text(surface, f"[{item_data['type']} Art]", x + width//2, y + 55, font_tiny, WHITE, center=True)
        # Note: Real artwork loaded from Google Drive /assets/ sync (see project notes)

    # Card name
    draw_text(surface, item_data['name'], x + width//2, y + 110, font_medium, BLACK, center=True)

    # Type badge
    type_y = y + 135
    pygame.draw.rect(surface, BLUE, (x + 10, type_y, width - 20, 22), 0, 4)
    draw_text(surface, item_data['type'].upper(), x + width//2, type_y + 11, font_small, WHITE, center=True)

    # Abilities (wrapped)
    ability_y = type_y + 30
    for i, ability in enumerate(item_data['abilities'][:3]):  # Limit to 3 lines
        draw_text(surface, f"• {ability}", x + 12, ability_y + i*18, font_tiny, DARK_GRAY)

    # Status indicators (exhaust, flip)
    status_y = y + height - 45
    if item_data['exhausted']:
        pygame.draw.rect(surface, RED, (x + 8, status_y, width - 16, 20), 0, 3)
        draw_text(surface, "EXHAUSTED", x + width//2, status_y + 10, font_tiny, WHITE, center=True)
    else:
        pygame.draw.rect(surface, GREEN, (x + 8, status_y, width - 16, 20), 0, 3)
        draw_text(surface, "READY", x + width//2, status_y + 10, font_tiny, WHITE, center=True)

    if item_data['flipped']:
        draw_text(surface, "FLIPPED", x + width - 50, y + 15, font_tiny, RED)

    # Bonuses summary
    if item_data.get('bonuses'):
        bonus_text = " ".join([f"+{v} {k[:3].upper()}" for k, v in item_data['bonuses'].items()])
        draw_text(surface, bonus_text, x + width//2, status_y - 18, font_tiny, GOLD, center=True)

def draw_placemat(surface, char):
    """Draw the character placemat with equipped cards."""
    placemat_x, placemat_y = 420, 80
    slot_width, slot_height = 170, 220
    gap = 20

    # Placemat background (like a physical mat)
    pygame.draw.rect(surface, (139, 119, 101), (placemat_x - 15, placemat_y - 15, 4*slot_width + 3*gap + 30, slot_height + 80), 0, 15)
    pygame.draw.rect(surface, (101, 67, 33), (placemat_x - 10, placemat_y - 10, 4*slot_width + 3*gap + 20, slot_height + 70), 0, 12)
    draw_text(surface, "CHARACTER PLACEMAT - EQUIPPED CARDS", placemat_x + 2*slot_width + gap, placemat_y - 35, font_large, GOLD, center=True)

    slots = ['weapon', 'core', 'relic', 'accessory']
    display_data = char.get_placemat_display()

    for i, slot in enumerate(slots):
        x = placemat_x + i * (slot_width + gap)
        y = placemat_y
        item = display_data[slot]
        is_selected = (selected_slot == slot)
        draw_card(surface, x, y, slot_width, slot_height, item, is_selected)

        # Slot label
        draw_text(surface, slot.upper(), x + slot_width//2, y + slot_height + 15, font_small, WHITE, center=True)

    # Instructions
    draw_text(surface, "Click a card slot to select • Press E to equip sample • X to exhaust • F to flip • R to refresh all", 
              placemat_x + 2*slot_width + gap, placemat_y + slot_height + 50, font_tiny, LIGHT_GRAY, center=True)

def draw_character_panel(surface, char):
    """Left panel: Character sheet with stats and tactics."""
    panel_x, panel_y = 30, 80
    panel_w = 360

    # Background
    pygame.draw.rect(surface, DARK_GRAY, (panel_x, panel_y, panel_w, 650), 0, 10)
    pygame.draw.rect(surface, GOLD, (panel_x, panel_y, panel_w, 650), 3, 10)

    # Header
    draw_text(surface, f"{char.name}", panel_x + panel_w//2, panel_y + 25, font_large, GOLD, center=True)
    draw_text(surface, f"Level {char.level} {char.hero_class}", panel_x + panel_w//2, panel_y + 55, font_medium, WHITE, center=True)

    # Base Stats
    y = panel_y + 100
    draw_text(surface, "BASE STATS", panel_x + 20, y, font_medium, GOLD)
    y += 30
    for stat, val in char.stats.items():
        draw_text(surface, f"{stat.capitalize()}: {val}", panel_x + 30, y, font_small, WHITE)
        y += 22

    # Resources
    y += 10
    draw_text(surface, "RESOURCES", panel_x + 20, y, font_medium, GOLD)
    y += 30
    draw_text(surface, f"Stamina (SP): {char.stamina}/{char.max_stamina}", panel_x + 30, y, font_small, WHITE)
    y += 22
    draw_text(surface, f"Health (HP): {char.health}/{char.max_health}", panel_x + 30, y, font_small, WHITE)
    y += 22
    draw_text(surface, f"Conviction (CV): {char.conviction}", panel_x + 30, y, font_small, WHITE)

    # Tactics Modifiers (from equipped cards)
    y += 40
    draw_text(surface, "TACTICS SUMMARY (Live from Placemat)", panel_x + 20, y, font_medium, GOLD)
    y += 30
    effective = char.get_tactics_summary()
    for stat, val in effective.items():
        mod = char.tactics_modifiers.get(stat, 0)
        color = GREEN if mod > 0 else (RED if mod < 0 else WHITE)
        draw_text(surface, f"{stat.capitalize()}: {val} {'(+' + str(mod) + ')' if mod != 0 else ''}", panel_x + 30, y, font_small, color)
        y += 20

    # Equipped count
    y += 20
    equipped_count = sum(1 for v in char.equipped.values() if v)
    draw_text(surface, f"Cards Equipped: {equipped_count}/4", panel_x + 20, y, font_small, GOLD)

    # Message log
    y = 620
    draw_text(surface, "LOG:", panel_x + 20, y, font_tiny, GOLD)
    for i, msg in enumerate(message_log[-4:]):
        draw_text(surface, msg[:45] + "..." if len(msg) > 45 else msg, panel_x + 20, y + 20 + i*18, font_tiny, LIGHT_GRAY)

def draw_controls(surface):
    """Bottom control bar."""
    bar_y = screen_height - 80
    pygame.draw.rect(surface, (20, 20, 30), (0, bar_y, screen_width, 80))
    pygame.draw.rect(surface, GOLD, (0, bar_y, screen_width, 3))

    controls = [
        "1-4: Select slot 1=Weapon, 2=Core, 3=Relic, 4=Accessory",
        "E: Equip random sample item to selected slot",
        "X: Toggle Exhaust on selected",
        "F: Toggle Flip on selected",
        "R: Refresh all cards (new round)",
        "U: Unequip selected slot",
        "Q: Quit"
    ]
    x_start = 50
    for i, ctrl in enumerate(controls):
        draw_text(surface, ctrl, x_start + (i % 4) * 280, bar_y + 15 + (i // 4) * 30, font_tiny, WHITE)

def main():
    global selected_slot, message_log
    running = True
    slots = ['weapon', 'core', 'relic', 'accessory']

    while running:
        screen.fill((30, 30, 45))  # Dark background

        # Draw UI panels
        draw_character_panel(screen, char)
        draw_placemat(screen, char)
        draw_controls(screen)

        # Title bar
        pygame.draw.rect(screen, DARK_GRAY, (0, 0, screen_width, 60))
        draw_text(screen, "MIDDARA PC GAME - PERSONAL DIGITAL EDITION", screen_width//2, 20, font_large, GOLD, center=True)
        draw_text(screen, "Phase 2: Character Placemat with Equipped Item Cards | Exhaust/Flip Mechanics | Live Tactics Integration", 
                  screen_width//2, 45, font_tiny, LIGHT_GRAY, center=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_1:
                    selected_slot = 'weapon'
                    message_log.append(f"Selected Weapon slot")
                elif event.key == pygame.K_2:
                    selected_slot = 'core'
                    message_log.append(f"Selected Core slot")
                elif event.key == pygame.K_3:
                    selected_slot = 'relic'
                    message_log.append(f"Selected Relic slot")
                elif event.key == pygame.K_4:
                    selected_slot = 'accessory'
                    message_log.append(f"Selected Accessory slot")
                elif event.key == pygame.K_e and selected_slot:
                    # Equip a random sample item
                    import random
                    item_key = random.choice(list(sample_items.keys()))
                    item = sample_items[item_key].copy()
                    item['exhausted'] = False
                    item['flipped'] = False
                    if char.equip_item(selected_slot, item):
                        message_log.append(f"Equipped {item['name']} to {selected_slot}!")
                    else:
                        message_log.append("Equip failed.")
                elif event.key == pygame.K_x and selected_slot:
                    if char.toggle_exhaust(selected_slot):
                        message_log.append(f"Toggled exhaust on {selected_slot}")
                elif event.key == pygame.K_f and selected_slot:
                    if char.toggle_flip(selected_slot):
                        message_log.append(f"Toggled flip on {selected_slot}")
                elif event.key == pygame.K_r:
                    char.refresh_all()
                    message_log.append("All cards refreshed! Ready for next encounter.")
                elif event.key == pygame.K_u and selected_slot:
                    if char.unequip_item(selected_slot):
                        message_log.append(f"Unequipped from {selected_slot}")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    # Check if clicked on a slot
                    placemat_x, placemat_y = 420, 80
                    slot_width, slot_height = 170, 220
                    gap = 20
                    mx, my = event.pos
                    for i, slot in enumerate(slots):
                        x = placemat_x + i * (slot_width + gap)
                        y = placemat_y
                        if x <= mx <= x + slot_width and y <= my <= y + slot_height:
                            selected_slot = slot
                            message_log.append(f"Selected {slot} slot via click")
                            break

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    print("Middara PC Game - Phase 2: Placemat & Equipped Cards Demo Starting...")
    print("Features implemented: Digital card images (placeholder), type/abilities display,")
    print("exhaust/flip mechanics, live tactics integration (stats update when equipped/exhausted).")
    print("Press 1-4 or click slots, E to equip, X/F to toggle states, R to refresh.")
    main()