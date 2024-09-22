class Skill:

    def __init__(self, name, damage, energy, value, rarity, allowed_weapons):
        self.name = name
        self.damage = damage
        self.energy = energy
        self.value = value
        self.rarity = rarity
        self.allowed_weapons = allowed_weapons  # List of weapon types that can use this skill

    def __str__(self):
        return f"Skill: {self.name} (Damage: {self.damage}, Energy Cost: {self.energy})"
