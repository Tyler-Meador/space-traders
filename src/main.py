import modules.console as Console
import modules.Agent as Agent
from enums.Factions import Factions
import modules.contracts as Contracts
import modules.systemInfo as SystemInfo
import modules.ship as Ship
import inquirer
import time

console = Console.console

if __name__ == '__main__':

   isLogined = False
   optionItems = ["exit", "view agent", "view contract", "current location", "locate shipyard", "my ships", "locate engineered asteroid"]
   loginItems = [""]

   login = {
      inquirer.List('option',
                    message = "Choose Option:",
                    choices = loginItems
                  )
   }

   options = {
      inquirer.List('option',
                    message = "Choose Option:",
                    choices = optionItems,
                    carousel = True
                  )
   }

   register = [
      inquirer.Text('name', message="Agent's Name"),
      inquirer.List('faction',
                        message = "Choose Faction",
                        choices = Factions._member_names_
                     )

   ]
   
   Agent.prepAgent()

   if Agent.token == None:
      loginItems.clear()
      loginItems.append("Register")
   else:
      loginItems.clear()
      loginItems.append("Login")


   chosenOption = inquirer.prompt(login)

   while not isLogined:
      if chosenOption["option"] == "Login":
         if Agent.token == '':
            console.print("Agent Not Registered. Register Agent to Continue")
         else:
            isLogined = True

      elif chosenOption["option"] == "Register":
         chosenOption = inquirer.prompt(register)
         Agent.register(chosenOption['name'] , getattr(Factions, chosenOption['faction']).name)

         isLogined = True

      console.print_json(data=Agent.viewAgent())

      chosenOption = inquirer.prompt(options)

   while chosenOption["option"] != "exit":

      if chosenOption["option"] == "view agent":
         console.print_json(data=Agent.viewAgent())

      elif chosenOption["option"] == "view contract":
         console.print_json(data=Contracts.viewContract())
         optionItems.append("accept contract")
      
      elif chosenOption["option"] == "accept contract":
         console.print_json(data=Contracts.acceptContract())
         optionItems.remove("accept contract")
      
      elif chosenOption["option"] == "current location":
         console.print_json(data=SystemInfo.viewCurrentLocation())
      
      elif chosenOption["option"] == "locate shipyard":
         console.print_json(data=SystemInfo.locate("shipyard", "trait"))
         optionItems.append("view ships")
      
      elif chosenOption["option"] == "view ships":
         SystemInfo.viewLocations("shipyard")
         optionItems.append("purchase ship")

      elif chosenOption["option"] == "purchase ship":
         purchase = [
            inquirer.Text('set', message = "Ship Set"),
            inquirer.Text('shipType', message = "Ship Type")
         ]
         purchaseOption = inquirer.prompt(purchase)

         console.print_json(data=Ship.purchaseShip(purchaseOption['shipType'], purchaseOption['set']))

      elif chosenOption["option"] == "my ships":

         for ship in Agent.viewShips():
            console.print_json(data=ship)

            setActive = {
                  inquirer.List('active',
                     message = "Set Ship as Active?",
                     choices = ["Yes", "No", "Exit"]
                  )
            }

            activeChoice = inquirer.prompt(setActive)

            if activeChoice['active'] == "Yes":
               Agent.activeShip = ship
            elif activeChoice['active'] == "Exit":
               break;
         
         optionItems.append("navigate to waypoint")


      elif chosenOption["option"] == "locate engineered asteroid":
         console.print_json(data=SystemInfo.locate("ENGINEERED_ASTEROID", "type"))


      elif chosenOption["option"] == "navigate to waypoint":
         arrived = False

         while not arrived:

            response = SystemInfo.navigateToLastWaypoint(Agent.activeShip)
            console.print_json(data= response)

            if "error" in response and response["error"]["code"] == 4214:
               time.sleep(response["error"]["data"]["secondsToArrival"])
            elif "error" in response and response["error"]["code"] == 4204:
               arrived = True
            elif "nav" in response["data"] and response["data"]["nav"]["status"] == "IN_ORBIT":
               arrived = True

         optionItems.append("dock")

      elif chosenOption["option"] == "dock":
         console.print_json(data=Ship.dock(Agent.activeShip))
         SystemInfo.inOrbit = False

         optionItems.remove("dock")
         optionItems.append("orbit")
         optionItems.append("refuel")

      elif chosenOption["option"] == "refuel":
         console.print_json(data=Ship.refuel(Agent.activeShip))

      elif chosenOption["option"] == "orbit":
         console.print_json(data=SystemInfo.orbit(Agent.activeShip))
         SystemInfo.inOrbit = True
         optionItems.append("extract")

      elif chosenOption["option"] == "extract":

         full = False
         
         while not full:
            response = Ship.extract(Agent.activeShip)
            console.print_json(data=response)

            if "error" in response:
               time.sleep(response["error"]["data"]["cooldown"]["remainingSeconds"])

            elif response["data"]["cargo"]["units"] == response["data"]["cargo"]["capacity"]:
               full = True


         optionItems.remove("extract")



      chosenOption = inquirer.prompt(options)
