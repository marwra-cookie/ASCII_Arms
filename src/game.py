import os
from item_manager import *


class Game:

    def __init__(self, player):
        self.player = player
        self.slain = 0

    def run(self):
        self.menu()

    def menu_combat(self):
        while True:
            os.system("cls")
            print(
                f"Combat options"
                f"\n\n1. Normal fight"
                f"\n2. Boss encounter [{self.slain}/4]"
                f"\n\n3. Back"
            )

            choice = input("> ")

            if choice == "1":
                # ToDo
                break
            elif choice == "2":
                # ToDo
                break
            elif choice == "3":
                break
            else:
                print(f"{error}")

    def menu_character(self):
        while True:
            os.system("cls")

            print(
                f"CHARACTER"
                f"\n\n{self.player.get_stats()}"
                f"\n\n1. Items"
                f"\n2. Spells"
                f"\n\n3. Back"
            )

            choice = input("> ")

            if choice == "1":
                self.menu_items()
            elif choice == "2":
                self.menu_spells()
            elif choice == "3":
                break
            else:
                print(f"{error}")

    def menu_items(self):
        while True:
            os.system("cls")
            print(f"GEAR" f"\n\n{self.player.get_items()}" f"\n3. Back")
            choice = input("> ")

            if choice == "3":
                break
            else:
                print(f"{error}")

    def menu_spells(self):
        while True:
            os.system("cls")
            print(f"SPELLS" f"\n\n{self.player.get_spells()}" f"\n\n3. Back")

            choice = input("> ")

            if choice == "3":
                break
            else:
                print(f"{error}")

    # TODO: Save game to file
    def menu_save(self):
        os.system("cls")

    def menu(self):

        while True:
            os.system("cls")

            print(
                f"--- DMG SIM ---"
                f"\n{self.player.name} lvl.{self.player.level}"
                f"\n\n1. Combat"
                f"\n2. Character"
                f"\n3. Save"
                f"\n\n4. Quit"
            )

            choice = input("> ")

            if choice == "1":
                self.menu_combat()
            elif choice == "2":
                self.menu_character()
            elif choice == "3":
                self.menu_save()
            elif choice == "4":
                print("Exiting game...")
                break
            else:
                print(f"{error}")
