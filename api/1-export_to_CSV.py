#!/usr/bin/python3
"this imports request"
import requests
"this imports sys"
import sys

"where the main code starts"
if __name__=="__main__":
    " This Python script retrieves tasks for a specific employee from a REST API and exports the data in CSV and JSON formats. The script accepts an employee ID as a command-line argument and fetches tasks associated with that ID from the provided API endpoints. The exported files include information about completed tasks and their titles."
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
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]

    # Add tasks data to CSV data list
    for task in todo_data:
        task_completed_status = task["completed"]
        task_title = task["title"]
        csv_data.append([user_id, username, task_completed_status, task_title])

    # Write CSV data to a file
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_data)