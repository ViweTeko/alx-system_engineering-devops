#!/usr/bin/python3
""" This script fetches Rest API todo lists of employees """

import requests
import json
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    Users = response.json()
    u_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)
        url = url + '/todos/'
        response = requests.get(url)

        task = response.json()
        u_dict[USER_ID] = []
        for job in task:
            JOB_DONE_STATUS = job.get('completed')
            TITLE = job.get('title')
            u_dict[USER_ID].append(
                    {
                        "task": TITLE,
                        "completed": JOB_DONE_STATUS,
                        "username": USERNAME })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(u_dict, file)
