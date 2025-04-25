import time
from launcher import rows
from game import *
from item_manager import *
from spell_manager import *


def testbench():
    # debug = create_item("helm", 1)

    print(red(f"\n\nDEBUG:"))
    # print(f"{debug}")


def new_save() -> Game:
    os.system("cls")
    print("CREATING NEW GAME" "\n\nEnter your player name:")
    name = input("> ")

    player = Player(name)

    save = Game(player)

    return save


# TODO: Open and load save file
def open_save() -> Game:
    """
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename()

    data = Game
    """

    player = Player("Test")
    data = Game(player)

    return data


def select_save() -> Game:
    print("\n1. Open save file" "\n2. New game")

    testbench()

    while True:
        choice = input("> ")

        if choice == "1":
            save = open_save()
            break
        elif choice == "2":
            save = new_save()
            break
        else:
            print("Invalid option... Please try again!")

    return save


def start_game(save):
    if save.player.name != "Test":
        r = "■" * rows
        tot = 100
        percent = tot / rows

        while len(r) > 0:
            os.system("cls")
            print(f"Entering game as {save.player.name}!\n")
            print(f"{tot}% {r}")
            tot -= percent
            r = r[:-1]
            time.sleep(0.1)

    os.system("cls")
    input("> Press any key to continue...")
    save.run()


def set_starter_items(save):
    save.player.add_item(get_item_name("Necklace"))
    save.player.add_item(get_item_name("Leather set"))
    save.player.add_item(get_item_name("Set of shoes"))
    save.player.add_item(get_item_name("Short sword"))
    save.player.spells[0] = get_spell_id(1)


def start_screen():
    print("--- WELCOME TO DMG SIM ---" "\nA damage simulation game in Python")

    load_items()
    load_spells()

    save = select_save()
    set_starter_items(save)

    start_game(save)


start_screen()
