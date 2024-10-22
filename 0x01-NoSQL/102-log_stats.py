#!/usr/bin/env python3
'''
task 15
'''
from pymongo import MongoClient


def Displaying_nginx_request(nginx_collection):
    '''
    Printing stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        reque_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, reque_count))
    status_checks = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks))


def Display_top_ip(se_collection):
    '''
    Printing statistics about the top 10 IPs in a collection.
    '''
    print('IPs:')
    reques_logs = se_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in reques_logs:
        ip = request_log['_id']
        requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, requests_count))


def prov():
    '''
    Providing stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    Displaying_nginx_request(client.logs.nginx)
    Display_top_ip(client.logs.nginx)


if __name__ == '__main__':
    prov()
