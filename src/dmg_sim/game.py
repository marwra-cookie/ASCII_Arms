from . import *

player = None
boss_requirement = 4


def menu_combat():

    if player.info["slain"] >= boss_requirement:
        boss_desc = yellow(f"<<< boss available!")
    else:
        boss_desc = dim(f"\n(requires {4 - player.info["slain"]} more kills)")

    while True:
        update()
        print(
            f"⚔️ Combat Options"
            f"\n\n1. Normal Encounter 🥊"
            f"\n2. Start A Boss Encounter [{player.info["slain"]}/4] 👹 {boss_desc}"
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
            f"\n\n1. Inventory 💰"
            f"\n2. Spellbook 🔮"
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
        print(f"Inventory 💰" f"\n\n{player.get_items()}" f"\n\n3. 🔙 Back")

        choice = input("> ")

        if choice == "3":
            break


def menu_spells():
    while True:
        update()
        print(f"Spellbook 🔮" f"\n\n{player.get_spells()}" f"\n\n3. 🔙 Back")
        choice = input("> ")

        if choice == "3":
            break


def menu_save():
    update()
    print("Saving Progress... 💾")
    save_player(player)
    print("Game saved successfully! ✅")
    input("> Press any key to continue...")


def menu():
    while True:
        update()
        print(
            f"=== PLAYER INFO ==="
            f"\nName: {player.info["name"]} {player.info["icon"]}"
            f"\nLevel: {player.info["level"]}"
            f"\n\n1. Enter Battle ⚔️"
            f"\n2. Character Info 🧙"
            f"\n3. Save Progress 💾"
            f"\n\n4. Quit 🚪"
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
