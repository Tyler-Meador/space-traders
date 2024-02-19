from libraries.RequestHandler import RequestHandler


class Agent:
    def __init__(self, agent) -> None:
        self.agent = agent
        self.requestHandler = RequestHandler(None)

        with open("secrets", "r") as secrets:
            self.token = secrets.readline().strip()

        if self.token != '':
            self.requestHandler.headers = {
                "Authorization": "Bearer " + self.token
            }
        else:
            self.token = None


    def register(self, faction) -> str:
        json_data = {
            "symbol": self.agent,
            "faction": faction
        }

        response_json = self.requestHandler.postNoAuth("https://api.spacetraders.io/v2/register", json_data)

        self.token = response_json['data']['token']

        self.requestHandler.headers = {
                    "Authorization": "Bearer " + self.token
                }
        
        with open("secrets", "w") as secrets:
            secrets.write(self.token)

        return response_json


    def view_agent(self) -> str:
        return self.requestHandler.get("https://api.spacetraders.io/v2/my/agent")
