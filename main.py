from character_creation import CharacterCreation
from enemy import Enemy
from battle import Battle
from party_member import PartyMember
from weapon_factory import WeaponFactory

# Create the weapon factory
weapon_factory = WeaponFactory()

# Create weapons
copper_sword = weapon_factory.create_weapon('Copper Sword')
claw_weapon = weapon_factory.create_weapon('Claw')
bite_weapon = weapon_factory.create_weapon('Bite')

# name, health, level, exp, speed, weapon, defence, gold, class_type

# Create player and party member with class 'warrior'
character_creation = CharacterCreation()
player = character_creation.create_character()
party_member = PartyMember('PM', 15, 1, 0, 8, copper_sword, 1, 'warrior')

print(f"\nWelcome, {player.name} the {player.class_type.capitalize()}!")

# name, health, level, exp, speed, weapon, defence, gold, class_type

# Create enemies with class 'monster'
enemy1 = Enemy('Enemy1', 12, 1, 8, 10, claw_weapon, 1, 5, 'monster')
enemy2 = Enemy('Enemy2', 10, 1, 6, 6, bite_weapon, 1, 3, 'monster')

# Start the battle
battle = Battle(player, [enemy1, enemy2], [party_member])
battle.start_battle()