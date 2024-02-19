import requests

class RequestHandler:

    def __init__(self, headers) -> None:
            self.headers = headers

    def postNoAuth(self, url, json_data) -> str:
          return requests.post(url, json = json_data).json()
    
    def post(self, url, json_data) -> str:
        return requests.post(url, json = json_data, headers = self.headers).json()
    
    def get(self, url) -> str:
          return requests.get(url, headers = self.headers).json()