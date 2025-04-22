import os
from src.entities.player import Player
import time
from src.game import Game
from launcher import rows
from gear_manager import *


def testbench():
    debug = create_gear("helm", 1)

    print(red(f"\n\nDEBUG:"))
    print(f"{debug}")


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


def start_screen():
    print("--- WELCOME TO DMG SIM ---" "\nA damage simulation game in Python")

    load_gear()
    load_spells()
    save = select_save()
    save.player.gear["accessory"] = get_gear("Necklace")
    save.player.gear["armor"] = get_gear("Leather set")
    save.player.gear["boots"] = get_gear("Half a set of shoes")
    save.player.gear["weapon"] = get_gear("Short sword")
    save.player.spells[0] = get_spell("Strike")
    start_game(save)


start_screen()
