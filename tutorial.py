from party_member_factory import PartyMemberFactory
from weapon_factory import WeaponFactory
from skill_factory import SkillFactory
from enemy import Enemy
from battle import Battle
from game_menu import GameMenu


class Tutorial:

    def __init__(self, player):
        self.player = player
        self.party_members = []

    def start(self):
        print('\nWelcome to the tutorial')

        # Adding a party member for testing - can remove later
        party_member_factory = PartyMemberFactory()
        warrior_friend = party_member_factory.create_party_member('warrior_friend')
        self.party_members.append(warrior_friend)

        print(f"\n{warrior_friend.name} has joined your party!")
        print(
            f"{warrior_friend.name}'s stats: Health: {warrior_friend.health}, Speed: {warrior_friend.speed}, Weapon: {warrior_friend.weapon.name}")

        # Starting tutorial battle
        self.start_battle()

    def start_battle(self):
        print('\nStarting intro battle')

        # Create a simple enemy to battle
        weapon_factory = WeaponFactory()
        enemy_weapon = weapon_factory.create_weapon('Claw')

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill('Slash')]

        # name, health, level, exp, speed, weapon, defence, gold, class_type, skills
        enemy = Enemy('Goblin', 20, 1, 10, 6, enemy_weapon, 1, 5, 'monster', skills=skills)

        # Start the battle using the GameMenu or Battle class
        battle = Battle(self.player, [enemy], self.party_members)
        battle.start_battle()

        # After the battle, continue with the tutorial or move to the game menu
        print("\nTutorial complete! Returning to game menu...")
        GameMenu(self.player, self.party_members).display_menu()
