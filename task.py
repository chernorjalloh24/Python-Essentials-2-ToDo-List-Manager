from datetime import date


class Task:
    """Represents one task in the to-do list."""

    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        # Display whether the task is completed
        status = "[X]" if self.completed else "[-]"

        # Display the task title
        task_info = f"{status} {self.title}"

        # Include the due date when provided
        if self.due_date:
            task_info += f" (due {self.due_date})"

            # Identify overdue incomplete tasks
            if not self.completed and self.due_date < date.today():
                task_info += " [OVERDUE]"

        return task_info


# Test the Task class
if __name__ == "__main__":
    task1 = Task("Submit Python assignment")
    task2 = Task("Complete project", date(2026, 12, 10))
    task3 = Task("Review Python notes", completed=True)

    print("===== TASK CLASS TEST =====")
    print(task1)
    print(task2)
    print(task3)
