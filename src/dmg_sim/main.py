from . import *
from .launcher import project_root
import time


def menu_new_save():
    update()
    print("Start New Adventure! 🧙‍♂️\n\nEnter your name:")
    name = input("> ")

    player_stats = base_stats

    player_stats["info"]["name"] = name
    player_stats["info"]["id"] = get_last_entity_id() + 1
    player_stats["spells"]["Slot 1"] = get_spell_id(1)
    player_stats["items"]["accessory"] = get_item_id(1)
    player_stats["items"]["armor"] = get_item_id(3)
    player_stats["items"]["boots"] = get_item_id(6)
    player_stats["items"]["weapon"] = get_item_id(10)
    player = Player(**player_stats)

    game.player = player


def menu_open_save() -> bool:
    update()

    json_path = os.path.join(project_root, "database", "entities.json")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    profiles = ""

    for player in data["player"]:
        if player["info"]["id"] != 0:
            profiles += f"\n({player["info"]["level"]}) {player["info"]["name"]}"

    print(f"Enter A Existing Profile 📂!" f"\n{profiles}" f"\n\nEnter profile name:")
    name = input("> ")

    for player in data["player"]:
        if name == player["info"]["name"]:
            player = load_player(player["info"]["id"])
            game.player = player
            return True

    return False


def menu_start():
    failed = False

    while True:
        update()
        print(
            "=== WELCOME TO DMG SIM ==="
            "\n🎯 A Damage Simulation Game Build in Python 🐍"
        )
        print("\n1. Open Save File 📂" "\n2. Start New Game 🆕")

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


def load_game():
    rows = 20

    if game.player.info["id"] != 0:
        r = "■" * rows
        tot = 100
        percent = tot / rows

        while len(r) > 0:
            update()
            print(f"Entering game as {game.player.info["name"]}!\n")
            print(f"🔄 {tot}% {r}")
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

    menu_start()

    load_game()
