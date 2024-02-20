import modules.console as Console
import modules.RequestHandler as RequestHandler


console = Console.console

shipyardsList = []

def viewShips(response) -> None:
        
    shipyard = {}

    if "symbol" in response["data"]: shipyard["symbol"] = response["data"]["symbol"]
    if "shipTypes" in response["data"]: shipyard["shipTypes"] = response["data"]["shipTypes"]
    if "transactions" in response["data"]: shipyard["transactions"] = response["data"]["transactions"]
    if "ships" in response["data"]: shipyard["ships"] = response["data"]["ships"]
    if "modificationsFee" in response["data"]: shipyard["modificationsFee"] = response["data"]["modificationsFee"]
    
    shipyardsList.append(shipyard)

    briefView = {}

    if "symbol" in shipyard: briefView["symbol"] = shipyard["symbol"]
    if "shipTypes" in shipyard: briefView["shipTypes"] = shipyard["shipTypes"]
    if "ships" in shipyard: 
        shipList = []
        for ship in shipyard["ships"]:
            shipList.append({
                "type": ship["type"],
                "description": ship["description"],
                "purchasePrice": ship["purchasePrice"]
            })
        briefView["ships"] = shipList

    
    console.print_json(data=briefView)


def moreShipDetails(symbol, shipType) -> str:
    return str(list(filter(lambda x: filterShipDetails(x, symbol, shipType))))


def purchaseShip(shipType, set) -> str:

    json_data = {
        "shipType": shipType,
        "waypointSymbol": shipyardsList[int(set) - 1]["symbol"]
    }

    return RequestHandler.postWithData("https://api.spacetraders.io/v2/my/ships", json_data)

    

def filterShipyard(pair) -> dict:
    key, value = pair
    if key == "transactions" or key == "modificationsFee":
        return False
    else:
        return True
     

def filterShipDetails(shipyard, symbol, shipType) -> bool:
    if shipyard["symbol"] == symbol and shipyard["shipType"] == shipType:
        return True
    else:
        return False
    
def dock(activeShip) -> str:
    return RequestHandler.post("https://api.spacetraders.io/v2/my/ships/" + activeShip["name"] + "/dock")

def refuel(activeShip) -> str:
    return RequestHandler.post("https://api.spacetraders.io/v2/my/ships/" + activeShip["name"] + "/refuel")

def extract(activeShip) -> str:
    return RequestHandler.post("https://api.spacetraders.io/v2/my/ships/" + activeShip["name"] + "/extract")