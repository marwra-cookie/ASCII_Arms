from tabulate import tabulate
from src.gear_manager import *


class Gear:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        stats = self.__dict__
        added = ""

        for stat in stats:
            match stat:
                case "attackPower":
                    added += f" {red(stats.get("attackPower", ""))}"
                case "spellPower":
                    added += f" {bright(magenta(stats.get("spellPower", "")))}"
                case "healingPower":
                    added += f" {bright(green(stats.get("healingPower", "")))}"
                case "criticalChance":
                    exist = f" {stats.get("criticalChance", None)}"
                    if exist:
                        added += f" {bright(red(f"{int(exist * 100)}")) + "%"}"
                case "criticalDamage":
                    exist = stats.get("criticalDamage", None)
                    if exist:
                        added += f" {bright(red(f"{int(exist * 100)}")) + "%"}"
                case "armorPenetration":
                    exist = stats.get("armorPenetration", None)
                    if exist:
                        added += f" {dim(red(f"{int(exist * 100)}")) + "%"}"
                case "spellPenetration":
                    exist = stats.get("spellPenetration", None)
                    if exist:
                        added += f" {dim(blue(f"{int(exist * 100)}")) + "%"}"
                case "health":
                    added += f" {green(stats.get("health", ""))}"
                case "defense":
                    added += f"{bright(yellow(stats.get("defense", "")))}"
                case "resistance":
                    added += f" {bright(cyan(stats.get("resistance", "")))}"
                case "parry":
                    exist = stats.get("parry", None)
                    if exist:
                        added += f" {int(exist * 100)}" + "%"
                case "dodge":
                    exist = stats.get("dodge", None)
                    if exist:
                        added += f" {int(exist * 100)}" + "%"
                case "regeneration":
                    exist = stats.get("regeneration", None)
                    if exist:
                        added += magenta(f" {int(exist * 100)}") + "%"
                case "energy":
                    added += f" {yellow(stats.get("energy", ""))}"
                case "momentum":
                    added += f" {str(stats.get("momentum", ""))}"

        msg = f"({stats["level"]})\t{stats["name"]}\t\t" + added

        return msg
