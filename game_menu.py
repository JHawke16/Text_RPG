class GameMenu:

    def __init__(self, player, party_members=None):
        self.player = player
        self.party_members = party_members if party_members else []

    def display_menu(self):
        while True:
            print("\nGame Menu:")
            print("1. Continue")
            print("2. View Items (Placeholder)")
            print("3. View Stats")
            print("4. View Party Members")
            print("5. View Quests (Placeholder)")
            print("6. Change Difficulty (Placeholder)")
            print("7. Save (Placeholder)")
            print("8. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                print("Continuing the game...")
                break  # Placeholder to simulate game progression
            elif choice == '2':
                print("View Items - (Placeholder)")
            elif choice == '3':
                self.view_stats()
            elif choice == '4':
                self.view_party_members()
            elif choice == '5':
                print("View Quests - (Placeholder)")
            elif choice == '6':
                print("Change Difficulty - (Placeholder)")
            elif choice == '7':
                print("Save - (Placeholder)")
            elif choice == '8':
                print("Exiting to Main Menu...")
                # Lazy import MainMenu inside the function to avoid circular import
                from main_menu import MainMenu
                MainMenu().display_menu()  # Return to main menu
                break
            else:
                print("Invalid choice, please try again.")


    def view_stats(self):
        print(f"\n{self.player.name}'s Stats:")
        print(f"Health: {self.player.health}")
        print(f"Speed: {self.player.speed}")
        print(f"Defence: {self.player.defence}")
        print(f"Weapon: {self.player.weapon.name} - Damage: {self.player.weapon.damage} - Energy: {self.player.weapon.energy}")
        print(f"Experience: {self.player.exp}/{self.player.exp_to_next_level}")
        print(f"Level: {self.player.level}")
        print(f"Gold: {self.player.gold}")

    def view_party_members(self):
        if not self.party_members:
            print("\nNo party members.")
        else:
            print("\nParty Members:")
            for member in self.party_members:
                print(f"- {member.name} ({member.class_type}) - Health: {member.health}, Level: {member.level}")