import requests

headers = None

def postNoAuth(url, json_data) -> str:
        return requests.post(url, json = json_data).json()

def post( url, json_data) -> str:
    return requests.post(url, json = json_data, headers = headers).json()

def get(url) -> str:
        return requests.get(url, headers = headers).json()