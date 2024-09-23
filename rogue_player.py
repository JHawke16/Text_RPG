from player import Player
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class RoguePlayer(Player):
    def __init__(self, name):
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon('Copper Dagger')

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill('Sap'), skill_factory.create_skill('Backstab')]

        super().__init__(
            name=name,
            health=17,
            level=1,
            exp=0,
            speed=20,
            weapon=starting_weapon,
            defence=2,
            gold=0,
            class_type='rogue',
            skills=skills
        )
