from redis import Redis
import json
from flask import current_app as application
from utils.exceptions import ConnectionError, ConfigrationError


class RedisCash(object):
    """initialize connection with Redis"""
    try:
        REDIS_SERVER_HOST = application.config["REDIS_SERVER_HOST"]
        REDIS_SERVER_PORT = application.config["REDIS_SERVER_PORT"]
    except:
        raise ConfigrationError("can't read cofigration :  \
            host = {} , port = {} ".format(REDIS_SERVER_HOST, REDIS_SERVER_PORT))

    try:
        client = Redis(host=REDIS_SERVER_HOST, port=REDIS_SERVER_PORT)
    except:
        raise ConnectionError("can't connect to redis with cofigration :  \
            host = {} , port = {} ".format(REDIS_SERVER_HOST, REDIS_SERVER_PORT))

    @classmethod
    def get_(cls, key):
        value = RedisCash.client.get(key)
        if value:
            value = json.loads(value.decode('utf8'))
        return value

    @classmethod
    def set_(cls, key, value, timeout=0):
        """timeout = 0 means no expire"""
        try:
            value = json.dumps(value, default=str)
        except:
            print("value isn't json and can not be dumped")
            return None
        RedisCash.client.set(key, value)
        if timeout:
            RedisCash.client.expire(key, int(timeout))
        return RedisCash.get_(key)

    @classmethod
    def clear_(cls, key):
        RedisCash.client.delete(key)

    @classmethod
    def app_prefix_get(cls, key, owner_id):
        _key = str(owner_id) + ':' + key
        return RedisCash.get_(_key)

    @classmethod
    def app_prefix_set(cls, key, value, owner_id, timeout=0):
        _key = str(owner_id) + ':' + key
        return RedisCash.set_(_key, value, timeout=timeout)

    @classmethod
    def app_prefix_clear(cls, key, owner_id):
        _key = str(owner_id) + ':' + key
        RedisCash.client.delete(_key)

    @classmethod
    def generate_key(cls, prefix, *args):
        cache_key = prefix + ":" + ":".join(args)
        return cache_key
