#!/usr/bin/python3
"""Script to fetch employee TODO list progress and export in CSV format."""

import csv
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

        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            for task in todos_data:
                writer.writerow([
                    user_data["id"],
                    user_data["username"],
                    str(task["completed"]),
                    task["title"]
                ])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./fetch_and_export_todo.py <employee_id>")
    else:
        employee_id = argv[1]
        get_employee_todo_progress(employee_id)
