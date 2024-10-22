#!/usr/bin/env python3
'''
Task 12
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''
    Printing stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        reque_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, reque_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def prov():
    '''
    Providing some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    prov()
