#!/usr/bin/python3
"""aaaa"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    try:
        id = int(argv[1])
    except ValueError:
        exit()

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo = "{}/todos".format(user)
    filename = '{}.csv'.format(id)

    res = requests.get(user).json()
    username = res.get('username')
    res = requests.get(todo).json()

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for PEPE1 in res:
            status = PEPE1.get('completed')
            title = PEPE1.get('title')

            writer.writerow([id, username, status, title])
