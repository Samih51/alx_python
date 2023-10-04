""" student JSON output """
import json 
import requests

TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'
USERS_URL = 'https://jsonplaceholder.typicode.com/users'

if __name__ == '__main__':

    user_id = 1 # example

    # Fetch all todos
    all_todos = requests.get(TODOS_URL).json() 

    # Filter user's todos
    user_todos = []
    for todo in all_todos:
        if todo['userId'] == user_id:
            user_todos.append(todo)

    # Fetch user info
    user_response = requests.get(f'{USERS_URL}/{user_id}')
    username = user_response.json()['username']

    # Build tasks list
    tasks = []
    for todo in user_todos:
        tasks.append({
            'username': username,
            'task': todo['title'],
            'completed': todo['completed']
        })

    # Write JSON file
    filename = f'{user_id}.json'
    with open(filename, 'w') as f:
        json.dump({user_id: tasks}, f)