from item_manager import *
from spell_manager import *
from entity_manager import *
from launcher import *
import game as Game
import time


def set_starter_inventory(player):
    player.add_item(get_item_name("Necklace"))
    player.add_item(get_item_name("Leather set"))
    player.add_item(get_item_name("Set of shoes"))
    player.add_item(get_item_name("Short sword"))
    player.spells["Slot 1"] = get_spell_id(1)


def new_save():
    update()
    print("Start New Adventure!\n\n🧙‍♂️ Enter your name:")
    name = input("> ")

    player = Player(name)

    set_starter_inventory(player)
    Game.player = player


# TODO: Open and load from a save file
def open_save():
    """
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename()

    data = Game
    """
    print("\n1. 📂 Open Save File" "\n2. 🧙‍♂️ Start New Game")
    player = load_player(0)

    set_starter_inventory(player)
    Game.player = player


def select_save():
    print("\n1. 📂 Open Save File" "\n2. 👶 Start New Game")

    while True:
        choice = input("> ")

        if choice == "1":
            open_save()
            break
        elif choice == "2":
            new_save()
            break


def load_game():
    if Game.player.info["name"] != "TEST.BOT":
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


def start_screen():
    print("⚔️ WELCOME TO DMG SIM 🛡️" "\n🎯 A Damage Simulation Game Build in Python 🐍")

    load_items()
    load_spells()
    load_enemies()

    select_save()
    load_game()


start_screen()
