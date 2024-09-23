from skill import Skill
import csv
import random


class SkillFactory:
    def __init__(self):
        # Set the path for the skills CSV
        csv_file = r"C:\Users\bhall\Documents\Pycharm Projects\Text_RPG\skills.csv"
        self.skills_blueprints = self.load_skills_from_csv(csv_file)

    def load_skills_from_csv(self, csv_file):
        skills = {}
        with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name'].strip()
                skills[name] = {
                    'damage': int(row['damage']),
                    'energy': int(row['energy']),
                    'value': int(row['value']),
                    'allowed_weapons': row['allowed_weapons'].split(';'),  # Allowing multiple weapons
                    'rarity_weights': {
                        'basic': int(row['basic_weight']),
                        'common': int(row['common_weight']),
                        'masterwork': int(row['masterwork_weight']),
                        'rare': int(row['rare_weight']),
                        'epic': int(row['epic_weight'])
                    }
                }
        return skills

    def get_random_rarity(self, rarity_weights):
        rarities = list(rarity_weights.keys())
        chances = list(rarity_weights.values())
        return random.choices(rarities, chances)[0]

    def create_skill(self, skill_name):
        blueprint = self.skills_blueprints.get(skill_name)
        if not blueprint:
            raise ValueError(f'Skill {skill_name} does not exist in the factory')

        # Determine the rarity dynamically based on the weights
        rarity = self.get_random_rarity(blueprint['rarity_weights'])

        return Skill(
            name=skill_name,
            damage=blueprint['damage'],
            energy=blueprint['energy'],
            value=blueprint['value'],
            rarity=rarity,
            allowed_weapons=blueprint['allowed_weapons']
        )
