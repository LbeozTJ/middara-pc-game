#!/usr/bin/env python3
"""
Middara PC Game - Personal Digital Edition
Phase 1: Rule Engine + Debug & Flagging UI (stub)
"""

import pygame
import sys
from src.ui.debug_panel import DebugPanel  # Placeholder for debug UI

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Middara PC Game - Personal Edition")
    
    debug_panel = DebugPanel()
    debug_active = False
    
    clock = pygame.time.Clock()
    running = True
    
    print("Middara PC Game started. Press F12 to toggle Debug & Flagging panel.")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F12:
                    debug_active = not debug_active
                    print(f"Debug mode: {'ON' if debug_active else 'OFF'}")
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill((30, 30, 40))
        
        # Placeholder game content
        font = pygame.font.SysFont(None, 48)
        text = font.render("Middara - Tactical Dungeon Crawler", True, (200, 200, 220))
        screen.blit(text, (320, 300))
        
        if debug_active:
            debug_panel.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
