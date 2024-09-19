from player import Player
from party_member import PartyMember
import random


class Battle:

    def __init__(self, player, enemies, party=None):
        self.player = player
        self.enemies = enemies
        self.party = party if party is not None else []
        self.combatants = [player] + self.party + enemies

    def start_battle(self):
        # Sort combatants by speed in descending order for turn order
        self.combatants.sort(key=lambda x: x.speed, reverse=True)

        while self.battle_active():
            for combatant in self.combatants:
                if combatant.check_alive():
                    self.take_turn(combatant)
                    if not self.battle_active():
                        break

        self.end_battle()

    def take_turn(self, combatant):
        # Placeholder logic for combatant taking their turn
        if isinstance(combatant, Player):
            target = self.player_choose_target(self.enemies)
        elif isinstance(combatant, PartyMember):
            target = self.choose_target(self.enemies)
        else:
            target = self.choose_target([self.player] + self.party)

        if target:
            print('-----------------------------')
            print(f'\n\n{combatant.name} attacks {target.name} for {combatant.weapon_attack()} damage')
            target.take_damage(combatant.weapon_attack())

    def player_choose_target(self, targets):
        # Displaying alive targets to the player
        alive_targets = [target for target in targets if target.check_alive()]
        if not alive_targets:
            return None

        while True:
            print('-----------------------------')
            print('\nChoose an enemy to attack:')
            for i, target in enumerate(alive_targets):
                print(f'{i + 1}. {target.name} - Health: {target.health}')  # Health only showing for debugging

            # Getting the player choice
            try:
                choice = int(input('\nEnter the number of which enemy you want to attack\nChoice:')) - 1
                if 0 <= choice < len(alive_targets):
                    return alive_targets[choice]
                else:
                    print('Invalid choice! Please enter a valid number')
            except ValueError:
                print('Invalid input! Please enter a valid number')

    def choose_target(self, targets):
        # Selecting a random target for now from the list of avaliable targets
        alive_targets = [target for target in targets if target.check_alive()]
        if alive_targets:
            return random.choice(alive_targets)
        return None

    def battle_active(self):
        if not self.player.check_alive():
            return False
        if all(not enemy.check_alive() for enemy in self.enemies):
            return False
        return True

    def end_battle(self):
        if self.player.check_alive():
            print('-----------------------------')
            print('\n\nBattle Won!')
            self.distribute_loot()
        else:
            print('\n\nBattle Lost!')

    def distribute_loot(self):
        total_exp = sum(enemy.drop_exp() for enemy in self.enemies)
        total_gold = sum(enemy.drop_gold() for enemy in self.enemies)

        # Player gets the gold
        self.player.gain_gold(total_gold)

        # Splitting exp between player and party members
        members = [self.player] + self.party
        if members:
            exp_per_member = total_exp // len(members)
            for member in members:
                member.gain_exp(exp_per_member)
            print(f'\nExp Earned: {total_exp} exp for all party members')
            print('-----------------------------')
