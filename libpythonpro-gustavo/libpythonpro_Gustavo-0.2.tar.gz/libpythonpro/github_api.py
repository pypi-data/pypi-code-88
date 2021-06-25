import requests as requests


def bucar_avatar(usuario):
    """
    busca o avatar do nome de usuario
    :param usuario:
    :return:
    """
    url = f"https://api.github.com/users/{usuario}"
    resp = requests.get(url)
    resp.json()['avatar_url']


if __name__ == '__main__':
    print(bucar_avatar('GustavoGuesser'))
