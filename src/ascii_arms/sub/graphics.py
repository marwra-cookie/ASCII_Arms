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


# region Fore
def white(msg) -> str:
    """
    Wraps the input string in white text.

    :param msg: Message to format.
    :return: White-colored string.
    """
    return Fore.WHITE + f"{msg}" + Fore.RESET


def red(msg) -> str:
    """
    Wraps the input string in red text.

    :param msg: Message to format.
    :return: Red-colored string.
    """
    return Fore.RED + f"{msg}" + Fore.RESET


def green(msg) -> str:
    """
    Wraps the input string in green text.

    :param msg: Message to format.
    :return: Green-colored string.
    """
    return Fore.GREEN + f"{msg}" + Fore.RESET


def yellow(msg) -> str:
    """
    Wraps the input string in yellow text.

    :param msg: Message to format.
    :return: Yellow-colored string.
    """
    return Fore.YELLOW + f"{msg}" + Fore.RESET


def blue(msg) -> str:
    """
    Wraps the input string in blue text.

    :param msg: Message to format.
    :return: Blue-colored string.
    """
    return Fore.BLUE + f"{msg}" + Fore.RESET


def magenta(msg) -> str:
    """
    Wraps the input string in magenta text.

    :param msg: Message to format.
    :return: Magenta-colored string.
    """
    return Fore.MAGENTA + f"{msg}" + Fore.RESET


def cyan(msg) -> str:
    """
    Wraps the input string in cyan text.

    :param msg: Message to format.
    :return: Cyan-colored string.
    """
    return Fore.CYAN + f"{msg}" + Fore.RESET


# endregion


# region Back
def fill_red(msg) -> str:
    """
    Applies a red background to the message.

    :param msg: Message to format.
    :return: String with red background.
    """

    return Back.RED + f"{msg}" + Back.RESET


def fill_green(msg) -> str:
    """
    Applies a green background to the message.

    :param msg: Message to format.
    :return: String with green background.
    """

    return Back.GREEN + f"{msg}" + Back.RESET


def fill_yellow(msg) -> str:
    """
    Applies a yellow background to the message.

    :param msg: Message to format.
    :return: String with yellow background.
    """

    return Back.YELLOW + f"{msg}" + Back.RESET


def fill_blue(msg) -> str:
    """
    Applies a blue background to the message.

    :param msg: Message to format.
    :return: String with blue background.
    """

    return Back.BLUE + f"{msg}" + Back.RESET


def fill_magenta(msg) -> str:
    """
    Applies a magenta background to the message.

    :param msg: Message to format.
    :return: String with magenta background.
    """

    return Back.MAGENTA + f"{msg}" + Back.RESET


def fill_cyan(msg) -> str:
    """
    Applies a cyan background to the message.

    :param msg: Message to format.
    :return: String with cyan background.
    """

    return Back.CYAN + f"{msg}" + Back.RESET


# endregion


# region Style
def dim(msg) -> str:
    """
    Applies dim style to the message.

    :param msg: Message to format.
    :return: Dim-styled string.
    """

    return Style.DIM + f"{msg}" + Style.RESET_ALL


def bright(msg) -> str:
    """
    Applies bright style to the message.

    :param msg: Message to format.
    :return: Bright-styled string.
    """

    return Style.BRIGHT + f"{msg}" + Style.RESET_ALL


# endregion

init(convert=True)
