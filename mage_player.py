from player import Player
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class MagePlayer(Player):
    def __init__(self, name):
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon('Wooden Staff')

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill('Flames'), skill_factory.create_skill('Fireball')]

        super().__init__(
            name=name,
            health=15,
            level=1,
            exp=0,
            speed=8,
            weapon=starting_weapon,
            defence=1,
            gold=0,
            class_type='mage',
            skills=skills
        )
