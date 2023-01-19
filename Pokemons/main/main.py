import requests
import json

# !!! Следующие ниже запросы из вики не переведены в формат информации:
#     8.  Создание покемона
#     10. Смена имени покемона
#     11. Поймать покемона в покебол

# 1. Получение токена в телеграмм и создание переменной для него

# 'id': '1800', 'trainer_name': 'Моня',
# 'trainer_token': '0078a7ea645d7b1aa55ded456ea89484'

token = '0078a7ea645d7b1aa55ded456ea89484'

# API 

# Протокол: `https`
# Host: `pokemonbattle.me`
# Порт: `5000`
# Обязательный `header` в POST, PUT, DELETE запросах: Content-Type: application/json
# После авторизации сетится кука `user_hash` в браузер на один год.


# 1. Регистрация с использованием полученного токена POST /trainers/reg

# response = requests.post('https://pokemonbattle.me:5000/trainer/reg', json = {
#     "trainer_token" : token,
#     "email" : "del-aleksandr-ershov@qa.studio",
#     "password" : "IysJNcerCDRm56YBJPkq9"
# }, headers={'Content-Type' : 'application/json'})
# print(response.text) 


# 2. Активация тренера -подтверждение почты POST trainers/confirm_email

# response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email',
# json = {"trainer_token": token
# }, headers={'Content-Type' : 'application/json'})
# print(response_confirm.text)
# print(response_confirm.status_code)

# if response_confirm.status_code == 200:
#     print('OK')
# else:
#     print('not ok')   


# 8. Создание покемона POST /pokemons

response_new = requests.post('https://pokemonbattle.me:5000/pokemons',
headers = {'Content-Type' : 'application/json',  'trainer_token' : token},
json = {
    "name": "Упсс",
    "photo": ""   
} )

print(response_new.text)

# пример для перевода значения ключа из ответа (если персонаж один)
# pokemon_id = response.json()['id']


# 10. Изменение имени или фото покемона PUT /pokemons

response_change = requests.put('https://pokemonbattle.me:5000/pokemons',
headers={'Content-Type' : 'application/json',  "trainer_token" : token},
json = {
    "pokemon_id": "3062",
    "name": "Котя",
    "photo": "https://dolnikov.ru/pokemons/05.png"
})

print(response_change.text)


# 11. Поймать покемона в покебол POST /trainers/add_pokeball

response_battle = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',
headers={'Content-Type' : 'application/json',  "trainer_token" : token},
json = {
     "pokemon_id": "3065"
})

print(response_battle.text)


# 12. Выселить покемона из покебола PUT /trainers/delete_pokeball    
# response_retreat = requests.put('https://pokemonbattle.me:5000/trainers/delete_pokeball'
# headers={'Content-Type' : 'application/json',  "trainer_token" : token},
# json = {
#      "pokemon_id": pokemon_id
# })



# 13. Убить своего покемона (как в покеболе так и без) POST /pokemons/kill

# response_kill = requests.post('https://pokemonbattle.me:5000/pokemons/kill',
# headers={'Content-Type' : 'application/json',  "trainer_token" : token},
# json = {
#       "pokemon_id": "3063"
# })



