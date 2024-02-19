from rich.console import Console
from libraries.Agent import Agent
from enums.Factions import Factions

console = Console()

if __name__ == '__main__':
    agent = Agent("testGroov5")
    
    if agent.token == None:
       console.print_json(data=agent.register(Factions.COSMIC.name))

    console.print_json(data=agent.view_agent())