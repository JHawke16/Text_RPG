from player import Player
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class WarriorPlayer(Player):
    def __init__(self, name):
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon('Copper Sword')

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill('Slash'), skill_factory.create_skill('Swipe')]

        # Call the parent class constructor with warrior-specific stats, including gold
        super().__init__(
            name=name,
            health=25,
            level=1,
            exp=0,
            speed=10,
            weapon=starting_weapon,
            defence=5,
            gold=0,
            class_type='warrior',
            skills=skills
        )
