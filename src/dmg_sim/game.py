from launcher import update
from sub import *

player = None
slain = 0


def menu_combat():
    while True:
        update()
        print(
            f"Combat options"
            f"\n\n1. Normal fight"
            f"\n2. Boss encounter [{slain}/4]"
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


def menu_character():
    while True:
        update()

        print(
            f"CHARACTER"
            f"\n\n{player.get_stats()}"
            f"\n\n1. Items"
            f"\n2. Spells"
            f"\n\n3. Back"
        )

        choice = input("> ")

        if choice == "1":
            menu_items()
        elif choice == "2":
            menu_spells()
        elif choice == "3":
            break


def menu_items():
    while True:
        update()
        print(f"GEAR" f"\n\n{player.get_items()}" f"\n3. Back")
        choice = input("> ")

        if choice == "3":
            break


def menu_spells():
    while True:
        update()
        print(f"SPELLS" f"\n\n{player.get_spells()}" f"\n\n3. Back")

        choice = input("> ")

        if choice == "3":
            break


# TODO: Save game to file
def menu_save():
    update()


def menu():

    while True:
        update()

        print(
            f"--- DMG SIM ---"
            f"\n{player.name} lvl.{player.level}"
            f"\n\n1. Combat"
            f"\n2. Character"
            f"\n3. Save"
            f"\n\n4. Quit"
        )

        choice = input("> ")

        if choice == "1":
            menu_combat()
        elif choice == "2":
            menu_character()
        elif choice == "3":
            menu_save()
        elif choice == "4":
            print("Exiting game...")
            break
