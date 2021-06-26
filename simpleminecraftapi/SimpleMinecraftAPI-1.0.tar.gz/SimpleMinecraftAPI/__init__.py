import requests

def getid(name:str):
    if name is None:
        return
    respond = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}')
    return respond["id"]

def getskin(name:str):
    return f'https://crafatar.com/skins/{getid(name)}'

def gethead(name: str):
    return f'https://crafatar.com/renders/head/{getid(name)}'

def getbody(name: str):
    return f'https://crafatar.com/renders/body/{getid(name)}'

def getcape(name: str):
    return f'https://crafatar.com/renders/capes/{getid(name)}'