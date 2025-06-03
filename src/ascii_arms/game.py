from . import *

game_name = "ASCII Arms"
player = None


def menu_combat(enemy):
    """ """
    print(enemy)


def menu_combat_options():
    """ """
    if player.check_requirement():
        boss_desc = yellow(f"<<< boss available!")
    else:
        boss_desc = dim(f"[{player.kills['slain']}/4]")

    while True:
        update()
        print(
            f"⚔️ Combat Options"
            f"\nTotal: {player.kills['enemies']}\tBosses: {player.kills['bosses']}"
            f"\n\n1. {str_to_length('Normal Fight', 20)}🥊"
            f"\n2. {str_to_length('Boss Encounter', 20)}👹 {boss_desc}"
            f"\n\n3. {str_to_length('Back', 20)}🔙"
        )

        choice = input("> ")

        if choice == "1":
            menu_combat(find_enemy(player.info["level"], False))
            break
        elif choice == "2":
            if player.check_requirement():
                player.slain = 0
                menu_combat(find_enemy(player.info["level"], True))
                break
        elif choice == "3":
            break


def menu_character():
    """ """
    while True:
        update()

        print(
            f"{"CHARACTER".upper()}"
            f"\n\n{player.get_stats()}"
            f"\n\n1. {str_to_length('Inventory', 20)}💰"
            f"\n2. {str_to_length('Spellbook', 20)}🔮"
            f"\n\n3. {str_to_length('Back', 20)}🔙"
        )

        choice = input("> ")

        if choice == "1":
            menu_items()
        elif choice == "2":
            menu_spells()
        elif choice == "3":
            break


def menu_items():
    """ """
    while True:
        update()
        print(
            f"{"Inventory".upper()}"
            f"\n\n{player.get_items()}"
            f"\n\n3. {str_to_length('Back', 20)}🔙"
        )

        choice = input("> ")

        if choice == "3":
            break


def menu_spells():
    """ """
    while True:
        update()
        print(
            f"{"Spellbook".upper()}"
            f"\n\n{player.get_spells()}"
            f"\n\n3. {str_to_length('Back', 20)}🔙"
        )
        choice = input("> ")

        if choice == "3":
            break


def menu_save():
    """ """
    update()
    print("Saving Progress... 💾")
    save_player(player)
    print("Game saved successfully! ✅")
    input("> Press any key to continue...")


def menu():
    """ """
    while True:
        update()
        print(
            f"=== {game_name.upper()} ==="
            f"\nName: {player.info['name']} {player.info['icon']}"
            f"\nLevel: {player.info['level']}"
            f"\n{player.get_xp_bar()}"
            f"\n\n1. {str_to_length('Enter Battle', 20)}⚔️"
            f"\n2. {str_to_length('Character Info', 20)}🧙"
            f"\n3. {str_to_length('Save Progress', 20)}💾"
            f"\n\n4. {str_to_length('Quit', 20)}🚪"
        )

        print(player.kills)
        choice = input("> ")

        if choice == "1":
            menu_combat_options()
        elif choice == "2":
            menu_character()
        elif choice == "3":
            menu_save()
        elif choice == "4":
            print("Exiting game...")
            break
