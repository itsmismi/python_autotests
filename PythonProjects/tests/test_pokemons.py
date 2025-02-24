import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1dabb8ae797a3657e94a1377dffcbd9f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '21428'


def test_status_code():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code==200

def test_part_of_response():
    response_get=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name']=='Хокайдо'

@pytest.mark.parametrize('key, value',[('trainer_name','Хокайдо'),('trainer_id','TRAINER_ID')])
def test_parametrize(key,value):
    response_parametrize=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0]['trainer_name']=='Хокайдо'