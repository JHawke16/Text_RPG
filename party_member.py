import random


class PartyMember:

    def __init__(self, name, health, level, exp, speed, weapon, defence, class_type, skills):
        self.name = name
        self.health = health
        self.level = level
        self.exp = exp
        self.speed = speed
        self.weapon = weapon
        self.defence = defence
        self.exp_to_next_level = 10
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

    def skill_attack(self):
        # Selecting a skill random from the available skills with enough energy in the weapon
        available_skills = [skill for skill in self.skills if skill.energy <= self.weapon.energy]
        if available_skills:
            selected_skill = random.choice(available_skills)
            self.weapon.energy -= selected_skill.energy  # Deduct energy from weapon
            return selected_skill.damage  # Return damage to apply
        else:
            print(f"{self.name}'s weapon does not have enough energy for any skills.")
            return False  # No skill used
