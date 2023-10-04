#!/usr/bin/python3
import requests
import sys
import json

if __name__=="__main__":
    user_id = sys.argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_data = todo_response.json()
    user_data = user_response.json()

    # Extract relevant information
    username = user_data["username"]

    # Prepare JSON data as a list of dictionaries
    json_data = []
    for task in todo_data:
        task_title = task["title"]
        completed_status = task["completed"]
        json_data.append({"task": task_title, "completed": completed_status, "username": username})

    # Define the JSON file path
    filename = f"{user_id}.json"

    # Write JSON data to a file
    with open(filename, 'w') as jsonfile:
        json.dump({user_id: json_data}, jsonfile)