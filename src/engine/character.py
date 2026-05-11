# Character management for Middara

class Character:
    def __init__(self, name, hero_class='Warrior'):
        self.name = name
        self.level = 1
        self.hero_class = hero_class
        self.base_stats = {'strength': 5, 'agility': 5, 'intelligence': 5, 'will': 5}
        self.stats = self.base_stats.copy()  # current effective, will be recalculated
        self.stamina = 10  # SP
        self.health = 20  # HP
        self.conviction = 3  # CV
        self.inventory = []  # For consumables, extra weapons etc.
        self.disciplines = []
        self.tags = []
        self.conditions = []
        self.max_stamina = 10
        self.max_health = 20
        self.symbols = {
            "tags": ["DOUBLE", "UNIQUE", "CURSED", "LEGENDARY"],
            "conditions": ["Poisoned", "Burning", "Stunned", "Bleeding"],
            "icons": ["SP", "CV", "HP", "AP", "DMG", "HIT", "MISS", "CRIT"]
        }  # Populated as described in core_rules.json symbols section
        self.weapons = []  # Populated list of available weapons
        self.consumables = []  # Inventory of consumables with proper use mechanics
        self.equippables = ['weapon', 'core', 'relic', 'accessory']  # As described
        # Equipment placemat - slots for equipped cards
        self.equipped = {
            'weapon': None,      # e.g. {'name': 'Iron Sword', 'type': 'Weapon', 'image': 'placeholder_sword.png', 'abilities': ['+1 Attack Die'], 'exhausted': False, 'flipped': False, 'bonuses': {'strength': 1}}
            'core': None,        # Core item type in Middara
            'relic': None,
            'accessory': None
        }
        self.tactics_modifiers = {}  # Dynamic stats from equipment for combat tactics

    def level_up(self):
        self.level += 1
        # Point buy for Middara style - add to stats
        self.stats['strength'] += 1
        print(f'{self.name} leveled up to {self.level}! Stats improved.')

    def spend_stamina(self, amount):
        if self.stamina >= amount:
            self.stamina -= amount
            return True
        return False  # Not enough SP

    def regain_stamina(self, amount):
        self.stamina = min(self.max_stamina, self.stamina + amount)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        if self.health == 0:
            print(f'{self.name} has fallen!')

    def apply_condition(self, condition):
        if condition in self.symbols['conditions']:
            self.conditions.append(condition)
            print(f'{self.name} is now {condition} (symbol from rules)')

    def add_to_inventory(self, item_data):
        """Add item (weapon, consumable etc) to inventory with proper mechanics."""
        self.inventory.append(item_data)
        if item_data.get('type') == 'Consumable':
            self.consumables.append(item_data.copy())
        elif item_data.get('type') == 'Weapon':
            self.weapons.append(item_data.copy())
        print(f"Added {item_data['name']} to inventory.")

    def use_consumable(self, item_name):
        """Use a consumable from inventory: applies effect and removes it (single use mechanic as described)."""
        for i, item in enumerate(self.consumables):
            if item['name'] == item_name:
                effect = item.get('effect', item.get('abilities', ['No effect'])[0])
                print(f"Using {item['name']}: {effect}")
                # Apply effect e.g. heal
                if 'heal' in effect.lower() or 'hp' in effect.lower():
                    heal = 5  # parse better in full
                    self.health = min(self.max_health, self.health + heal)
                    print(f"Healed {heal} HP. Current: {self.health}/{self.max_health}")
                elif 'stamina' in effect.lower() or 'sp' in effect.lower():
                    sp = 5
                    self.stamina = min(self.max_stamina, self.stamina + sp)
                    print(f"Restored {sp} SP. Current: {self.stamina}/{self.max_stamina}")
                # Remove from consumables and inventory
                self.consumables.pop(i)
                # Also remove from main inventory if present
                self.inventory = [inv for inv in self.inventory if inv.get('name') != item['name']]
                return True
        print(f"Consumable {item_name} not found or already used.")
        return False

    def __str__(self):
        equipped_summary = {slot: item['name'] if item else 'Empty' for slot, item in self.equipped.items()}
        return f'Character: {self.name} (Lvl {self.level}, {self.hero_class}) Stats: {self.stats} SP:{self.stamina}/{self.max_stamina} HP:{self.health}/{self.max_health} CV:{self.conviction} Equipped: {equipped_summary}'

    def equip_item(self, slot, item_data):
        """Equip an item card to a placemat slot. Updates tactics automatically."""
        if slot in self.equipped:
            # Unequip current if any
            if self.equipped[slot]:
                self._remove_bonuses(self.equipped[slot])
            # Ensure defaults for new cards
            item_data.setdefault('exhausted', False)
            item_data.setdefault('flipped', False)
            self.equipped[slot] = item_data
            if not item_data.get('exhausted', False):
                self._apply_bonuses(item_data)
            print(f"Equipped {item_data['name']} to {slot} slot.")
            return True
        return False

    def unequip_item(self, slot):
        """Remove item from placemat slot."""
        if slot in self.equipped and self.equipped[slot]:
            self._remove_bonuses(self.equipped[slot])
            name = self.equipped[slot]['name']
            self.equipped[slot] = None
            print(f"Unequipped {name} from {slot}.")
            return True
        return False

    def toggle_exhaust(self, slot):
        """Exhaust or ready the card (for tactics: exhausted cards don't provide bonuses until refreshed)."""
        if slot in self.equipped and self.equipped[slot]:
            item = self.equipped[slot]
            item['exhausted'] = not item['exhausted']
            if item['exhausted']:
                self._remove_bonuses(item)
                print(f"{item['name']} EXHAUSTED - bonuses disabled until refresh.")
            else:
                self._apply_bonuses(item)
                print(f"{item['name']} READY - bonuses active.")
            return True
        return False

    def toggle_flip(self, slot):
        """Flip the card (e.g. to exhausted side or alternate ability side)."""
        if slot in self.equipped and self.equipped[slot]:
            item = self.equipped[slot]
            item['flipped'] = not item['flipped']
            # In real Middara, flip might change abilities or exhaust state
            print(f"Flipped {item['name']} - {'back side' if item['flipped'] else 'front side'} active.")
            # Example: flip could toggle a bonus or exhaust
            if item['flipped']:
                item['exhausted'] = True
            return True
        return False

    def refresh_all(self):
        """Refresh phase: ready all exhausted cards (common in tactical games)."""
        for slot, item in self.equipped.items():
            if item and item['exhausted']:
                item['exhausted'] = False
                self._apply_bonuses(item)
        print("All equipment refreshed - ready for next round!")

    def _apply_bonuses(self, item):
        """Apply item bonuses to tactics_modifiers only (base_stats unchanged for proper equip/unequip mechanics)."""
        if 'bonuses' in item:
            for stat, val in item['bonuses'].items():
                self.tactics_modifiers[stat] = self.tactics_modifiers.get(stat, 0) + val
        # Update max resources if applicable (permanent? or also mod, but for now keep)
        if 'max_stamina_bonus' in item:
            self.max_stamina += item['max_stamina_bonus']

    def _remove_bonuses(self, item):
        """Remove bonuses when unequipping or exhausting."""
        if 'bonuses' in item:
            for stat, val in item['bonuses'].items():
                self.tactics_modifiers[stat] = self.tactics_modifiers.get(stat, 0) - val
        if 'max_stamina_bonus' in item:
            self.max_stamina -= item['max_stamina_bonus']

    def get_tactics_summary(self):
        """For combat tactics: current effective stats including equipment (base + modifiers)."""
        effective = self.base_stats.copy()
        for mod, val in self.tactics_modifiers.items():
            effective[mod] = effective.get(mod, 0) + val
        # Also include current stamina/health etc but focus on stats
        return effective

    def get_current_stats(self):
        """Return current effective stats for display."""
        effective = self.base_stats.copy()
        for mod, val in self.tactics_modifiers.items():
            effective[mod] = effective.get(mod, 0) + val
        return effective

    def get_placemat_display(self):
        """Data for UI placemat rendering: each slot with image ref, type, abilities, state."""
        display = {}
        for slot, item in self.equipped.items():
            if item:
                display[slot] = {
                    'name': item['name'],
                    'type': item.get('type', 'Unknown'),
                    'image': item.get('image', 'assets/placeholder_card.png'),  # Digital image path
                    'abilities': item.get('abilities', []),
                    'exhausted': item.get('exhausted', False),
                    'flipped': item.get('flipped', False),
                    'bonuses': item.get('bonuses', {})
                }
            else:
                display[slot] = {'name': 'Empty Slot', 'type': slot.capitalize(), 'image': None, 'abilities': [], 'exhausted': False, 'flipped': False}
        return display
