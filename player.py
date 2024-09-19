class Player:

    def __init__(self, name, health, level, exp, speed, weapon, defence, gold, class_type):
        self.name = name
        self.health = health
        self.level = level
        self.exp = exp
        self.speed = speed
        self.weapon = weapon
        self.defence = defence
        self.gold = gold
        self.class_type = class_type
        self.exp_to_next_level = 10

    def check_alive(self):
        return self.health > 0

    def weapon_attack(self):
        return self.weapon.damage

    def take_damage(self, damage):
        damage -= self.defence
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f'\n{self.name} takes {damage} damage')
        print(f'\n{self.name} remaining health: {self.health} HP')

    def gain_gold(self, amount):
        self.gold += amount
        print(f"\n{self.name} gained {amount} gold! Total Gold: {self.gold}")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"\n{self.name} gained {amount} EXP! Total EXP: {self.exp}")
        while self.exp >= self.exp_to_next_level:
            self.exp -= self.exp_to_next_level
            self.level_up()
        # Display current EXP after leveling up
        print(f"{self.name} Total EXP: {self.exp}/{self.exp_to_next_level} needed for next level")

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to Level {self.level}!")
        # Example: Increase exp required for next level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
