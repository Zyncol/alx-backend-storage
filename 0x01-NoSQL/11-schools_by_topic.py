#!/usr/bin/env python3
'''
Task 11
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Returns a list of school having a specific topic.
    '''
    topic_filt = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filt)]
