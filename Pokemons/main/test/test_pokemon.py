import requests
import pytest



def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200



def test_name_trainer():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params=
    {'trainer_1d': '1800'})
    assert response.json ['trainer_name'] == 'Моня'
