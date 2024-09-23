from enemy_factory import EnemyFactory
from battle import Battle
from game_menu import GameMenu
from emma_pm import EmmaPM


class Tutorial:

    def __init__(self, player):
        self.player = player
        self.party_members = []

    def start(self):
        print('\nWelcome to the tutorial')

        # Initializing Emma as a party member
        emma = EmmaPM()
        self.party_members.append(emma)

        print(f"\n{emma.name} has joined your party!")
        print(f"{emma.name}'s stats: Health: {emma.health}, Speed: {emma.speed}, Weapon: {emma.weapon.name}")

        # Starting tutorial battle
        self.start_battle()

        # Starting tutorial battle
        self.start_battle()

    def start_battle(self):
        print('\nStarting intro battle')

        # Create enemy using EnemyFactory
        enemy_factory = EnemyFactory()

        # Create two enemies for the battle (adjust levels as needed)
        goblin = enemy_factory.create_enemy('Cave Goblin', level=1)
        orc = enemy_factory.create_enemy('Orc Soldier', level=1)

        # Start the battle using the GameMenu or Battle class
        battle = Battle(self.player, [goblin, orc], self.party_members)
        battle.start_battle()

        # After the battle, continue with the tutorial or move to the game menu
        print("\nTutorial complete! Returning to game menu...")
        GameMenu(self.player, self.party_members).display_menu()
