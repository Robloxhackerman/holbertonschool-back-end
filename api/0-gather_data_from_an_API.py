#!/usr/bin/python3
"""aaaa"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        id = int(argv[1])
    except ValueError:
        exit()

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todo = "{}/todos".format(user)

    res = requests.get(user).json()
    name = res.get("name")
    res = requests.get(todo).json()
    total = len(res)
    hechont = 0

    for PEPE in res:
        if PEPE.get("completed") is False:
            hechont = hechont + 1
        else:
            pass

    hecho = total - hechont

    print("Employee {} is done with tasks({}/{}):".format(name, hecho, total))

    for elem in res:
        if elem.get("completed") is True:
            print("\t", elem.get("title"))
