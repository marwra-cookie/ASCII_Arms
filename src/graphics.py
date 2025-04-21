from colorama import Fore, Back, Style, init

"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

Fore: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
Back: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX

from colorama import Fore, Back, Style

Fore.RED + 'some red text' + Fore.Reset
Back.GREEN + 'and with a green background' + Back.Reset
Style.DIM + 'and in dim text' + Style.RESET_ALL
"""


def red(msg) -> str:
    return Fore.RED + f"{msg} " + Fore.RESET


def green(msg) -> str:
    return Fore.GREEN + f"{msg} " + Fore.RESET


def yellow(msg) -> str:
    return Fore.YELLOW + f"{msg} " + Fore.RESET


def blue(msg) -> str:
    return Fore.BLUE + f"{msg} " + Fore.RESET


def magenta(msg) -> str:
    return Fore.MAGENTA + f"{msg} " + Fore.RESET


def cyan(msg) -> str:
    return Fore.CYAN + f"{msg} " + Fore.RESET


def fill_cyan(msg) -> str:
    return Back.CYAN + f"{msg} " + Back.RESET


def fill_red(msg) -> str:
    return Back.RED + f"{msg} " + Back.RESET


def fill_green(msg) -> str:
    return Back.GREEN + f"{msg} " + Back.RESET


def fill_yellow(msg) -> str:
    return Back.YELLOW + f"{msg} " + Back.RESET


def fill_blue(msg) -> str:
    return Back.BLUE + f"{msg} " + Back.RESET


def fill_magenta(msg) -> str:
    return Back.MAGENTA + f"{msg} " + Back.RESET


def fill_cyan(msg) -> str:
    return Back.CYAN + f"{msg} " + Back.RESET


def dim(msg) -> str:
    return Style.DIM + f"{msg} " + Style.RESET_ALL


def bright(msg) -> str:
    return Style.BRIGHT + f"{msg} " + Style.RESET_ALL


init(convert=True)
