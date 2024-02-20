import modules.RequestHandler as RequestHandler
import modules.systemInfo as SystemInfo

agent = None
token = None
ships = None
activeShip = None

def prepAgent() -> None:
    global agent
    global token
    
    with open("secrets", "r") as secrets:
        agent = secrets.readline().strip()
        token = secrets.readline().strip()

    if token != '':
        RequestHandler.headers = {
            "Authorization": "Bearer " + token
        }
    else:
        token = None


def register(name, faction) -> str:
    global token
    global agent

    json_data = {
        "symbol": name,
        "faction": faction
    }

    response_json = RequestHandler.postNoAuth("https://api.spacetraders.io/v2/register", json_data)

    agent = response_json["data"]["agent"]["symbol"]
    token = response_json['data']['token']

    RequestHandler.headers = {
                "Authorization": "Bearer " + token
            }
    
    with open("secrets", "a") as secrets:
        secrets.write(agent + "\n")
        secrets.write(token)

    return response_json


def viewAgent() -> str:
    response = RequestHandler.get("https://api.spacetraders.io/v2/my/agent")
    SystemInfo.waypoint = response["data"]["headquarters"]
    SystemInfo.setSystem()

    return response

def viewShips() -> str:
    response = RequestHandler.get("https://api.spacetraders.io/v2/my/ships")

    ships = response["data"]

    reducedShips = []
    for ship in ships:
        reducedShips.append(ship["registration"])

    return reducedShips