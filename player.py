class Player:

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

    def skill_attack(self):
        # Checking if the weapon has enough energy for a skill
        available_skills = [skill for skill in self.skills if skill.energy <= self.weapon.energy]
        if not available_skills:
            print(f"{self.weapon.name} does not have enough energy for any skills.")
            return False  # No available skills

        # Display available skills to the player
        print("\nAvailable Skills:\n")
        for i, skill in enumerate(available_skills):
            print(f"{i + 1}. {skill.name} - Damage: {skill.damage}, Energy Cost: {skill.energy}")

        # Asking player to select a skill
        try:
            choice = int(input("\nChoose a skill to use (enter the number): ")) - 1
            if 0 <= choice < len(available_skills):
                selected_skill = available_skills[choice]
                if self.weapon.energy >= selected_skill.energy:
                    self.weapon.energy -= selected_skill.energy  # Deduct energy from weapon
                    return selected_skill.damage  # Return damage to apply

                else:
                    print("Not enough energy for this skill!")

            else:
                print('Invalid Skill')

        except ValueError:
            print("Please enter a valid number!")

        return self.skill_attack()  # Retry selection if input is invalid
