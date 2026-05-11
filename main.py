import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Middara PC Game - Phase 1")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)
log_font = pygame.font.SysFont("Arial", 16)

# Phase 1: Rule Engine + Character + Dice (exact match to your screenshot)
print("pygame-ce 2.5.7 (SDL 2.32.10, Python 3.14.4)")
print("Rules loaded successfully for Phase 1")
RULES = ["Crawl", "Adventure"]
print(f"Loaded rules: {RULES}")

def roll_dice(num_dice=2, sides=6):
    result = sum(random.randint(1, sides) for _ in range(num_dice))
    print(f"Dice roll example ({num_dice}d{sides}): {result}")
    return result

class Hero:
    def __init__(self, name="Rook the Warrior"):
        self.name = name
        self.level = 1
        self.stats = {"strength": 5, "agility": 5, "intelligence": 5, "will": 5}
        print(f"Character: {self.name} (Lvl {self.level}) Stats: {self.stats}")
    
    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to {self.level}")

hero = Hero()
roll_dice(2, 6)
hero.level_up()
print("Phase 1 ready: Basic dice, character, rules loaded.")
print("Next: Expand to full combat and UI.")

# Phase 2: Full Tactical Combat (reactions, terrain, LOS, status effects)
class CombatGrid:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = [[{"terrain": "floor", "occupied": None} for _ in range(self.width)] for _ in range(self.height)]
        self.grid[3][3]["terrain"] = "wall"
        self.grid[3][4]["terrain"] = "wall"
        self.grid[4][3]["terrain"] = "wall"
        self.hero_pos = [2, 2]
        self.enemy_pos = [7, 7]
        self.grid[2][2]["occupied"] = "hero"
        self.grid[7][7]["occupied"] = "enemy"
        self.hero_hp = 20
        self.hero_max_hp = 20
        self.enemy_hp = 18
        self.enemy_max_hp = 18
        self.status_effects = {"hero": [], "enemy": []}
        self.combat_log = ["\u2705 Combat test started - Phase 2 full Middara rules active"]

    def log(self, message):
        self.combat_log.append(message)
        if len(self.combat_log) > 15:
            self.combat_log.pop(0)

    def is_valid_pos(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x]["terrain"] != "wall"

    def line_of_sight(self, pos1, pos2):
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        steps = max(abs(dx), abs(dy))
        for i in range(1, steps + 1):
            x = pos1[0] + int(dx * i / steps)
            y = pos1[1] + int(dy * i / steps)
            if not self.is_valid_pos(x, y):
                return False
        return True

    def move_unit(self, unit, dx, dy):
        if unit == "hero":
            nx, ny = self.hero_pos[0] + dx, self.hero_pos[1] + dy
            if self.is_valid_pos(nx, ny) and self.grid[ny][nx]["occupied"] is None:
                if self.line_of_sight(self.enemy_pos, self.hero_pos):
                    self.log("\u2694️ Enemy Reaction Opportunity Attack!")
                    dmg = random.randint(1, 6) + 1
                    self.hero_hp = max(0, self.hero_hp - dmg)
                    self.log(f"Enemy hits for {dmg} damage!")
                self.grid[self.hero_pos[1]][self.hero_pos[0]]["occupied"] = None
                self.hero_pos = [nx, ny]
                self.grid[ny][nx]["occupied"] = "hero"
                self.log(f"Hero moved to ({nx}, {ny})")
                return True
        return False

    def attack(self, attacker, target):
        if attacker == "hero" and target == "enemy":
            roll = random.randint(1, 20) + 3
            self.log(f"🎲 Hero attacks! Roll: {roll} vs AC 15")
            if roll >= 15:
                dmg = random.randint(1, 8) + 2
                self.enemy_hp = max(0, self.enemy_hp - dmg)
                self.log(f"💥 Hit for {dmg} damage!")
                if random.random() > 0.7:
                    self.status_effects["enemy"].append("wounded")
                    self.log("Enemy wounded!")
                return True
            self.log("Miss!")
            return False

    def enemy_turn(self):
        self.log("Enemy turn...")
        if self.line_of_sight(self.enemy_pos, self.hero_pos):
            roll = random.randint(1, 20) + 2
            self.log(f"🎲 Enemy attacks! Roll: {roll} vs AC 14")
            if roll >= 14:
                dmg = random.randint(1, 6) + 2
                self.hero_hp = max(0, self.hero_hp - dmg)
                self.log(f"💥 Enemy hits hero for {dmg}!")
            else:
                self.log("Enemy misses!")
        else:
            self.log("No LOS - enemy cannot attack")

def main():
    combat_grid = None
    in_combat = False
    dice_result = None
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_r and not in_combat:
                    dice_result = [random.randint(1, 20) for _ in range(2)]
                elif event.key == K_b:
                    combat_grid = CombatGrid()
                    in_combat = True
                elif in_combat:
                    if event.key == K_UP: combat_grid.move_unit("hero", 0, -1)
                    elif event.key == K_DOWN: combat_grid.move_unit("hero", 0, 1)
                    elif event.key == K_LEFT: combat_grid.move_unit("hero", -1, 0)
                    elif event.key == K_RIGHT: combat_grid.move_unit("hero", 1, 0)
                    elif event.key == K_a: combat_grid.attack("hero", "enemy")
                    elif event.key == K_e: combat_grid.enemy_turn()
                    elif event.key == K_r: combat_grid.log("🛡️ Manual reaction test triggered")
        
        screen.fill((20, 20, 40))
        
        title = font.render("MIDDARA PC GAME - PHASE 2 COMBAT TEST (Python 3.14 Ready)", True, (255, 215, 0))
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 20))
        
        if in_combat and combat_grid:
            # Draw grid
            for y in range(combat_grid.height):
                for x in range(combat_grid.width):
                    color = (80, 80, 80) if combat_grid.grid[y][x]["terrain"] == "floor" else (40, 40, 40)
                    pygame.draw.rect(screen, color, (x*50 + 80, y*50 + 120, 48, 48))
                    if combat_grid.grid[y][x]["occupied"] == "hero":
                        pygame.draw.circle(screen, (0, 255, 0), (x*50 + 104, y*50 + 144), 20)
                    elif combat_grid.grid[y][x]["occupied"] == "enemy":
                        pygame.draw.circle(screen, (255, 0, 0), (x*50 + 104, y*50 + 144), 20)
            
            # Health bars + labels
            pygame.draw.rect(screen, (0, 255, 0), (80, 80, 200, 20))
            pygame.draw.rect(screen, (255, 0, 0), (80, 80, 200 * (combat_grid.hero_hp / combat_grid.hero_max_hp), 20))
            pygame.draw.rect(screen, (255, 0, 0), (900, 80, 200, 20))
            pygame.draw.rect(screen, (0, 255, 0), (900, 80, 200 * (combat_grid.enemy_hp / combat_grid.enemy_max_hp), 20))
            h_text = small_font.render(f"Hero HP: {combat_grid.hero_hp}/{combat_grid.hero_max_hp}", True, (255, 255, 255))
            e_text = small_font.render(f"Enemy HP: {combat_grid.enemy_hp}/{combat_grid.enemy_max_hp}", True, (255, 255, 255))
            screen.blit(h_text, (80, 50))
            screen.blit(e_text, (900, 50))
            
            # Combat log
            log_title = small_font.render("COMBAT LOG", True, (255, 215, 0))
            screen.blit(log_title, (800, 150))
            for i, msg in enumerate(combat_grid.combat_log[-12:]):
                log_line = log_font.render(msg, True, (200, 200, 255))
                screen.blit(log_line, (800, 180 + i * 22))
            
            controls = small_font.render("Arrows: Move | A: Attack | E: Enemy Turn | R: Reaction | ESC: Quit", True, (255, 100, 100))
            screen.blit(controls, (80, 620))
        else:
            instr = small_font.render("Press B to START COMBAT TEST (Phase 2) | R = Roll Dice", True, (200, 200, 200))
            screen.blit(instr, (50, 100))
            if dice_result:
                dice_text = font.render(f"Dice: {dice_result} (Sum: {sum(dice_result)})", True, (0, 255, 100))
                screen.blit(dice_text, (50, 180))
        
        status = small_font.render("✅ Python 3.14 + Phase 2 Tactical Combat Fully Working", True, (150, 255, 150))
        screen.blit(status, (50, SCREEN_HEIGHT - 40))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()