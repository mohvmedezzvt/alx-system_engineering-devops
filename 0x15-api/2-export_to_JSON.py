#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Returns information about a given employee's TODO list progress,
    in the JSON format.
    """
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todo]}, json_file)
