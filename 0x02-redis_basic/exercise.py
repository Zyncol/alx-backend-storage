#!/usr/bin/env python3
"""
writing strings to reddis
"""
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: callable) -> callable:
    """
    it tracks the number of calls made to cache class
    """
    @functools.wraps(method)
    def triger(self, *args, **kwargs): #sourcery skip: avoid-builtin-shadow
        """
        trigers the given method
        """ 
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return triger

class Cache:
    """
    Represents an object for storing data
    """
    def __init__(self, host="localhost", port=6379, db=0):
        """
        stores an instanc as private variable
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
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
        if data is None:
            return data
        if fn:
            desired = fn(data)
            return desired
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        retrieves a string value from storage
        """
        Dvalue = self.get(key, fn=lambda d: d.decode("utf-8"))
        return Dvalue

    def get_int(self, key: str) -> int:
        """
        retrieves an integer value from storage
        """
        Dvalue = self._redis.get(key)
        try:
            Dvalue = int(Dvalue.decode("utf-8"))
        except Exception:
            return None
        return Dvalue
