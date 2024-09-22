from character_creation import CharacterCreation
from tutorial import Tutorial


class MainMenu:

    def display_menu(self):

        while True:
            print("\nMain Menu:")
            print("1. New Game")
            print("2. Load Game")
            print("3. Options")
            print("4. Info")
            print("5. Exit")

            choice = input('\nEnter your choice: ')

            if choice == '1':
                self.new_game()
            elif choice == '2':
                print("Load Game - (Placeholder)")
            elif choice == '3':
                print("Options - (Placeholder)")
            elif choice == '4':
                print("Game Info - RPG Game v0.2.0 Alpha")
            elif choice == '5':
                print("Exiting game...")
                break
            else:
                print("Invalid choice, please try again.")

    def new_game(self):
        print('\nStarting a new game')
        # Initialising the character creator
        character_creation = CharacterCreation()
        player = character_creation.create_character()
        print(f"\nWelcome, {player.name} the {player.class_type.capitalize()}!")
        # Proceeding to the tutorial
        Tutorial(player).start()
