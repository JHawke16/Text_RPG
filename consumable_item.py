from item import Item


class ConsumableItem(Item):
    def __init__(self, name, value, effect, category):
        super().__init__(name, value, category)
        self.effect = effect

    def use(self, player):
        # Apply the consumable's effect based on the effect string
        if "restore" in self.effect:
            # Handle HP restoration
            if "HP" in self.effect:
                hp_restore = int(self.effect.split()[1])
                print(f"{self.name} used! Restoring {hp_restore} HP.")
                player.health += hp_restore

            # Handle energy restoration
            if "energy" in self.effect:
                energy_restore = int(self.effect.split()[1])
                print(f"{self.name} used! Restoring {energy_restore} energy.")
                player.energy += energy_restore
        else:
            print(f"{self.name} cannot be used.")
