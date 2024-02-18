import requests
from rich.console import Console

console = Console()

if __name__ == '__main__':
   # response = requests.get("https://api.spacetraders.io/v2/")
   # console.print_json(data = response.json())
#
   # json_data = {
   #     "symbol": "Groov-One",
   #     "faction": "COSMIC"
   # }
#
   # response = requests.post("https://api.spacetraders.io/v2/register", json = json_data)
   # console.print_json(data=response.json)
    
    secrets = open("secrets", "r")
    headers = {
        "Authorization": "Bearer " + secrets.readline().strip()
    }

    response = requests.get("https://api.spacetraders.io/v2/my/agent", headers=headers)
    console.print_json(data=response.json())