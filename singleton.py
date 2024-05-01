#Redis singleton pattern

import redis

#Redis Configs
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 1

class RedisClient:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._make_redis_client()
        else:
            cls._check_client_connection()

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
    

redis_cli1 = RedisClient()
redis_cli2 = RedisClient()

print(redis_cli1 == redis_cli2)
print(redis_cli1.get_redis_client() == redis_cli2.get_redis_client())




