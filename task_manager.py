import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

TASKS_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description):
        self.tasks.append({'description': description, 'completed': False})
        self.save_tasks()
        logging.info(f"Task added: {description}")

    def complete_task(self, index):
        try:
            self.tasks[index]['completed'] = True
            self.save_tasks()
            logging.info(f"Task {index} marked as complete.")
        except IndexError:
            logging.error("Invalid task index.")

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✔" if task['completed'] else "✖"
            logging.info(f"{i}: [{status}] {task['description']}")
