import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuario no Github
    :param usuario: str com nome de usuário no github
    :return: str com link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('pessoasnil'))
