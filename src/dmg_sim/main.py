from . import *
import time


def menu_new_save():
    """ """
    update()
    print("Start New Adventure! 🧙\n\nEnter your name:")
    name = input("> ")

    base_stats["info"]["id"] = get_last_entity_id() + 1
    base_stats["info"]["name"] = name
    base_stats["spells"]["1"] = get_spell_id(1)
    base_stats["items"]["armor"] = get_item_id(12)
    base_stats["items"]["boots"] = get_item_id(18)
    base_stats["items"]["weapon"] = get_item_id(4)

    player = Player(**base_stats)
    print(player.xp)
    game.player = player


def menu_open_save() -> bool:
    """

    :return:
    """
    update()

    json_path = os.path.join(project_root, "database", "entities.json")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    profiles = ""

    for player in data["player"]:
        if player["info"]["id"] != 0:
            profiles += f"\n({player['info']['level']}) {player['info']['name']}"

    print(f"Enter A Existing Profile 📂!" f"\n{profiles}" f"\n\nEnter profile name:")
    name = input("> ")

    for player in data["player"]:
        if name == player["info"]["name"]:
            player = load_player(player["info"]["id"])
            game.player = player
            return True

    return False


def menu_start():
    """ """
    failed = False

    while True:
        update()
        print(
            "=== WELCOME TO DMG SIM ==="
            "\n🎯 A Damage Simulation Game Build In Python 🐍"
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
    """ """
    rows = 20

    if game.player.info["id"] != 0:
        r = "■" * rows
        tot = 100
        percent = tot / rows

        while len(r) > 0:
            update()
            print(f"Entering game as {game.player.info['name']}!\n")

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
    load_items()
    load_spells()
    load_enemies()

    while True:
        menu_start()
        load_game()
        game.player = None
