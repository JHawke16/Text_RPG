import random
from weapon import Weapon
import csv


class WeaponFactory:

    def __init__(self):
        # Setting the path
        csv_file = r"C:\Users\bhall\Documents\Pycharm Projects\Text_RPG\weapons.csv"
        self.weapons_blueprints = self.load_weapons_from_csv(csv_file)

    def load_weapons_from_csv(self, csv_file):
        weapons = {}
        with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:  # Use utf-8-sig to remove BOM
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name'].strip()
                weapons[name] = {
                    'base_damage': int(row['damage']),
                    'base_energy': int(row['energy']),
                    'value': int(row['value']),
                    'allowed_classes': row['allowed_classes'].split(';'),
                    'weapon_type': row['weapon_type'],
                    'rarity_weights': {
                        'basic': int(row['basic_weight']),
                        'common': int(row['common_weight']),
                        'masterwork': int(row['masterwork_weight']),
                        'rare': int(row['rare_weight']),
                        'epic': int(row['epic_weight'])
                    }
                }
        return weapons

    def get_random_rarity(self, rarity_weights):
        rarities = list(rarity_weights.keys())
        chances = list(rarity_weights.values())
        return random.choices(rarities, chances)[0]

    def create_weapon(self, weapon_name):
        blueprint = self.weapons_blueprints.get(weapon_name)
        if not blueprint:
            raise ValueError(f'Weapon {weapon_name} does not exist in the factory')

        # Determine the rarity dynamically based on the weights
        rarity = self.get_random_rarity(blueprint['rarity_weights'])

        return Weapon(
            name=weapon_name,
            damage=blueprint['base_damage'],
            energy=blueprint['base_energy'],
            value=blueprint['value'],
            rarity=rarity,
            allowed_classes=blueprint['allowed_classes'],
            weapon_type=blueprint['weapon_type']
        )
