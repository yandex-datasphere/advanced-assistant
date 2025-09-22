import json
import jwt
import time
import requests 

def get_iam(service_account_id, key_id, private_key):
    now = int(time.time())
    payload = {
        'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
        'iss': service_account_id,
        'iat': now,
        'exp': now + 360}

    # Формирование JWT
    encoded_token = jwt.encode(
        payload,
        private_key,
        algorithm='PS256',
        headers={'kid': key_id})

    url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    x = requests.post(url,  
                    headers={'Content-Type': 'application/json'},
                    json = {'jwt': encoded_token}).json()
    return x['iamToken']
