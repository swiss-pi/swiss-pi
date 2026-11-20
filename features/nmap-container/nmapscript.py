import json
import os
import ipaddress
from typing import TypeIs, TypedDict, cast
from enum import Enum

from rich.console import Console

console = Console()

type JSON = dict[str, JSON] | list[JSON] | str | int | float | bool | None

class SanitizedConfig(TypedDict):
    target: list[str]
    flags: list[str]
    timeout:int
    scan:bool

NMAP_CONFIGURATION_FILE = "./nmap.json"
NMAP_LASTKNOWNGOOD_FILE = "./nmap.lastknowngood.json"
APPROVED_FLAGS = [
    "-T0",
    "-T1",
    "-T2",
    "-T3",
    "-T4",
    "-T5",
    "-A",
    "-v",
    "-vv",
    "-vvv",
    "-sS",
    "-sU",
    "-p",  # here follows a number 
    "-p-",
    "-Pn",
    "-sn",
    "-F",
    "-sV",
    "-O",
    "--version-light",
    "--traceroute",
]

class DEFAULT_SCANS(Enum):
    NO_DEFAULT = 0
    INTENSE = 1
    INTENSE_AND_UDP = 2
    INTENSE_ALL_TCP = 3
    PING_SCAN = 4
    QUICK = 5
    QUICK_PLUS = 6
    QUICK_TRACERROUTE = 7
    REGULAR = 8

DEFAULT_TIMEOUT: dict[DEFAULT_SCANS, int] = {
    DEFAULT_SCANS.INTENSE: 300,
    DEFAULT_SCANS.INTENSE_AND_UDP: 2700,
    DEFAULT_SCANS.INTENSE_ALL_TCP: 1200,
    DEFAULT_SCANS.PING_SCAN: 5,
    DEFAULT_SCANS.QUICK: 20,
    DEFAULT_SCANS.QUICK_PLUS: 90,
    DEFAULT_SCANS.QUICK_TRACERROUTE: 5,
    DEFAULT_SCANS.REGULAR: 120,
}

#* __________ Accessing Configurationfiles __________
def load_json(path: str) -> JSON:
    if not os.path.isfile(path):
        return None

    with open(path, encoding="utf-8") as file:
        return cast(JSON, json.load(file))

def is_config_file_valid(config: JSON) -> TypeIs[dict[str, JSON]]:
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
            console.print("[[orange3]~[/]] [orange3] FAILURE: User configuration file not valid [/]")
    else:
        console.print("[[orange3]~[/]] [orange3] FAILURE: User configuration file not found [/]")

    config_file = load_json(NMAP_LASTKNOWNGOOD_FILE)
    
    if config_file is not None:
        console.print("[[cyan]i[/]] Last known good configuration file loaded")
        if is_config_file_valid(config_file):
            console.print("[[cyan]i[/]] Last known good configuration file valid")
            return config_file
        else:
            console.print("[[red bold]![/]] [red] ERROR: No configuration valid [/]")
            exit(1)
    else:
        console.print("[[red bold]![/]] [red] ERROR: No configuration file found [/]")
        exit(1)

def sanitize_json(json_file:dict[str, JSON]) -> SanitizedConfig:
    timeout = json_file.get("timeout")
    scan = json_file.get("scan")

    return {
        "target": approve_targets(json_file["target"]),
        "flags": approve_flags(json_file["flags"]),
        "timeout": timeout if type(timeout) is int else -1,
        "scan": scan if type(scan) is bool else False,
    }

def approve_targets(target_list:JSON)-> list[str]:
    approved_target_list :list[str]= []
    if not isinstance(target_list, list): return approved_target_list

    for target in target_list:
        if not isinstance(target, str): continue

        #if starting with a dash: reject immediately
        if target[0] is "-":
            continue

        #Check if its an IP Adress
        try:
            _ = ipaddress.ip_address(target)
            approved_target_list.append(target)
            continue
        except: 
            # Check if its a subnet
            try:
                _ = ipaddress.ip_network(target, False)
                approved_target_list.append(target)
                continue
            except ValueError:
                console.print("[white]-[/]] skipped ", target, " is not a valid target")
                continue


        
    return approved_target_list


def approve_flags(flag_list:JSON)-> list[str]:
    approved_flag_list:list[str] = []
    if isinstance(flag_list, list):
        for flag in flag_list:
            if flag in APPROVED_FLAGS:
                approved_flag_list.append(flag)
    return approved_flag_list



#*__________ Preparing for Scan __________ 
def set_timeout(user_timeout:int, default_scan:DEFAULT_SCANS)-> int:
    #-1 means the user did not implement a custom timeout
    if user_timeout <= 0:
        if default_scan != DEFAULT_SCANS.NO_DEFAULT:
            return DEFAULT_TIMEOUT[default_scan]
        else:
            console.print("[[orange3 bold]![/]] [yellow] WARNING: No timeout set. Timeout will be infinite [/] ") 
            return -1 # -1 meaning there is no timeout
    else:
        if default_scan != DEFAULT_SCANS.NO_DEFAULT:
            if user_timeout < DEFAULT_TIMEOUT[default_scan] - 10000 or user_timeout > DEFAULT_TIMEOUT[default_scan] + 10000:
                console.print("[[orange3]~[/] WARNING: Set user Timeout is not in recommended range.")
        
        return user_timeout

#* __________ Scanning __________
def scan():
    return

            
if __name__ == "__main__":
    #* Accessing configurationfiles
    config_file = load_and_check_config_file()
    sanitized_config_file = sanitize_json(config_file)
    console.print(sanitized_config_file)
    #* Preparing for scan
    timeout = set_timeout(sanitized_config_file["timeout"], DEFAULT_SCANS.NO_DEFAULT)

    #* Scan
    scan()