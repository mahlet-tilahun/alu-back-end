# API

This project involves accessing employee data via a REST API and organizing it into different data structures using Python. The goal is to retrieve and export employee TODO list progress in various formats.

## Features
- Fetch employee TODO list data using an API.
- Display task progress in a structured format.
- Export data in **CSV** and **JSON** formats.
- Support for retrieving data for a single employee or all employees.

## Usage
1. Run the script with an employee ID to get task progress.
2. Use additional scripts to export data to CSV or JSON.

## Requirements
- Python 3.4+
- `requests` module (or `urllib` for API requests)
- Ubuntu 14.04 LTS environment

## File Formats
- **CSV**: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- **JSON**: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}] }`

This project demonstrates why Bash scripting is not ideal for such tasks and follows Pythonic best practices.

