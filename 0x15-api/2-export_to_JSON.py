#!/usr/bin/python3
"""Script to fetch employee TODO list progress and export in JSON format."""

import json
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

        json_filename = f"{employee_id}.json"

        json_data = {
            str(user_data["id"]): [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_data["username"]
                }
                for task in todos_data
            ]
        }

        with open(json_filename, "w") as jsonfile:
            json.dump(json_data, jsonfile, indent=2)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./fetch_and_export_todo.py <employee_id>")
    else:
        employee_id = argv[1]
        get_employee_todo_progress(employee_id)
