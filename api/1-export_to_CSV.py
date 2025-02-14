#!/usr/bin/python3
"""
Script that retrieves and displays an employee's TODO list progress
using a REST API and exports data to a CSV file.
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    session = requests.Session()
    emp_id = sys.argv[1]
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    tasks_response = session.get(tasks_url)
    user_response = session.get(user_url)
    tasks = tasks_response.json()
    emp_name = user_response.json().get('username')
    
    completed_tasks = [task for task in tasks if task['completed']]
    
    print(f"Employee {emp_name} is done with tasks"
          f"({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
    
    # Export to CSV
    file_name = f"{emp_id}.csv"
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([emp_id, emp_name, task['completed'], task['title']])

