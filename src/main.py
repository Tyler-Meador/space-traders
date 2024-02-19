from rich.console import Console
import modules.Agent as Agent
from enums.Factions import Factions

console = Console()

if __name__ == '__main__':
    Agent.prepAgent("testGroov6")
    
    if Agent.token == None:
       console.print_json(data=Agent.register(Factions.COSMIC.name))

    console.print_json(data=Agent.view_agent())