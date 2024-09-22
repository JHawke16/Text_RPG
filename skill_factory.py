from skill import Skill


class SkillFactory:
    def __init__(self):
        self.skills_blueprints = {
            'Slash': {
                'damage': 10,
                'energy': 2,
                'value': 50,
                'rarity': 'common',
                'allowed_weapons': ['sword', 'axe']
            },
            'Fireball': {
                'damage': 15,
                'energy': 8,
                'value': 100,
                'rarity': 'rare',
                'allowed_weapons': ['staff']
            },
            'Swipe': {
                'damage': 12,
                'energy': 3,
                'value': 60,
                'rarity': 'common',
                'allowed_weapons': ['sword, axe']
            },
            # Add more skills here
        }

    def create_skill(self, skill_name):
        blueprint = self.skills_blueprints.get(skill_name)
        if not blueprint:
            raise ValueError(f"Skill {skill_name} does not exist.")

        return Skill(
            name=skill_name,
            damage=blueprint['damage'],
            energy=blueprint['energy'],
            value=blueprint['value'],
            rarity=blueprint['rarity'],
            allowed_weapons=blueprint['allowed_weapons']
        )
