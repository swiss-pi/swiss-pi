import json
import os
from collections.abc import Sequence
from typing import cast

from rich.console import Console

console = Console()

type JSON = dict[str, JSON] | list[JSON] | str | int | float | bool | None

NMAP_CONFIGURATION_FILE = "./nmap.json"
NMAP_LASTKNOWNGOOD_FILE = "./nmap.lastknowngood.json"
COMMAND_INJECTION_BLACKLIST = [";", "&", "|", "$", "(", ")", "`", "'"]

#* Laden und Verifizieren der Dateien
def load_json(path: str) -> JSON:
    if not os.path.isfile(path):
        return None

    with open(path, encoding="utf-8") as file:
        return cast(JSON, json.load(file))

def is_config_file_valid(config: JSON) -> bool:
    if not isinstance(config, dict):
        return False

    if "target" not in config or not isinstance(config["target"], list):
        config["target"] = []

    if "flags" not in config or not isinstance(config["flags"], list):
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

def sanitize_json(json_file:dict[str, Sequence[object]]):
    sanitized_json_file:dict[str,list[str]]= {}
    sanitized_json_file["target"] = approve_output(json_file["target"])
    sanitized_json_file["flags"] = approve_output(json_file["flags"])
    return sanitized_json_file

def approve_output(list_to_validate:Sequence[object]):
    validated_list: list[str] = []
    for item_to_validate in list_to_validate:
        if not isinstance(item_to_validate, str):continue

        item_approved=True
        for blacklisted_char in COMMAND_INJECTION_BLACKLIST:
            if blacklisted_char in item_to_validate:
                item_approved = False
                break
        if item_approved:
            validated_list.append(item_to_validate)

    return validated_list
            
if __name__ == "__main__":
    #* Datenzugriff auf der Configurationsfile
    config_file = load_and_check_config_file()
    sanitized_config_file = sanitize_json(config_file)  # pyright: ignore[reportArgumentType] #? We know it has to be a dic[str, list[str]] because we validated it in load_and_check
    console.print("DEBUG: " , sanitized_config_file)

