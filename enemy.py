import random


class Enemy:

    def __init__(self, name, health, level, exp, speed, weapon, defence, gold, class_type, skills):
        self.name = name
        self.health = health
        self.level = level
        self.exp = exp
        self.speed = speed
        self.weapon = weapon
        self.defence = defence
        self.gold = gold
        self.class_type = class_type
        self.skills = skills

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

    def skill_attack(self):
        # Selecting a skill random from the available skills with enough energy in the weapon
        available_skills = [skill for skill in self.skills if skill.energy <= self.weapon.energy]
        if available_skills:
            selected_skill = random.choice(available_skills)
            print(f"\n{self.name} uses {selected_skill.name}!")
            self.weapon.energy -= selected_skill.energy  # Deduct energy from weapon
            return selected_skill.damage  # Return damage to apply
        else:
            print(f"{self.name}'s weapon does not have enough energy for any skills.")
            return False  # No skill used
