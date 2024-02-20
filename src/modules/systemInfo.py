import modules.RequestHandler as RequestHandler
import modules.console as Console
import modules.ship as Ship
import inquirer

waypoint = None
system = None
locationWaypoints = None
inOrbit = False

console = Console.console

def viewCurrentLocation() -> str:
    return RequestHandler.get("https://api.spacetraders.io/v2/systems/" + system[0] + "-" + system[1] + "/waypoints/" + waypoint)

def setSystem() -> None:
    global system
    system = waypoint.split("-")

def locate(trait: str, type) -> str:
        global locationWaypoints

        response = RequestHandler.get("https://api.spacetraders.io/v2/systems/" + system[0] + "-" + system[1] + "/waypoints?" + type + "=" + trait.upper())

        locationWaypoints = response["data"]

        return response

def viewLocations(trait: str) -> None: 
     numerOfLocations = len(locationWaypoints)
     currentNum = 1
     for location in locationWaypoints:
        console.print("%s of %s" % (currentNum, numerOfLocations))

        response = RequestHandler.get("https://api.spacetraders.io/v2/systems/" + system[0] + "-" + system[1] + "/waypoints/" + location["symbol"] + "/" + trait.upper())
    
        if trait == "shipyard":
             Ship.viewShips(response)

        next = {
            inquirer.List('option',
                        message = "Choose Option:",
                        choices = ["Continue", "Quit"]
                        )
        }

        if currentNum == numerOfLocations:
            break
        
        chosenOption = inquirer.prompt(next)
        currentNum += 1

        if chosenOption['option'] == "Quit":
            break

def navigateToLastWaypoint(activeShip) -> str:
     json_data = {
          "waypointSymbol": locationWaypoints[0]["symbol"]
     }

     if not inOrbit:
        console.print_json(data=orbit(activeShip))



     return RequestHandler.postWithData("https://api.spacetraders.io/v2/my/ships/" + activeShip["name"] + "/navigate", json_data)

def orbit(activeShip) -> str:
     global inOrbit
     inOrbit = True

     return RequestHandler.post("https://api.spacetraders.io/v2/my/ships/" + activeShip["name"] + "/orbit")
