import json
import os
from typing import cast

from rich.console import Console

console = Console()

type JSON = dict[str, JSON] | list[JSON] | str | int | float | bool | None

NMAP_CONFIGURATION_FILE = "./nmap.json"
NMAP_LASTKNOWNGOOD_FILE = "./nmap.lastknowngood.json"


def load_json(path: str) -> JSON:
    if not os.path.isfile(path):
        return None

    with open(path, encoding="utf-8") as file:
        return cast(JSON, json.load(file))

def is_config_file_valid(config: JSON) -> bool:
    if not isinstance(config, dict):
        return False

    if "target" not in config:
        config["target"] = []

    if "flags" not in config:
        config["flags"] = []

    return True

def load_and_check_config_file():
    config_file = load_json(NMAP_CONFIGURATION_FILE)

    if config_file is not None:
        console.print("[[cyan]i[/]] User configuration file loaded")
        if is_config_file_valid(config_file):
            console.print("[[cyan]i[/]] User configuration file valid")
            return config_file
        else:
            console.print("[[orang3]~[/]] User configuration file not valid")
    else:
        console.print("[[orang3]~[/]] User configuration file not found")

    config_file = load_json(NMAP_LASTKNOWNGOOD_FILE)
    
    if config_file is not None:
        console.print("[[cyan]i[/]] Last known good configuration file loaded")
        if is_config_file_valid(config_file):
            console.print("[[cyan]i[/]] Last known good configuration file valid")
            return config_file
        else:
            console.print("[[red bold]![/]] No configuration valid")
            exit(1)
    else:
        console.print("[[red bold]![/]] No configuration file found")
        exit(1)

if __name__ == "__main__":
    #* Datenzugriff auf der Configurationsfile
    config_file = load_and_check_config_file()
