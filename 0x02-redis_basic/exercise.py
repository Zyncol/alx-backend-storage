#!/usr/bin/env python3
"""
writing strings to reddis
"""
import redis
import uuid
from typing import Union, Callabo, Optional


class Cache:
    """
    Represents an object for storing data
    """
    def __init__(self, host="localhost",port=6379, db=0):
        """
        stores an instanc as private variable
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random key
        """
        keyy = str(uuid.uuid4())
        self._redis.set(keyy, data)
        return keyy
    def get(self, key: str, 
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        takes key string arguments
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data
    def get_str(self, key: str) -> str:
        """
        retrieves a string value from storage
        """
        Dvalue = self.get(key, fn=lambda x: x.decode('utf-8'))
        return Dvalue
    def get_int(self, key: str) -> int:
        """
        retrieves an integer value from storage
        """
        return self.get(key, lambda x: int(x))
