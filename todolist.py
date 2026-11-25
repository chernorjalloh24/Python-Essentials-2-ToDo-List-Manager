from datetime import datetime, date
from task import Task


# Add a new task
def add_task(task_list, title, due_date=None):
    try:
        if not title.strip():
            print("Error: Task title cannot be empty.")
            return

        if due_date:
            due_date = datetime.strptime(
                due_date, "%Y-%m-%d"
            ).date()

        new_task = Task(title, due_date)
        task_list.append(new_task)

        print("Task added successfully!")

    except ValueError:
        print("Error: Invalid date. Use YYYY-MM-DD.")


# Complete a task
def complete_task(task_list, index):
    try:
        if index < 0:
            raise IndexError

        task_list[index].completed = True
        print("Task marked as completed!")

    except IndexError:
        print("Error: Invalid task number.")


# Delete a task
def delete_task(task_list, index):
    try:
        if index < 0:
            raise IndexError

        removed_task = task_list.pop(index)
        print("Task deleted:", removed_task.title)

    except IndexError:
        print("Error: Invalid task number.")


# Display all tasks
def list_tasks(task_list):
    if not task_list:
        print("Your to-do list is empty.")
        return

    print("\n===== YOUR TO-DO LIST =====")

    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")
