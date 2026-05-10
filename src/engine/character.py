# Character management

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.stats = {'strength': 5, 'agility': 5, 'intelligence': 5, 'will': 5}
        self.stamina = 10
        self.health = 20
        self.inventory = []
        self.disciplines = []

    def level_up(self):
        self.level += 1
        # Point buy for Middara style
        print(f'{self.name} leveled up to {self.level}')

    def __str__(self):
        return f'Character: {self.name} (Lvl {self.level}) Stats: {self.stats}'
