import os
from rich.console import Console
console = Console()

NMAP_CONFIGURATION_FILE="./nmap.json"
NMAP_LASTKNOWNGOOD_FILE="./nmap.lastknowngood.json"

files_not_found = 0
if not os.path.isfile(NMAP_CONFIGURATION_FILE):
    console.print("[[orange3 bold]![/]] NMAP configuration file not found")
    files_not_found += 1
else:
    console.print("[[blue]i[/]] NMAP configuration file found")

if not os.path.isfile(NMAP_LASTKNOWNGOOD_FILE):
    console.print("[[orange3]-[/]] NMAP last known good not found")
    files_not_found += 1
else:
    console.print("[[blue]i[/]] NMAP last known good file found")

if files_not_found == 2:
    console.print("[[red bold]X[/]] FATAL: NO CONFIG FILES FOUND EXITING WITH CODE 1")
    exit(1)
