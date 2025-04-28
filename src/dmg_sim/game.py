from launcher import update
from entity_manager import *
from sub import *

player = None
slain = 0


def menu_instructions():
    while True:
        update()

        with open(f"database/instructions.txt", "r") as file:
            data = file.read()
            print(f"🦽 Gameplay Instructions 📃" f"\n{data}" f"\n\n3. 🔙 Back")

        choice = input("> ")

        if choice == "3":
            break


def menu_combat():
    while True:
        update()
        print(
            f"⚔️ Combat Options"
            f"\n\n1. 🥊 Normal fight"
            f"\n2. 👹 Boss encounter [{slain}/4]"
            f"\n\n3. 🔙 Back"
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
            f"🧙‍♂️ Character"
            f"\n\n{player.get_stats()}"
            f"\n\n1. 🧰 Inventory"
            f"\n2. 📖 Spellbook"
            f"\n\n3. 🔙 Back"
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
        print(f"🧰 Inventory" f"\n\n{player.get_items()}" f"\n\n3. 🔙 Back")

        choice = input("> ")

        if choice == "3":
            break


def menu_spells():
    while True:
        update()
        print(f"📖 Spellbook" f"\n\n{player.get_spells()}" f"\n\n3. 🔙 Back")
        choice = input("> ")

        if choice == "3":
            break


# TODO: Save game to file
def menu_save():
    update()
    print("💾 Saving Progress...")
    print("✅ Game saved successfully!")


def menu():
    while True:
        update()

        print(
            f"🎖️ {player.info["name"]} | lvl.{player.info["level"]}"
            f"\n\n1. ⚔️ Combat"
            f"\n2. 🧙 Character"
            f"\n3. 💾 Save"
            f"\n4. 🦽 Instructions"
            f"\n\n5. 🚪 Quit"
        )

        choice = input("> ")

        if choice == "1":
            menu_combat()
        elif choice == "2":
            menu_character()
        elif choice == "3":
            menu_save()
        elif choice == "4":
            menu_instructions()
        elif choice == "5":
            print("Exiting game...")
            break
