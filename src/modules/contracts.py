import modules.RequestHandler as RequestHandler

def viewContract() -> str:
    return RequestHandler.get("https://api.spacetraders.io/v2/my/contracts")