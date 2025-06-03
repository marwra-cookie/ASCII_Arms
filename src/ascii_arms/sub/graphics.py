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

error = "Invalid option... Please try again!"


def str_to_color(msg, color) -> str:
    """

    :param str:
    :return:
    """
    match color:
        case "white":
            return white(msg)
        case "red":
            return red(msg)
        case "green":
            return green(msg)
        case "yellow":
            return yellow(msg)
        case "blue":
            return blue(msg)
        case "magenta":
            return magenta(msg)
        case "cyan":
            return cyan(msg)
        case "fill_cyan":
            return fill_cyan(msg)
        case "fill_red":
            return fill_red(msg)
        case "fill_green":
            return fill_green(msg)
        case "fill_yellow":
            return fill_yellow(msg)
        case "fill_blue":
            return fill_blue(msg)
        case "fill_magenta":
            return fill_magenta(msg)
        case "fill_cyan":
            return fill_cyan(msg)
        case "dim":
            return dim(msg)
        case "bright":
            return bright(msg)
    return None


def white(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.WHITE + f"{msg}" + Fore.RESET


def red(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.RED + f"{msg}" + Fore.RESET


def green(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.GREEN + f"{msg}" + Fore.RESET


def yellow(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.YELLOW + f"{msg}" + Fore.RESET


def blue(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.BLUE + f"{msg}" + Fore.RESET


def magenta(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.MAGENTA + f"{msg}" + Fore.RESET


def cyan(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Fore.CYAN + f"{msg}" + Fore.RESET


def fill_cyan(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.CYAN + f"{msg}" + Back.RESET


def fill_red(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.RED + f"{msg}" + Back.RESET


def fill_green(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.GREEN + f"{msg}" + Back.RESET


def fill_yellow(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.YELLOW + f"{msg}" + Back.RESET


def fill_blue(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.BLUE + f"{msg}" + Back.RESET


def fill_magenta(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.MAGENTA + f"{msg}" + Back.RESET


def fill_cyan(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Back.CYAN + f"{msg}" + Back.RESET


def dim(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Style.DIM + f"{msg}" + Style.RESET_ALL


def bright(msg) -> str:
    """

    :param msg:
    :return:
    """
    return Style.BRIGHT + f"{msg}" + Style.RESET_ALL


init(convert=True)
