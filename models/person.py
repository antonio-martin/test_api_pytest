import datetime
import re

from requests import Response

from apis import people
from models import species
from models import vehicle, film

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'


class Person:
    def __init__(self, id: int = None, birth_year=None, eye_color=None, films: [] = None, gender=None, hair_color=None,
                 height: int = None, homeworld=None, mass=None, name=None, skin_color=None, created: datetime = None,
                 edited: datetime = None, species: [] = None, starships: [] = None, url=None, vehicles: [] = None):
        self.id = id
        self.birth_year = birth_year
        self.eye_color = eye_color
        self._films: [] = films
        self.gender = gender
        self.hair_color = hair_color
        self.height: int = height
        self.homeworld: str = homeworld
        self.mass: int = mass
        self.name: str = name
        self.skin_color = skin_color
        self.created: datetime = created
        self.edited: datetime = edited
        self._species: [] = species
        self._starships: [] = starships
        self._vehicles: [] = vehicles
        self.url = url

    @classmethod
    def load_from_api(cls, id: int):
        response = people.get_people(id=id)
        assert response.status_code == 200, 'Not possible to instantiate person, wrong status code from API'
        return cls.load_from_api_response(response)

    @classmethod
    def load_from_api_response(cls, response: Response):
        return cls(
            id=response.json().get('id'),
            birth_year=response.json().get('birth_year'),
            eye_color=response.json().get('eye_color'),
            films=response.json().get('films'),
            gender=response.json().get('gender'),
            hair_color=response.json().get('hair_color'),
            height=response.json().get('height'),
            homeworld=response.json().get('homeworld'),
            mass=response.json().get('mass'),
            name=response.json().get('name'),
            skin_color=response.json().get('skin_color'),
            created=response.json().get('created'),
            edited=response.json().get('edited'),
            species=response.json().get('species'),
            starships=response.json().get('starships'),
            vehicles=response.json().get('vehicles'),
        )

    def __str__(self):
        return self.name

    def films(self) -> [film.Film]:
        return [film.Film.load_from_api(id=int(re.search(r'(\d)/*$', movie).group(1))) if isinstance(movie, str) else movie for movie in self._films] or []

    def species(self) -> [species.Species]:
        return [species.Species.load_from_api(id=int(re.search(r'(\d)/*$', s).group(1))) if isinstance(s, str) else s for s in self._species] or []

    def starships(self) -> [vehicle.Starship]:
        return [vehicle.Starship.load_from_api(id=int(re.search(r'(\d)/*$', s).group(1))) if isinstance(s, str) else s for s in self._starships] or []

    def vehicles(self) -> [vehicle.Vehicle]:
        return [vehicle.Vehicle.load_from_api(id=int(re.search(r'(\d)/*$', v).group(1))) if isinstance(v, str) else v for v in self._vehicles] or []
