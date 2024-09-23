import random


class Enemy:
    def __init__(self, name, health, speed, weapon, defence, class_type, skills, level=1):
        self.name = name
        self.base_health = health
        self.speed = speed
        self.weapon = weapon
        self.defence = defence
        self.class_type = class_type
        self.skills = skills
        self.level = level
        self.health = self.base_health  # Final health after scaling
        self.gold = 10  # Starting gold (scalable)
        self.exp = 5  # Starting exp (scalable)

        # Scale enemy stats based on level
        self.level_scaler()

    def check_alive(self):
        return self.health > 0

    def level_scaler(self):
        # Adjust the scaling factor formula for more meaningful scaling
        scaling_factor = 1 + (self.level * 0.5)  # Scaling increases faster based on level

        # Apply scaling to stats
        self.health = int(self.base_health * scaling_factor)
        self.defence = int(self.defence * scaling_factor)
        self.weapon.damage = int(self.weapon.damage * scaling_factor)

        # Scale gold and exp more meaningfully
        self.gold = int(10 * scaling_factor)  # Baseline gold starts at 10 and scales with level
        self.exp = int(5 * scaling_factor)  # Baseline exp starts at 5 and scales with level

    def take_damage(self, damage):
        damage -= self.defence
        self.health -= max(damage, 0)  # Ensuring damage isn't negative
        if self.health < 0:
            self.health = 0
        print(f'{self.name} takes {damage} damage\n{self.name} remaining health: {self.health} HP')

    def drop_exp(self):
        return self.exp

    def drop_gold(self):
        return self.gold

    def weapon_attack(self):
        return self.weapon.damage

    def skill_attack(self):
        # Selecting a skill random from the available skills with enough energy in the weapon
        available_skills = [skill for skill in self.skills if skill.energy <= self.weapon.energy]
        if available_skills:
            selected_skill = random.choice(available_skills)
            self.weapon.energy -= selected_skill.energy  # Deduct energy from weapon
            return selected_skill.damage  # Return damage to apply
        else:
            print(f"\n{self.name}'s weapon does not have enough energy for any skills.")
            return False  # No skill used
