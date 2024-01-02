#!/usr/bin/python3
"""Script to fetch employee TODO list progress from a REST API."""

import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """Fetch and display employee TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)

        print(f"Employee {user_data['name']} is done with tasks "
              f"({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./fetch_todo_progress.py <employee_id>")
    else:
        employee_id = argv[1]
        get_employee_todo_progress(employee_id)
