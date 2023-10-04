'''
This Python script retrieves tasks for a specific employee from a REST API and exports 
the data in  JSON format. The script accepts an employee ID as a command-line argument and 
fetches tasks associated with that ID from the provided API endpoints. The exported files 
include information about completed tasks and their titles.
'''
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

   # Extract user name
    employee_name = user_data["name"]
    
    # Open CSV file for writing 
    csv_file = open('{}.csv'.format(user_id), 'w', newline='')

    # Create CSV writer 
    writer = csv.writer(csv_file)

    # Write header row
    writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
    
    # Write data rows
    for task in todo_data:
        writer.writerow([user_id, employee_name, task['completed'], task['title']])

    csv_file.close()