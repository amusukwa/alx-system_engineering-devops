#!/usr/bin/python3
"""Script to fetch Employees TODO list progress and export in JSON format."""

import requests
import json


def get_todo_all_employees():
    """Fetch and display TODO list progress for all employees."""
    base_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        users_response = requests.get(base_url)
        users_data = users_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        json_data = {}
        for user in users_data:
            user_id = str(user["id"])
            json_data[user_id] = [
                {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                }
                for task in todos_data if task["userId"] == user["id"]
            ]

        json_filename = "todo_all_employees.json"

        with open(json_filename, "w") as jsonfile:
            json.dump(json_data, jsonfile, indent=2)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_todo_all_employees()
