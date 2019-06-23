import json

import pytest

from apis.people import get_people
from models import person

__author__ = 'Antonio Martin Gonzalez'
__email__ = 'ant.martin.gonzalez@gmail.com'

test_character_data = [
    (1, 'Luke Skywalker', 'Human', 5, 2, 2),
    (2, 'C-3PO', 'Droid', 6, 0, 0),
    (3, 'R2-D2', 'Droid', 7, 0, 0),
    (4, 'Darth Vader', 'Human', 4, 0, 1),
    (5, 'Leia Organa', 'Human', 5, 1, 0),
               ]


@pytest.mark.parametrize("id, name, species_name, films_number, vehicles_number, starships_number", test_character_data)
def test_character(id, name, species_name, films_number, vehicles_number, starships_number):
    character = person.Person.load_from_api(id=id)
    assert character.name == name, 'Wrong character name'
    assert character.species()[0].name == species_name, 'Wrong species name'

    films = character.films()
    assert len(films) == films_number, f'Wrong number of films for character {id}'

    vehicles = character.vehicles()
    assert len(vehicles) == vehicles_number, f'Wrong number of vehicles for character {id}'

    starships = character.starships()
    assert len(starships) == starships_number, f'Wrong number of starships for character {id}'


def test_get_all_people():
    response = get_people(id=None)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json()['count'] == 87, 'Wrong count value'
    assert len(response.json()['results']) == 10, 'Not enough results'


test_person_invalid_id_data = [
    (-1, 404, 'Not found'),
    ('a', 404, 'Not found'),
    (0, 404, 'Not found'),
    (999999999999, 404, 'Not found'),
    (1.5, 404, '''<!DOCTYPE html>'''),
]


@pytest.mark.parametrize("id, expected_code, expected_message", test_person_invalid_id_data)
def test_person_invalid_id(id, expected_code, expected_message):
    response = get_people(id=id)
    assert response.status_code == expected_code, 'Wrong status code'
    try:
        assert response.json()['detail'] == expected_message, 'Wrong expected message'
    except json.decoder.JSONDecodeError:
        assert expected_message in response.text, 'Wrong expected message'
