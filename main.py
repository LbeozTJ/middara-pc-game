import sys
import pygame
from src.engine.dice import DiceRoller
from src.engine.character import Character

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Middara PC Game - Phase 1')

print('Middara PC Game starting...')

# Basic test
roller = DiceRoller()
print('Dice roll example:', roller.roll('2d6'))

char = Character('Test Hero')
print(char)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()