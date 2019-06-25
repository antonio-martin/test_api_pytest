# test_api_pytest
Simple API test structure against Star Wars API (https://swapi.co/) with pytest

## Instalation
You will need the following tools/programs already installed:
* [Homebrew](https://brew.sh/) or any other package manager
* [Python 3](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)

An installation example could be like this:
```
brew install python3
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Having active virtual env, to run the tests:
```
pytest
```
To deactivate the virtual env you just have to type:
```
deactivate
```

## Project structure
| Folder | Description |
| apis | All endpoints for each source separated by source file |
| models | Python classes that match the different objects as Person, Species, etc |
| tests | All tests are here |
