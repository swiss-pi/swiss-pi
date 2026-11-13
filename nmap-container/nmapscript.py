import os
from rich.console import Console
console = Console()

NMAP_CONFIGURATION_FILE="./nmap.json"
NMAP_LASTKNOWNGOOD_FILE="./nmap.lastknowngood.json"

if not os.path.isfile(NMAP_CONFIGURATION_FILE):
    console.print("[[red bold]![/]] NMAP configuration file not found")
    