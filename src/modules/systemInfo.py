import modules.RequestHandler as RequestHandler
import modules.console as Console
import inquirer

waypoint = None
system = None
locationWaypoints = None

console = Console.console

def viewCurrentLocation() -> str:
    return RequestHandler.get("https://api.spacetraders.io/v2/systems/" + system[0] + "-" + system[1] + "/waypoints/" + waypoint)

def setSystem() -> None:
    global system
    system = waypoint.split("-")

def locate(trait: str) -> str:
        global locationWaypoints

        response = RequestHandler.get("https://api.spacetraders.io/v2/systems/" + system[0] + "-" + system[1] + "/waypoints?traits=" + trait.upper())

        locationWaypoints = response["data"]

        return response

def viewLocations(trait: str, dataType: str) -> None:
     
     numerOfLocations = len(locationWaypoints)
     currentNum = 1
     for location in locationWaypoints:
        console.print("%s of %s" % (currentNum, numerOfLocations))


        response = RequestHandler.get("https://api.spacetraders.io/v2/systems/" + system[0] + "-" + system[1] + "/waypoints/" + location["symbol"] + "/" + trait.upper())
        
        requestedWaypoint = response["data"]["symbol"]
        requestedData = response["data"][dataType]
        
        console.print("Waypoint: %s" % (requestedWaypoint))
        console.print_json(data=requestedData)
        
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