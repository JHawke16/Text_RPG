from player import Player
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class CommonerPlayer(Player):
    def __init__(self, name):
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon('Wooden Club')

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill('Bash'), skill_factory.create_skill('Whack')]

        super().__init__(
            name=name,
            health=15,
            level=1,
            exp=0,
            speed=6,
            weapon=starting_weapon,
            defence=1,
            gold=0,
            class_type='commoner',
            skills=skills
        )
