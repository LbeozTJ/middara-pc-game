# Dice and rules engine for Middara

import random
import re

class DiceRoller:
    def roll(self, notation='1d6'):
        # Simple dice parser e.g. '2d6+1', supports Middara custom too
        match = re.match(r'(\d+)d(\d+)([+-]\d+)?', notation)
        if match:
            num, sides, mod = match.groups()
            num = int(num)
            sides = int(sides)
            mod = int(mod) if mod else 0
            total = sum(random.randint(1, sides) for _ in range(num)) + mod
            return total
        return random.randint(1, 6)

    def skill_check(self, stat, difficulty, advantage=False):
        # Middara skill checks often use d20 + stat vs difficulty
        roll = self.roll('1d20')
        if advantage:
            roll2 = self.roll('1d20')
            roll = max(roll, roll2)
        success = roll + stat >= difficulty
        return {'roll': roll, 'success': success, 'margin': roll + stat - difficulty}

    def attack_roll(self, attacker_stat, defender_defense, num_dice=1):
        # Simulate Middara attack with hit/miss, using symbols
        hits = 0
        damages = []
        for _ in range(num_dice):
            roll = self.roll('1d6')  # Assume d6 attack dice with symbols
            if roll >= 4:  # e.g. hit on 4+
                hits += 1
                damage = max(0, roll - 3)  # simple damage
                damages.append(damage)
        return {'hits': hits, 'damages': damages, 'symbols': ['HIT' if h > 0 else 'MISS' for h in [1]*hits + [0]*(num_dice-hits)] }

    def convinction_check(self, cv_pool):
        # Special for Conviction resource
        return random.randint(1, 6) <= cv_pool  # e.g. success on low roll or something
