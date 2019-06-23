import datetime
import re

from requests import Response

from apis import species
from models import person
from models import film

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'


class Species:
    def __init__(self, id: int = None, name: str = None, classification: str = None, designation: str = None,
                 average_height: int = None, skin_colors: str = None, hair_colors: str = None, eye_colors: str = None,
                 average_lifespan: int = None, homeworld: str = None, language: str = None, people: [] = None,
                 films: [] = None,
                 created: datetime = None, edited: datetime = None, url: str = None):
        self.id = id
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.skin_colors = skin_colors
        self.hair_colors = hair_colors
        self.eye_colors = eye_colors
        self.average_lifespan = average_lifespan
        self.homeworld = homeworld
        self.language = language
        self._people: [] = people
        self._films: [] = films
        self.created = created
        self.edited = edited
        self.url = url

    @classmethod
    def load_from_api(cls, id: int):
        response = species.get_species(id=id)
        return cls.load_from_api_response(response)

    @classmethod
    def load_from_api_response(cls, response: Response):
        return cls(
            id=response.json().get('id'),
            name=response.json().get('name'),
            classification=response.json().get('classification'),
            designation=response.json().get('designation'),
            average_height=response.json().get('average_height'),
            skin_colors=response.json().get('skin_colors'),
            hair_colors=response.json().get('hair_colors'),
            eye_colors=response.json().get('eye_colors'),
            average_lifespan=response.json().get('average_lifespan'),
            homeworld=response.json().get('homeworld'),
            language=response.json().get('language'),
            people=response.json().get('people'),
            films=response.json().get('films'),
            created=response.json().get('created'),
            edited=response.json().get('edited'),
            url=response.json().get('url'),
        )

    def __str__(self):
        return self.name

    def films(self) -> [film.Film]:
        return [film.Film.load_from_api(id=int(re.search(r'(\d)/*$', movie).group(1))) if isinstance(movie, str) else movie for movie in self._films] or []

    def people(self) -> []:
        return [person.Person.load_from_api(id=int(re.search(r'(\d)/*$', character).group(1))) if isinstance(character, str) else character for character in self._people] or []
