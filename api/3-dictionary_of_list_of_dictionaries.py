#!/usr/bin/python3
"""
Script that retrieves and displays all employees' TODO list progress
using a REST API and exports the data in JSON format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    session = requests.Session()
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_response = session.get(users_url).json()
    todos_response = session.get(todos_url).json()
    all_data = {}
    for user in users_response:
        user_id = user["id"]
        username = user["username"]
        user_tasks = [{"username": username, "task": task["title"],
                       "completed": task["completed"]}
                      for task in todos_response if task["userId"] == user_id]
        all_data[user_id] = user_tasks
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file, indent=4)
    print("Data exported to todo_all_employees.json")

