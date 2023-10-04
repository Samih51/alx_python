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

if __name__=="__main__":
    user_id = sys.argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_data = todo_response.json()
    user_data = user_response.json()

    # Extract relevant information
    username = user_data["username"]

    # Prepare JSON data as a list of dictionaries
    data = []
    for task in todo_data:
        data.append({
            "id": user_id,
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })


    # Define the JSON file path
    filename = "{}.json".format(user_id)

    # Write JSON data to a file
    # Write to JSON 
    with open(filename, 'w') as f:
        json.dump(data, f)