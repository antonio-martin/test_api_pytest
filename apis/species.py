import requests
from apis.config import base_url

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'


def get_species(id: int = None):
    url = base_url + '/species'
    if id is not None:
        url = url + f'/{id}'
    response = requests.get(url=url)
    return response
