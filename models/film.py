import datetime
import re

from requests import Response

from apis import films
from models import person

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'


class Film:
    def __init__(self, id: int = None, episode_id: int = None, title: str = None, opening_crawl: str = None,
                 director: str = None,
                 producer: str = None, release_date: datetime = None, characters: [] = None, planets: [] = None,
                 starships: [] = None,
                 vehicles: [] = None, species: [] = None, created: datetime = None, edited: datetime = None,
                 url: str = None):
        self.episode_id: int = episode_id
        self.title: str = title
        self.opening_crawl: str = opening_crawl
        self.director: str = director
        self.producer: str = producer
        self.release_date: datetime = release_date
        self._characters: [] = characters
        self._planets: [] = planets
        self._starships: [] = starships
        self._vehicles: [] = vehicles
        self._species: [] = species
        self.created: datetime = created
        self.edited: datetime = edited
        self.url: str = url
        self.id: int = id

    @classmethod
    def load_from_api(cls, id: int):
        response = films.get_film(id=id)
        return cls.load_from_api_response(response)

    @classmethod
    def load_from_api_response(cls, response: Response):
        return cls(
            episode_id=response.json().get('episode_id'),
            title=response.json().get('title'),
            opening_crawl=response.json().get('opening_crawl'),
            director=response.json().get('director'),
            producer=response.json().get('producer'),
            release_date=response.json().get('release_date'),
            characters=response.json().get('_characters'),
            planets=response.json().get('planets'),
            starships=response.json().get('starships'),
            vehicles=response.json().get('vehicles'),
            species=response.json().get('species'),
            created=response.json().get('created'),
            edited=response.json().get('edited'),
            url=response.json().get('url'),
            id=response.json().get('id'),
        )

    def __str__(self):
        return self.title

    def characters(self) -> []:
        return [person.Person.load_from_api(id=int(re.search(r'(\d)/*$', character).group(1))) if isinstance(character, str) else character for character in self._characters] or []
