from weapon_factory import WeaponFactory
from party_member import PartyMember
from skill_factory import SkillFactory


class PartyMemberFactory:

    def __init__(self):
        self.party_members_blueprints = {
            'warrior_friend': {
                'name': 'Ragnar',
                'health': 30,
                'speed': 8,
                'defence': 4,
                'class_type': 'warrior',
                'starting_weapon': 'Copper Sword',
                'skills': ['Swipe', 'Slash'],
                'level': 1
            },
            'mage_friend': {  # Only a placeholder for now
                'name': 'Elara',
                'health': 20,
                'speed': 12,
                'defence': 2,
                'class_type': 'mage',
                'starting_weapon': 'Staff',
                'skills': ['Fireball'],
                'level': 1
            }
            # Can add more here
        }

    def create_party_member(self, member_key):
        blueprint = self.party_members_blueprints.get(member_key)
        if not blueprint:
            raise ValueError(f"Party member {member_key} does not exist.")

        # Initialising the weapon
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon(blueprint['starting_weapon'])

        # Initialising the skills
        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill(skill_name) for skill_name in blueprint['skills']]

        return PartyMember(
            name=blueprint['name'],
            health=blueprint['health'],
            level=blueprint['level'],
            exp=0,  # Starting experience
            speed=blueprint['speed'],
            weapon=starting_weapon,
            defence=blueprint['defence'],
            class_type=blueprint['class_type'],
            skills=skills
        )

