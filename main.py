import sys
import pygame
from src.engine.dice import DiceRoller
from src.engine.character import Character
from src.engine.rules_parser import load_rules

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Middara PC Game - Phase 1')

print('Middara PC Game starting - Phase 1 Complete')

rules = load_rules()
print('Loaded rules:', rules['game_modes'])

roller = DiceRoller()
print('Dice roll example (2d6):', roller.roll('2d6'))

char = Character('Rook the Warrior')
print(char)
char.level_up()

print('\nPhase 1 ready: Basic dice, character, rules loaded.')
print('Next: Expand to full combat and UI.')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()