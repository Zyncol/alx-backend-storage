#!/usr/bin/env python3
'''
Task 10
'''


def update_topics(mongo_collection, name, topics):
    '''
    Changing all topics of document in a collection based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
