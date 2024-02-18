import requests
from rich.console import Console
import Agent

console = Console()

if __name__ == '__main__':
    agent = Agent.Agent("testGroov4")
    
    if agent.token == None:
       console.print_json(data=agent.register("COSMIC"))

    console.print_json(data=agent.view_agent())