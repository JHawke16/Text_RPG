from battle import Battle
from emma_pm import EmmaPM
from enemy_factory import EnemyFactory
from game_menu import GameMenu
from item_factory import ItemFactory
from loot_table_factory import LootTableFactory


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

        # Adding the factories
        item_factory = ItemFactory()
        loot_table_factory = LootTableFactory()

        # Starting the tutorial battle
        self.start_battle(item_factory, loot_table_factory)

    def start_battle(self, item_factory, loot_table_factory):
        print('\nStarting intro battle')

        # Initialize enemy factory and create enemies
        enemy_factory = EnemyFactory()
        goblin = enemy_factory.create_enemy('Cave Goblin', level=1)
        orc = enemy_factory.create_enemy('Orc Soldier', level=1)

        # Start the battle, passing in the item_factory and loot_table_factory
        battle = Battle(self.player, [goblin, orc], self.party_members)
        battle.start_battle(item_factory, loot_table_factory)

        # After battle, return to the game menu or continue tutorial
        print("\nTutorial complete! Returning to game menu...")
        GameMenu(self.player, self.party_members).display_menu()
