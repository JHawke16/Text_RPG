class Weapon:

    def __init__(self, name, damage, energy, value, rarity, allowed_classes, weapon_type):
        self.name = name
        self.damage = damage
        self.energy = energy
        self.value = value
        self.rarity = rarity
        self.allowed_classes = allowed_classes  # List of classes that can equip this weapon
        self.weapon_type = weapon_type
        self.apply_rarity_modifier()

    def apply_rarity_modifier(self):
        # Rarity scaling factors
        rarity_modifiers = {
            'basic': 1.0,
            'common': 1.2,
            'masterwork': 1.5,
            'rare': 1.8,
            'epic': 2.0
        }

        modifier = rarity_modifiers.get(self.rarity, 1.0)
        self.damage = int(self.damage * modifier)
        self.energy = int(self.energy * modifier)

    def __str__(self):
        return f"{self.name} ({self.rarity.capitalize()}) - Damage: {self.damage}, Energy: {self.energy}, Value: {self.value}"
