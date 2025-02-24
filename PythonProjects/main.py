import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1dabb8ae797a3657e94a1377dffcbd9f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_rename = {
    "pokemon_id": "new_name",
    "name": "generate",
    "photo_id": -1
}

body_hunt = {
    "pokemon_id": "privet_Alena"
}

response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)

POKEMON_ID=response_create.json()['id']
print(POKEMON_ID)

body_rename["pokemon_id"]=POKEMON_ID

response_rename=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.text)

body_hunt["pokemon_id"]=POKEMON_ID

response_hunt=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_hunt)
print(response_hunt.text)






