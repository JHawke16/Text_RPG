import random


class Enemy:
    def __init__(self, name, health, speed, weapon, defence, class_type, skills, loot_table, level=1):
        self.name = name
        self.base_health = health
        self.speed = speed
        self.weapon = weapon
        self.defence = defence
        self.class_type = class_type
        self.skills = skills
        self.loot_table = loot_table  # New loot_table parameter
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
        # Selecting a skill randomly from the available skills with enough energy in the weapon
        available_skills = [skill for skill in self.skills if skill.energy <= self.weapon.energy]
        if available_skills:
            selected_skill = random.choice(available_skills)
            self.weapon.energy -= selected_skill.energy  # Deduct energy from weapon
            return selected_skill.damage  # Return damage to apply
        else:
            print(f"\n{self.name}'s weapon does not have enough energy for any skills.")
            return False  # No skill used

    def drop_loot(self, item_factory, loot_table_factory):
        # Dropping loot based on the enemy's loot table.
        # print(f"{self.name} defeated! Checking loot table: {self.loot_table}") # Keep for debugging

        loot_items = []
        for loot_table in self.loot_table:
            # Retrieving loot from each loot table assigned to the enemy
            loot_items += loot_table_factory.get_loot_from_table(loot_table)

        dropped_items = []
        for loot_item in loot_items:
            # Creating the item using the ItemFactory
            item = item_factory.create_item(loot_item['item_name'])
            print(f"\n{self.name} dropped {item.name}.")
            dropped_items.append(item)

        return dropped_items  # Returning the list of dropped items
