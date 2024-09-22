import random
from weapon import Weapon


class WeaponFactory:

    def __init__(self):
        # Weapon Blueprints
        self.weapons_blueprints = {
            'Copper Sword': {
                'base_damage': 7,
                'base_energy': 2,
                'value': 5,
                'allowed_classes': ['warrior', 'berserker'],
                'rarity_weights': {
                    'basic': 70,
                    'common': 30
                }

            },
            'Claw': {
                'base_damage': 5,
                'base_energy': 2,
                'value': 0,
                'allowed_classes': 'monster',
                'rarity_weights': {
                    'basic': 100
                }

            },
            'Bite': {
                'base_damage': 7,
                'base_energy': 2,
                'value': 0,
                'allowed_classes': 'monster',
                'rarity_weights': {
                    'basic': 70,
                    'common': 30
                }

            },
            # New blueprints go here

        }

    def create_weapon(self, weapon_name):
        # Getting the blueprint
        blueprint = self.weapons_blueprints.get(weapon_name)
        if not blueprint:
            raise ValueError(f'Weapon {weapon_name} does not exist in the factory')

        # Determining the rarity based on the weights
        rarity = self.get_random_rarity(blueprint['rarity_weights'])

        # Creating and returning the weapon
        return Weapon(
            name=weapon_name,
            damage=blueprint['base_damage'],
            energy=blueprint['base_energy'],
            value=blueprint['value'],
            rarity=rarity,
            allowed_classes=blueprint['allowed_classes']
        )

    def get_random_rarity(self, weights):
        rarities = list(weights.keys())
        chances = list(weights.values())
        return random.choices(rarities, chances)[0]
