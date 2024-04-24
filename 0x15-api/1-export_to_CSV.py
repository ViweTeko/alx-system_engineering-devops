#!/usr/bin/python3
""" This script exports API to CSV """

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    link = "https://jsonplaceholder.typicode.com/users/" + user
    result = requests.get(link)
    user_name = result.json().get('username')
    todo = link + "/todos"
    result = requests.get(todo)
    tasks = result.json()

    with open('{}.csv'.format(user), w) as csv_file:
        for job in tasks:
            done = job.get('completed')
            title = job.get('title')
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, done, title))
