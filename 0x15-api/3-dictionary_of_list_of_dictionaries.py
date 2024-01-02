#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Returns information about a given employee's TODO list progress,
    in the JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todo = requests.get(url + "todos").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todo
            if user.get("id") == task.get("userId")] for user in users},
            json_file)
