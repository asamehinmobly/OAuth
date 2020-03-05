import json
from functools import wraps

from flask import Response, current_app
from flask import request
from http import HTTPStatus

import binascii
import base64
from Crypto.Cipher import AES
from Crypto.Util import Counter

from utils.OAuth import Credentials


def int_of_string():
    iv = current_app.config['DECRYPTION_IV']
    iv_byte = bytes(iv, encoding="utf8")
    return int(binascii.hexlify(iv_byte), 16)


def decrypt_message(message):
    key = current_app.config['DECRYPTION_KEY']

    message = base64.b64decode(message)
    ctr = Counter.new(128, initial_value=int_of_string())
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    dec_msg = aes.decrypt(message[0:])
    b = str(dec_msg, encoding="utf-8")
    payload = base64.b64decode(b)
    return payload


def oauth_checker(f, auth=True):
    @wraps(f)
    def checker(*args, **kwargs):
        if auth:
            message = request.headers.get('Message')
            try:
                dec_message = decrypt_message(message)
                b = str(dec_message, encoding="utf-8")
                credentials_dict = json.loads(b)
            except Exception as e:
                print(e)
                return response_with_unauthorized()

            if credentials_dict:
                Credentials.set_credentials(credentials_dict=credentials_dict)
                app_id = credentials_dict['application']['app_identifier']
                response = f(app_id, *args, **kwargs)
                Credentials.clear()
                return response
            else:
                return response_with_unauthorized()
        else:
            response = f(*args, **kwargs)
            return response

    return checker


def response_with_unauthorized():
    return Response(response=json.dumps({'error': 'UNAUTHORIZED TOKEN'}),
                    status=HTTPStatus.UNAUTHORIZED.value, mimetype="application/json")
