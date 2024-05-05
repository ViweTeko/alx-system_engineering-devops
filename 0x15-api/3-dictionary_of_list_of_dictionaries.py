#!/usr/bin/python3
""" This script fetches Rest API todo lists of employees """

import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open('todo_all_employees.json', 'w') as file:
        json.dump({
            us.get('id'): [{
                "task": job.get("title"),
                "completed": job.get("completed"),
                "username": job.get("username")
            } for job in requests.get(
                    url + "todos", params={"userId": us.get('id')}).json()]
            for us in users}, file)
