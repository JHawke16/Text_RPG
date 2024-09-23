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
                    print('-' * 40)
                    if not self.battle_active():
                        break

        self.end_battle()

    def take_turn(self, combatant):
        if isinstance(combatant, Player):
            self.player_turn()
        elif isinstance(combatant, PartyMember):
            self.party_member_turn(combatant)
        else:
            self.enemy_turn(combatant)

    def player_turn(self):
        print(f"\n{self.player.name}'s turn!")
        print("1. Attack")
        print("2. Use Skill")

        choice = input("\nChoose your action: ")

        if choice == '1':
            self.basic_attack(self.player, self.enemies)
        elif choice == '2':
            damage = self.player.skill_attack()
            if damage:
                target = self.choose_target(self.enemies, self.player)
                if target:
                    print(f"{self.player.name} uses a skill on {target.name} for {damage} damage!")
                    target.take_damage(damage)
            else:
                # Retry if the player didn't select a valid skill or have enough energy
                self.player_turn()
        else:
            print("Invalid choice. Try again.")
            self.player_turn()

    def party_member_turn(self, party_member):
        if random.choice(['attack', 'skill']) == 'skill':
            damage = party_member.skill_attack()
            if damage:
                target = self.choose_target(self.enemies, party_member)
                if target:
                    print(f"{party_member.name} uses a skill on {target.name} for {damage} damage!")
                    target.take_damage(damage)
            else:
                self.basic_attack(party_member, self.enemies)
        else:
            self.basic_attack(party_member, self.enemies)

    def enemy_turn(self, enemy):
        if random.choice(['attack', 'skill']) == 'skill':
            damage = enemy.skill_attack()
            if damage:
                target = self.choose_target([self.player] + self.party, enemy)
                if target:
                    print(f"{enemy.name} uses a skill on {target.name} for {damage} damage!")
                    target.take_damage(damage)
            else:
                self.basic_attack(enemy, [self.player] + self.party)
        else:
            self.basic_attack(enemy, [self.player] + self.party)

    def basic_attack(self, attacker, targets):
        target = self.choose_target(targets, attacker)
        if target:
            print(f"\n{attacker.name} attacks {target.name} for {attacker.weapon_attack()} damage!")
            target.take_damage(attacker.weapon_attack())

    def choose_target(self, targets, attacker):
        alive_targets = [target for target in targets if target.check_alive()]
        if not alive_targets:
            return None

        if isinstance(attacker, Player):
            # Player chooses a target
            print("\nChoose a target:")
            for i, target in enumerate(alive_targets):
                print(f"{i + 1}. {target.name} (HP: {target.health})")

            choice = input("\nEnter the number of the target: ")
            try:
                choice = int(choice) - 1
                if 0 <= choice < len(alive_targets):
                    return alive_targets[choice]
            except ValueError:
                pass
            print("Invalid choice.")
            return self.choose_target(alive_targets, attacker)  # Retry if invalid
        else:
            # Enemies and party members choose randomly
            return random.choice(alive_targets)

    def battle_active(self):
        if not self.player.check_alive():
            return False
        if all(not enemy.check_alive() for enemy in self.enemies):
            return False
        return True

    def end_battle(self):
        if self.player.check_alive():
            print("\nBattle Won!")
            # Distribute loot: gold and experience
            self.distribute_loot()

        else:
            print("\nBattle Lost!")

    def distribute_loot(self):
        total_exp = sum(enemy.exp for enemy in self.enemies)
        total_gold = sum(enemy.gold for enemy in self.enemies)

        # Player gets all the gold
        self.player.gain_gold(total_gold)

        # Split experience between player and party members
        members = [self.player] + self.party
        exp_per_member = total_exp // len(members) if members else 0

        for member in members:
            member.gain_exp(exp_per_member)

        print(f"\nExp Earned: {total_exp} exp shared among party members.")
