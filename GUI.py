import csv
import datetime
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define the CSV file for storing tasks
CSV_FILE = 'tasks.csv'

# Function to add a task to the CSV file
def write_task_to_csv(task):
    """
    Write a task to the CSV file. Creates the file with headers if it doesn't exist.
    
    Args:
        task (dict): Dictionary containing task details (description, priority, deadline).
    """
    fieldnames = ['description', 'priority', 'deadline']
    file_exists = os.path.exists(CSV_FILE)
    mode = 'w' if not file_exists else 'a'
    with open(CSV_FILE, mode, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(task)

# Function to generate suggestions based on task urgency
def get_suggestion(deadline_date):
    """
    Generate a suggestion for a task based on its deadline.
    
    Args:
        deadline_date (datetime.date): The deadline date of the task.
    
    Returns:
        str: A suggestion message based on urgency.
    """
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

# Function to load tasks from CSV and display in the GUI
def load_tasks():
    """
    Load tasks from the CSV file and display them in the task list.
    Clears the existing list before loading.
    """
    task_list.delete(*task_list.get_children())  # Clear existing rows
    if not os.path.exists(CSV_FILE):
        return
    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        tasks = list(reader)
    for task in tasks:
        try:
            deadline_date = datetime.datetime.strptime(task['deadline'], '%Y-%m-%d').date()
            suggestion = get_suggestion(deadline_date)
            task_list.insert("", "end", values=(task['description'], task['priority'], task['deadline'], suggestion))
        except ValueError:
            messagebox.showerror("Error", f"Invalid deadline format for task: {task['description']}")

# Function to add a new task via GUI
def add_task():
    """
    Add a new task using input from the GUI fields.
    Validates the input and updates the CSV file and task list.
    """
    description = description_entry.get()
    priority = priority_entry.get().lower()
    deadline = deadline_entry.get()
    
    # Input validation
    if not description:
        messagebox.showerror("Error", "Task description cannot be empty.")
        return
    if priority not in ['high', 'medium', 'low']:
        messagebox.showerror("Error", "Priority must be high, medium, or low.")
        return
    try:
        datetime.datetime.strptime(deadline, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
        return
    
    # Add task to CSV and refresh task list
    task = {'description': description, 'priority': priority, 'deadline': deadline}
    write_task_to_csv(task)
    description_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)
    load_tasks()  # Refresh the task list

# GUI Setup
root = tk.Tk()
root.title("Task Manager")

# Input fields for adding tasks
tk.Label(root, text="Description:").grid(row=0, column=0, padx=5, pady=5)
description_entry = tk.Entry(root, width=30)
description_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Priority (high/medium/low):").grid(row=1, column=0, padx=5, pady=5)
priority_entry = tk.Entry(root, width=30)
priority_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Deadline (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
deadline_entry = tk.Entry(root, width=30)
deadline_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

refresh_button = tk.Button(root, text="Refresh Tasks", command=load_tasks)
refresh_button.grid(row=4, column=0, columnspan=2, pady=5)

# Task list display using Treeview
task_list = ttk.Treeview(root, columns=("Description", "Priority", "Deadline", "Suggestion"), show="headings")
task_list.heading("Description", text="Description")
task_list.heading("Priority", text="Priority")
task_list.heading("Deadline", text="Deadline")
task_list.heading("Suggestion", text="Suggestion")
task_list.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Initial load of tasks
load_tasks()

# Start the GUI loop
root.mainloop()