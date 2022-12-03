#!/usr/bin/python3
"""aaaa"""
from json import dumps
import requests


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users"
    todo = "https://jsonplaceholder.typicode.com/todos"
    filename = "todo_all_employees.json"

    ussr = requests.get(user).json()
    res = requests.get(todo).json()
    task1 = dict()

    for PEPE1 in res:

        task2 = list()

        for PEPE2 in res:
            if PEPE2.get("userId") == PEPE1.get("id"):
                info = {
                    "username": PEPE1.get("username"),
                    "tasks": PEPE2.get("title"),
                    "completed": PEPE2.get("completed")
                }
            task2.append(info)
        task1[PEPE1.get("id")] = task2

    with open(filename, "w") as f:
        f.write(dumps(task1))