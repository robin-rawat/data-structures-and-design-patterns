#Redis singleton pattern

import redis
from threading import Lock, Thread

#Redis Configs
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 1


"""
    Method 1 : using __new__ method
"""
class RedisClient:

    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._make_redis_client()
            else:
                cls._check_client_connection()
        print("INSTANCE : ", cls._instance)
        return cls._instance
    
    @classmethod
    def _make_redis_client(cls):
        cls._instance._redis_client = redis.StrictRedis(host=REDIS_HOST, port = REDIS_PORT, db=REDIS_DB)
    
    @classmethod
    def _check_client_connection(cls):
        try:
            cls._instance._redis_client.ping()
        except Exception:
            cls._make_redis_client()

    def get_redis_client(self):
        return self._redis_client
    

process1 = Thread(target=RedisClient().get_redis_client)
process2 = Thread(target=RedisClient().get_redis_client)
process1.start()
process2.start()


"""
    Method 2 : using metaclass __call__ method
"""


class MetaRedis(type):

    _instance = None
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance  = super().__call__(*args, **kwargs)
                cls._instance._make_redis_client()
            else:
                cls._instance._check_client_connection()
        print("INSTANCE : ", cls._instance)
        return cls._instance


class RedisClient(metaclass=MetaRedis):

    def _make_redis_client(self):
        self._redis_client = redis.StrictRedis(host=REDIS_HOST, port = REDIS_PORT, db=REDIS_DB)
    
    def _check_client_connection(self):
        try:
            self._redis_client.ping()
        except Exception:
            self._make_redis_client()
    
    def get_redis_client(self):
        print("CLI : ", self._redis_client)
        return self._redis_client

process1 = Thread(target=RedisClient().get_redis_client)
process2 = Thread(target=RedisClient().get_redis_client)
process1.start()
process2.start()