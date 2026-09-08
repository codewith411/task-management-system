from datetime import datetime

from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)

    except ValueError as error:
        print(error)
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    if not pending_tasks:
        print("No pending tasks.")
        return

    for task in pending_tasks:
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print()


def calculate_progress(tasks=tasks):
    if not tasks:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100

    return progress
