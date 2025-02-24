# Step-by-Step Plan

## Set Up Environment
- Install Python (available for free at [python.org](https://www.python.org)).
- Use a free code editor like Visual Studio Code, Sublime Text, or Notepad.

## Plan Functionality

### Features
- Add tasks with a description, priority (high/medium/low), and deadline.
- Save tasks to a CSV file for persistent storage.
- Sort tasks by deadline for prioritization.
- Provide suggestions based on how urgent each task is.

## Tools
- Use Python’s built-in `csv` module for file handling.
- Use the `datetime` module for working with dates.
- Use simple rule-based logic for urgency suggestions.

## Interface
- Create a command-line interface using `input()` for user interaction.

## Write the Script
1. **Import Required Modules**:
   - Import `csv`, `datetime`, and `os`.
2. **Define Constants**:
   - Define a constant for the CSV file name.

### Write Functions
- `add_task()`: Collect task details from the user.
- `write_task_to_csv(task)`: Save tasks to the CSV file.
- `get_suggestion(deadline_date)`: Generate urgency-based suggestions.
- `view_tasks()`: Display all tasks sorted by deadline with suggestions.

3. **Create a Main Function**:
   - Implement a menu loop for adding tasks, viewing them, or exiting.

## Test the Script
1. Run the script with `python script_name.py`.
2. Add a few test tasks with varying priorities and deadlines.
3. View the tasks to ensure they display sorted and with correct suggestions.
4. Check the CSV file to confirm tasks are stored properly.
5. Test edge cases like past deadlines or invalid date formats.

## Refine and Expand (Optional)
1. Add input validation to handle errors (e.g., invalid dates).
2. Improve the display formatting for better readability.
3. Add error handling for file operations.
4. Optionally extend with features like editing or deleting tasks.
