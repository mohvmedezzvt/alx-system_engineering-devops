#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Returns information about a given employee's TODO list progress,
    in the CSV format.
    """
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            csv_writer.writerow([user_id,
                                 user.get("username"),
                                 task.get("completed"),
                                 task.get("title")])
