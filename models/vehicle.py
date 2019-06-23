import datetime
import re

from requests import Response

from apis import vehicles, starships
from models import person
from models import film

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'


class Vehicle:
    def __init__(self, id: int = None, name: str = None, model: str = None, manufacturer: str = None,
                 cost_in_credits: str = None,
                 length: str = None, max_atmosphering_speed: str = None, crew: str = None, passengers: str = None,
                 cargo_capacity: str = None,
                 consumables: str = None, vehicle_class: str = None,
                 pilots: [] = None,
                 films: [] = None, created: datetime = None, edited: datetime = None, url: str = None):
        self.id: int = id
        self.name: str = name
        self.model: str = model
        self.manufacturer: str = manufacturer
        self.cost_in_credits: str = cost_in_credits
        self.length: str = length
        self.max_atmosphering_speed: str = max_atmosphering_speed
        self.crew: str = crew
        self.passengers: str = passengers
        self.cargo_capacity: str = cargo_capacity
        self.consumables: str = consumables
        self.vehicle_class: str = vehicle_class
        self._pilots: [] = pilots
        self._films: [] = films
        self.created: datetime = created
        self.edited: datetime = edited
        self.url: str = url

    @classmethod
    def load_from_api(cls, id: int):
        response = vehicles.get_vehicles(id=id)
        return cls.load_from_api_response(response)

    @classmethod
    def load_from_api_response(cls, response: Response):
        return cls(
            id=response.json().get('id'),
            name=response.json().get('name'),
            model=response.json().get('model'),
            manufacturer=response.json().get('manufacturer'),
            cost_in_credits=response.json().get('cost_in_credits'),
            length=response.json().get('length'),
            max_atmosphering_speed=response.json().get('max_atmosphering_speed'),
            crew=response.json().get('crew'),
            passengers=response.json().get('passengers'),
            cargo_capacity=response.json().get('cargo_capacity'),
            consumables=response.json().get('consumables'),
            vehicle_class=response.json().get('vehicle_class'),
            pilots=response.json().get('pilots'),
            films=response.json().get('films'),
            created=response.json().get('created'),
            edited=response.json().get('edited'),
            url=response.json().get('url'),
        )

    def __str__(self):
        return self.name

    def films(self) -> [film.Film]:
        return [film.Film.load_from_api(id=int(re.search(r'(\d)/*$', movie).group(1))) if isinstance(movie,
                                                                                                     str) else movie
                for movie in self._films] or []

    def pilots(self) -> []:
        return [person.Person.load_from_api(id=int(re.search(r'(\d)/*$', character).group(1))) if isinstance(
            character, str) else character for character in self._pilots] or []


class Starship(Vehicle):
    def __init__(self, hyperdrive_rating: str = None, mglt: str = None, starship_class: str = None, **kwargs):
        super().__init__(**kwargs)
        delattr(self, 'vehicle_class')
        self.hyperdrive_rating: str = hyperdrive_rating
        self.mglt: str = mglt
        self.starship_class: str = starship_class

    @classmethod
    def load_from_api(cls, id: int):
        response = starships.get_starships(id=id)
        return cls.load_from_api_response(response)

    @classmethod
    def load_from_api_response(cls, response: Response):
        return cls(
            id=response.json().get('id'),
            name=response.json().get('name'),
            model=response.json().get('model'),
            manufacturer=response.json().get('manufacturer'),
            cost_in_credits=response.json().get('cost_in_credits'),
            length=response.json().get('length'),
            max_atmosphering_speed=response.json().get('max_atmosphering_speed'),
            crew=response.json().get('crew'),
            passengers=response.json().get('passengers'),
            cargo_capacity=response.json().get('cargo_capacity'),
            consumables=response.json().get('consumables'),
            hyperdrive_rating=response.json().get('hyperdrive_rating'),
            mglt=response.json().get('mglt'),
            starship_class=response.json().get('starship_class'),
            pilots=response.json().get('pilots'),
            films=response.json().get('films'),
            created=response.json().get('created'),
            edited=response.json().get('edited'),
            url=response.json().get('url'),
        )
