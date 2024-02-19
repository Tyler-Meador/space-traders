from rich.console import Console
import modules.Agent as Agent
from enums.Factions import Factions

console = Console()

if __name__ == '__main__':

   userInput = input("Choose Option: ") 

   if userInput == "login":
      Agent.prepAgent("testGroov6")
   
      if Agent.token == None:
         console.print("Register Agent to Continue")
      else:
         console.print_json(data=Agent.viewAgent())

   elif userInput == "register":
      console.print_json(data=Agent.register(Factions.COSMIC.name))
   
