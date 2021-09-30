import requests


def buscar_avatar(usuario):
    """
    Busca avatar a partir de um usuario do GitHub
    :param usuario: str com o nome do usuário do github
    :return: str com o link do avatar do usuario
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('artursalviano'))
