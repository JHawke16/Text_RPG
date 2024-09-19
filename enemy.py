class Enemy:

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

    def drop_exp(self):
        return self.exp

    def drop_gold(self):
        return self.gold
