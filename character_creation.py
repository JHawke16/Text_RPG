from player import Player
from weapon_factory import WeaponFactory


class CharacterCreation:

    def __init__(self):
        # Predefined setups
        self.setups = {
            'warrior': {
                'health': 25,
                'speed': 10,
                'defence': 5,
                'starting_weapon': 'Copper Sword',
                'class_type': 'warrior',
                'skills': ['Slash', 'Swipe']  # Placeholder skills
            },
            'rogue': {
                'health': 17,
                'speed': 20,
                'defence': 2,
                'starting_weapon': 'Dagger',  # Placeholder
                'class_type': 'rogue',
                'skills': ['Sap, Backstab']  # PLaceholder skills
            },
            'mage': {
                'health': 15,
                'speed': 8,
                'defence': 1,
                'starting_weapon': 'Fire Staff',  # Placeholder
                'class_type': 'mage',
                'skills': ['Flames', 'Fireball']  # Placeholder skills
            },
            'commoner': {
                'health': 15,
                'speed': 6,
                'defence': 1,
                'starting_weapon': 'Club',  # Placeholder
                'class_type': 'commoner',
                'skills': ['Bash', 'Whack']  # Placeholder skills
            }
        }

    def display_class_info(self, class_name):
        setup = self.setups[class_name]
        print(f"\nClass: {class_name.capitalize()}")
        print(f"Health: {setup['health']}")
        print(f"Speed: {setup['speed']}")
        print(f"Defence: {setup['defence']}")
        print(f"Starting Weapon: {setup['starting_weapon']}")
        print(f"Skills: {', '.join(setup['skills'])}")
        print('-' * 30)

    def create_character(self):
        # Displaying options to user
        print('\nWelcome to Character Creation!\n')
        print('Available classes:')
        for setup_name in self.setups.keys():
            self.display_class_info(setup_name)

        # Getting user choice
        chosen_class = None
        while chosen_class not in self.setups:
            chosen_class = input("\nEnter the name of the class you want to choose: ").lower()

        # Character Name
        name = input('\nEnter a name for your character: ')

        # Getting the setup data
        setup = self.setups[chosen_class]

        # Initialising the weapon using the WeaponFactory
        weapon_factory = WeaponFactory()
        starting_weapon = weapon_factory.create_weapon(setup['starting_weapon'])

        # Returning player instance
        return Player(
            name=name,
            health=setup['health'],
            level=1,
            exp=0,
            speed=setup['speed'],
            weapon=starting_weapon,
            defence=setup['defence'],
            gold=0,
            class_type=setup['class_type']
        )
