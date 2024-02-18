import requests

class Agent:
    def __init__(self, agent) -> None:
        self.agent = agent

        with open("secrets", "r") as secrets:
            self.token = secrets.readline().strip()

        if self.token != '':
            self.headers = {
                "Authorization": "Bearer " + self.token
            }
        else:
            self.token = None


    def register(self, faction) -> str:
        json_data = {
            "symbol": self.agent,
            "faction": faction
        }

        response_json = requests.post("https://api.spacetraders.io/v2/register", json = json_data).json()

        self.token = response_json['data']['token']
        self.headers = {
                    "Authorization": "Bearer " + self.token
                }
        
        with open("secrets", "w") as secrets:
            secrets.write(self.token)

        return response_json


    def view_agent(self) -> str:
        return requests.get("https://api.spacetraders.io/v2/my/agent", headers=self.headers).json()
