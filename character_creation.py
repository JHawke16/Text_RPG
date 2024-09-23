from warrior_player import WarriorPlayer
from rogue_player import RoguePlayer
from mage_player import MagePlayer
from commoner_player import CommonerPlayer


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
                'skills': ['Slash', 'Swipe']
            },
            'rogue': {
                'health': 17,
                'speed': 20,
                'defence': 2,
                'starting_weapon': 'Copper Dagger',
                'class_type': 'rogue',
                'skills': ['Sap', 'Backstab']
            },
            'mage': {
                'health': 15,
                'speed': 8,
                'defence': 1,
                'starting_weapon': 'Wooden Staff',
                'class_type': 'mage',
                'skills': ['Flames', 'Fireball']
            },
            'commoner': {
                'health': 15,
                'speed': 6,
                'defence': 1,
                'starting_weapon': 'Wooden Club',
                'class_type': 'commoner',
                'skills': ['Bash', 'Whack']
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

        # Create an instance of the chosen player class
        if chosen_class == 'warrior':
            return WarriorPlayer(name)
        elif chosen_class == 'rogue':
            return RoguePlayer(name)
        elif chosen_class == 'mage':
            return MagePlayer(name)
        elif chosen_class == 'commoner':
            return CommonerPlayer(name)
        else:
            print("Invalid class choice")
            self.create_character()
