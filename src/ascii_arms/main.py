from . import *
import time


def menu_new_save():
    """
    Starts a new game by prompting for a player name and initializing base stats and items.
    """
    update()
    print(f"Start New Adventure! 🧙\n\nEnter your name:")
    name = input("> ")

    new_player = deepcopy(players[-1])

    new_player.info["id"] = get_last_entity_id() + 1
    new_player.info["name"] = name
    new_player.spells["1"] = get_spell_id(1)
    new_player.items["armor"] = get_item_id(12)
    new_player.items["boots"] = get_item_id(18)
    new_player.items["weapon"] = get_item_id(4)

    game.player = new_player


def menu_open_save() -> bool:
    """
    Attempts to load a save file based on player input.

    :return: True if a valid profile is loaded, False otherwise.
    """
    update()
    profiles = ""
    index = 1

    for player in players:
        if players[player].info["id"] not in (-1, 0):
            profiles += f"\n{index}) {players[player].info['name']} [lvl.{players[player].info['level']}]"
            index += 1

    print(f"Enter A Existing Profile 📂!" f"\n{profiles}" f"\n\nEnter profile name:")
    name = input("> ")

    # TODO: This return correct but not correct :/
    correct = check_name(name)
    if not correct:
        return False

    for player in players:
        if name == players[player].info["name"]:
            game.player = players[player]
            return True
    return False


def menu_start():
    """
    Displays the starting menu for opening a save or creating a new game.
    """
    failed = False

    while True:
        update()
        print(
            f"=== Welcome To {game.name.upper()} ==="
            "\n🎯 A ASCII-Based Damage Simulation Game Build In Python 🐍"
        )
        print(
            f"\n1. {str_to_length('Open Save File', 20)}📂"
            f"\n2. {str_to_length('Start New Game', 20)}🆕"
        )

        if failed:
            print("\nFailed to load profile...")

        choice = input("> ")

        if choice == "1":
            found_save = menu_open_save()
            if found_save:
                break
            else:
                failed = True
        elif choice == "2":
            menu_new_save()
            break
        else:
            failed = True
            update()


def load_game():
    """
    Animates a loading screen and enters the main game loop for the loaded player.
    """
    rows = 20

    if game.player.info["id"] != 0:
        r = "■" * rows
        tot = 100
        percent = tot / rows

        while len(r) > 0:
            update()
            print(f"Entering game as {game.player.info['name']}!\n")
            print(check_name(game.player.info["name"]))
            if tot > 66:
                print(f"🔄 {tot}% {green(r)}")
            elif tot > 33:
                print(f"🔄 {tot}% {yellow(r)}")
            else:
                print(f"🔄 {tot}% {red(r)}")

            tot -= percent
            r = r[:-1]
            time.sleep(0.1)

    update()
    print("Ready for adventure! ✅")
    input("> Press any key to continue...")
    game.menu()


if __name__ == "__main__":
    while True:
        load_items()
        load_spells()
        load_entities()

        menu_start()
        load_game()
        game.player = None
