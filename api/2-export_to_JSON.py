#!/usr/bin/python3
"""aaaa"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    try:
        id = int(argv[1])
    except ValueError:
        exit()

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo = "{}/todos".format(user)
    filename = '{}.json'.format(id)

    urss = requests.get(user).json()
    res = requests.get(todo).json()
    user_tasks = list()

    for PEPE1 in res:
        data = {
            'task': PEPE1.get('title'),
            'completed': PEPE1.get('completed'),
            'username': urss.get('username')
        }

        user_tasks.append(data)

    with open(filename, 'w') as f:
        f.write(dumps({id: user_tasks}))
