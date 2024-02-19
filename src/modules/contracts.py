import modules.RequestHandler as RequestHandler

contractId = None

def viewContract() -> str:
    global contractId

    response = RequestHandler.get("https://api.spacetraders.io/v2/my/contracts")
    contractId = response['data'][0]['id']
    return response

def acceptContract() -> str:
    if contractId != None:
        return RequestHandler.post("https://api.spacetraders.io/v2/my/contracts/" + contractId + "/accept")
    else:
        viewContract()
        return acceptContract()