#!/usr/bin/env python3
"""
writing strings to reddis
"""
import redis
import uuid
from typing import Union


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
