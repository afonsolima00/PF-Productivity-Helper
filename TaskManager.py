import csv
import datetime
import os

CSV_FILE = 'tasks.csv'

def add_task():
    description = input("Enter task description: ")
    while True:
        priority = input("Enter priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        print("Invalid priority. Please enter high, medium, or low.")
    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(deadline, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    task = {'description': description, 'priority': priority, 'deadline': deadline}
    write_task_to_csv(task)

def write_task_to_csv(task):
    fieldnames = ['description', 'priority', 'deadline']
    file_exists = os.path.exists(CSV_FILE)
    mode = 'w' if not file_exists else 'a'
    with open(CSV_FILE, mode, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(task)

def get_suggestion(deadline_date):
    today = datetime.date.today()
    delta = (deadline_date - today).days
    if delta < 0:
        return "Overdue! Do this now!"
    elif delta == 0:
        return "Due today! Prioritize this."
    elif delta <= 3:
        return "Due soon. Plan accordingly."
    else:
        return "Upcoming task. Keep it on your radar."

def view_tasks():
    if not os.path.exists(CSV_FILE):
        print("No tasks found.")
        return
    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        tasks = list(reader)
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        task['deadline_date'] = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
    sorted_tasks = sorted(tasks, key=lambda x: x['deadline_date'])
    print(f"{'Description':<20} | {'Priority':<8} | {'Deadline':<10} | {'Suggestion'}")
    print("-" * 60)
    for task in sorted_tasks:
        suggestion = get_suggestion(task['deadline_date'])
        print(f"{task['description']:<20} | {task['priority']:<8} | {task['deadline']:<10} | {suggestion}")

def main():
    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()