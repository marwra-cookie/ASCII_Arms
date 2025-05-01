from item_manager import *
from spell_manager import *
from entity_manager import *
from launcher import *
import game as Game
import time


def menu_new_save():
    update()
    print("🧙‍♂️ Start New Adventure!\n\nEnter your name:")
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

    Game.player = player


def menu_open_save():
    update()

    with open(f"database/entities.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    profiles = ""

    for player in data["player"]:
        if player["info"]["id"] != 0:
            profiles += f"\n({player["info"]["level"]}) {player["info"]["name"]}"

    print(
        f"📂 Open A Saved Profile!"
        f"\n{profiles}"
        f"\n3. 🔙 Back"
        f"\nEnter profile name:"
    )
    name = input("> ")

    if name != "3":
        for player in data["player"]:
            if name == player["info"]["name"]:
                player = load_player(player["info"]["id"])
                Game.player = player


def menu_start():
    run = False
    while True:
        update()
        print(
            "⚔️ WELCOME TO DMG SIM 🛡️" "\n🎯 A Damage Simulation Game Build in Python 🐍"
        )
        print("\n1. 📂 Open Save File" "\n2. 👶 Start New Game")
        if Game.player is None and run:
            print("\nFailed to load profile...")
        elif Game.player is not None and run:
            break
        choice = input("> ")

        if choice == "1":
            menu_open_save()
            run = True
        elif choice == "2":
            menu_new_save()
            break


def load_game():
    if Game.player.info["id"] != 0:
        r = "■" * rows
        tot = 100
        percent = tot / rows

        while len(r) > 0:
            update()
            print(f"Entering game as {Game.player.info["name"]}!\n")
            print(f"🔄 {tot}% {r}")
            tot -= percent
            r = r[:-1]
            time.sleep(0.1)

    update()
    print("✅ Ready for adventure!")
    input("> Press any key to continue...")
    Game.menu()


def start():
    load_items()
    load_spells()
    load_enemies()

    menu_start()

    load_game()


start()
