class Item:
    def __init__(self, name, value, category):
        self.name = name
        self.value = value
        self.category = category

    def __str__(self):
        return f"{self.name} (Category: {self.category}, Value: {self.value})"

    def use(self, player):
        # Default use case for items that don't have a specific 'use'
        print(f"{self.name} cannot be used directly.")
