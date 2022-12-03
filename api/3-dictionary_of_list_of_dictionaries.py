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

    for ussr_info in ussr:
        ussr_id = ussr_info.get("id")

        task2 = list()

        for res_info in res:
            if res_info.get("userId") == ussr_id:
                info = {
                    "username": ussr_info.get("username"),
                    "task": res_info.get("title"),
                    "completed": res_info.get("completed")
                }

                task2.append(info)
        task1[ussr_id] = task2

    with open(filename, "w") as f:
        f.write(dumps(task1))
