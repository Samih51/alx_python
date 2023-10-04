#!/usr/bin/python3
'''
This Python script retrieves tasks for a specific employee from a REST API and exports 
the data in  JSON format. The script accepts an employee ID as a command-line argument and 
fetches tasks associated with that ID from the provided API endpoints. The exported files 
include information about completed tasks and their titles.
'''

import json
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url) 

    user_data = user_response.json()
    todo_data = todo_response.json()

    # Extract username 
    username = user_data['username']

    # Format task data
    tasks = []
    for task in todo_data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"], 
            "username": username
        })

    # Write to JSON file
    filename = f"{user_id}.json"
    with open(filename, 'w') as f:
        json.dump({user_id: tasks}, f)