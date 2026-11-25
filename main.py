import os
import csv
from datetime import datetime
from task import Task
from todolist import add_task, complete_task, delete_task, list_tasks

# Save the data file in the same folder as main.py
FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "tasks.csv"
)


# Load previously saved tasks
def load_tasks():
    task_list = []

    if not os.path.exists(FILE_NAME):
        print("No saved tasks found. Starting a new list.")
        return task_list

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                due_date = None

                if row["due_date"]:
                    due_date = datetime.strptime(
                        row["due_date"], "%Y-%m-%d"
                    ).date()

                completed = row["completed"] == "True"

                task = Task(row["title"], due_date, completed)
                task_list.append(task)

        print("Saved tasks loaded successfully!")

    except (OSError, ValueError, KeyError, csv.Error) as error:
        print("Error loading tasks:", error)

    return task_list


# Save tasks to a CSV file
def save_tasks(task_list):
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["title", "due_date", "completed"])

            for task in task_list:
                writer.writerow([
                    task.title,
                    str(task.due_date) if task.due_date else "",
                    task.completed
                ])

        print("Tasks saved successfully!")

    except OSError as error:
        print("Error saving tasks:", error)


# Main menu
def main():
    task_list = load_tasks()

    while True:
        print("\n===== PERSONAL TO-DO LIST MANAGER =====")
        print("A. Add a new task")
        print("C. Mark a task as completed")
        print("D. Delete a task")
        print("L. List all tasks")
        print("Q. Quit")

        choice = input("Enter your choice (A/C/D/L/Q): ").upper().strip()

        if choice == "A":
            title = input("Enter task title: ").strip()
            due_date = input(
                "Enter due date (YYYY-MM-DD) or press Enter to skip: "
            ).strip()

            add_task(task_list, title, due_date or None)

        elif choice == "C":
            list_tasks(task_list)

            try:
                number = int(input("Enter task number to complete: "))
                complete_task(task_list, number - 1)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "D":
            list_tasks(task_list)

            try:
                number = int(input("Enter task number to delete: "))
                delete_task(task_list, number - 1)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "L":
            list_tasks(task_list)

        elif choice == "Q":
            answer = input("Save your tasks before quitting? (Y/N): ")

            if answer.strip().upper() == "Y":
                save_tasks(task_list)

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select A, C, D, L, or Q.")


# Run the program
if __name__ == "__main__":
    main()
