#!/usr/bin/python3
""" This script converts API data to JSON"""

import requests
import csv
import json
from sys import argv

if __name__ == "__main__":
    USER_ID = argv[1]
    link = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    result = requests.get(link)
    USERNAME = result.json().get('username')
    link_task = link + '/todos'
    result = requests.get(link_task)
    tasks = result.json()
    data = {USER_ID: []}
    for job in tasks:
        JOB_DONE_STATUS = job.get('completed')
        TITLE = job.get('title')
        data[USER_ID].append(
                {
                    "task": TITLE,
                    "completed": JOB_DONE_STATUS,
                    "username": USERNAME
                    })

    with open('{}.json'.format(USER_ID), 'w') as json_file:
        json.dump(data, json_file)
