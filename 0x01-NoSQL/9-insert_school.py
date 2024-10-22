#!/usr/bin/env python3
'''
Task 9
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserting a new document in a collection.
    '''
    resul = mongo_collection.insert_one(kwargs)
    return resul.inserted_id
