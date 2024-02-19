import modules.RequestHandler as RequestHandler

agent = None
token = None

def prepAgent(prepAgent) -> None:
    global agent
    global token
    
    agent = prepAgent

    with open("secrets", "r") as secrets:
        token = secrets.readline().strip()

    if token != '':
        RequestHandler.headers = {
            "Authorization": "Bearer " + token
        }
    else:
        token = None


def register(faction) -> str:
    global token

    json_data = {
        "symbol": agent,
        "faction": faction
    }

    response_json = RequestHandler.postNoAuth("https://api.spacetraders.io/v2/register", json_data)

    token = response_json['data']['token']

    RequestHandler.headers = {
                "Authorization": "Bearer " + token
            }
    
    with open("secrets", "w") as secrets:
        secrets.write(token)

    return response_json


def view_agent() -> str:
    return RequestHandler.get("https://api.spacetraders.io/v2/my/agent")
