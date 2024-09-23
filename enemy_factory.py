from skill_factory import SkillFactory
from weapon_factory import WeaponFactory
from enemy import Enemy
import csv


class EnemyFactory:
    def __init__(self):
        # Path to enemy CSV
        csv_file = r"C:\Users\bhall\Documents\Pycharm Projects\Text_RPG\enemies.csv"
        self.enemies_blueprints = self.load_enemies_from_csv(csv_file)

    def load_enemies_from_csv(self, csv_file):
        enemies = {}
        with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name'].strip()
                enemies[name] = {
                    'base_health': int(row['health']),
                    'speed': int(row['speed']),
                    'weapon': row['weapon'],  # Weapon loaded later
                    'defence': int(row['defence']),
                    'class_type': row['class_type'],
                    'skills': row['skills'].split(';')
                }
        return enemies

    def create_enemy(self, enemy_name, level=1):
        blueprint = self.enemies_blueprints.get(enemy_name)
        if not blueprint:
            raise ValueError(f'Enemy {enemy_name} does not exist in the factory')

        # Initialize weapon and skills using factories
        weapon_factory = WeaponFactory()
        weapon = weapon_factory.create_weapon(blueprint['weapon'])

        skill_factory = SkillFactory()
        skills = [skill_factory.create_skill(skill_name) for skill_name in blueprint['skills']]

        # Create and return an enemy object
        return Enemy(
            name=enemy_name,
            health=blueprint['base_health'],
            speed=blueprint['speed'],
            weapon=weapon,
            defence=blueprint['defence'],
            class_type=blueprint['class_type'],
            skills=skills,
            level=level  # Scaling starts from level 1
        )
