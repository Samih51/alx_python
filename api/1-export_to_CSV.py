#!/usr/bin/python3
import csv
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
    user_id = user_data["id"]
    username = user_data["username"]

    # Create a list to store CSV data
    csv_data = [
        {"USER_ID": user_id, "USERNAME": username, "TASK_COMPLETED_STATUS": task["completed"], "TASK_TITLE": task["title"]}
        for task in todo_data
    ]

    # Define the CSV file path
    filename = f"{user_id}.csv"

    # Write CSV data to a file using csv.DictWriter
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        csvwriter.writeheader()

        # Write the CSV data
        csvwriter.writerows(csv_data)