from item_manager import *
from spell_manager import *
from launcher import *
import game as Game
import time


def new_save():
    update()
    print("CREATING NEW GAME" "\n\nEnter your player name:")
    name = input("> ")

    player = Player(name)

    player.add_item(get_item_name("Necklace"))
    player.add_item(get_item_name("Leather set"))
    player.add_item(get_item_name("Set of shoes"))
    player.add_item(get_item_name("Short sword"))
    player.spells[0] = get_spell_id(1)

    Game.player = player


# TODO: Open and load from a save file
def open_save():
    """
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename()

    data = Game
    """

    player = Player("Test")

    player.add_item(get_item_name("Necklace"))
    player.add_item(get_item_name("Leather set"))
    player.add_item(get_item_name("Set of shoes"))
    player.add_item(get_item_name("Short sword"))
    player.spells[0] = get_spell_id(1)

    Game.player = player


def select_save():
    print("\n1. Open save file" "\n2. New game")

    while True:
        choice = input("> ")

        if choice == "1":
            open_save()
            break
        elif choice == "2":
            new_save()
            break


def load_game():
    if Game.player.name != "Test":
        r = "■" * rows
        tot = 100
        percent = tot / rows

        while len(r) > 0:
            update()
            print(f"Entering game as {Game.player.name}!\n")
            print(f"{tot}% {r}")
            tot -= percent
            r = r[:-1]
            time.sleep(0.1)

    update()
    input("> Press any key to continue...")
    Game.menu()


def start_screen():
    print("--- WELCOME TO DMG SIM ---" "\nA damage simulation game in Python")

    load_items()
    load_spells()

    select_save()
    load_game()


start_screen()
