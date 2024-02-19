import modules.console as Console
import modules.Agent as Agent
from enums.Factions import Factions
import modules.contracts as Contracts
import modules.systemInfo as SystemInfo
import inquirer

console = Console.console

if __name__ == '__main__':

   isLogined = False
   optionItems = ["exit", "view agent", "view contract", "accept contract", "current location", "locate shipyard"]
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
                    choices = optionItems
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

      console.clear(True)
      console.print_json(data=Agent.viewAgent())

      chosenOption = inquirer.prompt(options)

   while chosenOption["option"] != "exit":
      console.clear(True)

      if chosenOption["option"] == "view agent":
         console.print_json(data=Agent.viewAgent())

      elif chosenOption["option"] == "view contract":
         console.print_json(data=Contracts.viewContract())
      
      elif chosenOption["option"] == "accept contract":
         console.print_json(data=Contracts.acceptContract())
      
      elif chosenOption["option"] == "current location":
         console.print_json(data=SystemInfo.viewCurrentLocation())
      
      elif chosenOption["option"] == "locate shipyard":
         console.print_json(data=SystemInfo.locate("shipyard"))
         optionItems.append("view ships")
      
      elif chosenOption["option"] == "view ships":
         SystemInfo.viewLocations("shipyard", "shipTypes")

      chosenOption = inquirer.prompt(options)
