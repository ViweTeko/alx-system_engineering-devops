#!/usr/bin/python3
"""
 This script gathers employee data from API
"""

import re
import requests
from sys import argv

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            emp_id = int(argv[1])
            user = requests.get('{}/users/{}'.format(REST_API, emp_id)).json()
            todo = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = user.get('name')
            task = list(filter(lambda a: a.get('userId') == emp_id, todo))
            done = list(filter(lambda a: a.get('completed'), task))
            print('Employee {} is done with tasks({}/{}):'.format(
                emp_name, len(done), len(task)))
            if len(done) > 0:
                for job in done:
                    print('\t {}'.format(job.get('title')))
