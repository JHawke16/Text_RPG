import csv

from consumable_item import ConsumableItem
from item import Item


class ItemFactory:
    def __init__(self, csv_file=None):
        # Use the default path if no path is provided
        self.csv_file = csv_file or r"C:\Users\bhall\Documents\Pycharm Projects\Text_RPG\items.csv"
        self.items_blueprints = self.load_items_from_csv(self.csv_file)

    def load_items_from_csv(self, csv_file):
        items = {}
        with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items[row['item_name']] = {
                    'name': row['item_name'],
                    'value': int(row['value']),
                    'item_type': row['item_type'],
                    'effect': row['effect'],  # Storing the effect of consumable items
                    'category': row['category']  # The category of the item
                }
        return items

    def create_item(self, item_name):
        if item_name not in self.items_blueprints:
            raise ValueError(f"Item {item_name} does not exist.")

        blueprint = self.items_blueprints[item_name]
        item_type = blueprint['item_type']
        effect = blueprint['effect']
        category = blueprint['category']

        # Handle consumable items
        if item_type == "consumable":
            return ConsumableItem(
                name=blueprint['name'],
                value=blueprint['value'],
                effect=effect,
                category=category
            )
        # Handle other item types (e.g., materials, quest items)
        else:
            return Item(
                name=blueprint['name'],
                value=blueprint['value'],
                category=category
            )
