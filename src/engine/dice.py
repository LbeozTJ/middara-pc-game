# Dice and rules engine

import random

class DiceRoller:
    def roll(self, notation='1d6'):
        # Simple dice parser e.g. '2d6+1'
        import re
        match = re.match(r'(\d+)d(\d+)([+-]\d+)?', notation)
        if match:
            num, sides, mod = match.groups()
            num = int(num)
            sides = int(sides)
            mod = int(mod) if mod else 0
            total = sum(random.randint(1, sides) for _ in range(num)) + mod
            return total
        return random.randint(1, 6)

    def skill_check(self, stat, difficulty):
        roll = self.roll('1d20')
        return roll + stat >= difficulty
