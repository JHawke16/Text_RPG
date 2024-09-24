import csv
import random

from item_factory import ItemFactory


class LootTableFactory:
    def __init__(self, csv_file=None, item_factory=None):
        # Use the default path if no path is provided
        self.csv_file = csv_file or r"C:\Users\bhall\Documents\Pycharm Projects\Text_RPG\loot_table.csv"
        self.loot_tables = self.load_loot_tables(self.csv_file)
        self.item_factory = item_factory or ItemFactory()  # Default to using the ItemFactory

    def load_loot_tables(self, csv_file):
        loot_tables = {}
        with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loot_table = row['loot_table']
                if loot_table not in loot_tables:
                    loot_tables[loot_table] = []
                loot_tables[loot_table].append({
                    'item_name': row['item_name'],
                    'drop_chance': float(row['drop_chance'])
                })
        return loot_tables

    def get_loot_from_table(self, loot_table_name):
        if loot_table_name not in self.loot_tables:
            print(f"Loot table '{loot_table_name}' not found.")
            return []

        loot_items = []
        for loot_entry in self.loot_tables[loot_table_name]:
            if random.random() <= loot_entry['drop_chance']:
                loot_items.append(loot_entry)
        return loot_items
