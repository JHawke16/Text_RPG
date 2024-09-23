from party_member import PartyMember
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory


class EmmaPM(PartyMember):
    def __init__(self):
        # Initializing Emma's attributes using the Wooden Staff and mage-specific skills
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon('Wooden Staff')  # Emma's mage weapon

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill('Fireball'), skill_factory.create_skill('Flames')]

        # Call the parent class constructor with Emma's stats
        super().__init__(
            name='Emma',
            health=25,  # Mage class has lower health
            level=1,
            exp=0,
            speed=8,  # Mages tend to have lower speed
            weapon=starting_weapon,
            defence=2,  # Light defence for mages
            class_type='mage',  # Emma is a mage
            skills=skills
        )

    # Can add Emma-specific methods later if needed, like quest-related features
