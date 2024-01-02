#!/usr/bin/python3
"""Script to fetch employee TODO list progress and export in CSV format."""

import requests
import csv
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
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in todos_data:
                writer.writerow({
                    "USER_ID": user_data["id"],
                    "USERNAME": user_data["username"],
                    "TASK_COMPLETED_STATUS": task["completed"],
                    "TASK_TITLE": task["title"]
                })

        print(f"CSV file '{csv_filename}' created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./fetch_and_export_todo.py <employee_id>")
    else:
        employee_id = argv[1]
        get_employee_todo_progress(employee_id)
