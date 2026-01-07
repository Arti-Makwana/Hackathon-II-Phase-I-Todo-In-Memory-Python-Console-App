import json
import os

class TodoManager:

    def search_tasks(self, keyword):
        """Returns a list of tasks where the keyword is in the title or description."""
        keyword = keyword.lower()
        return [
            t for t in self.tasks 
            if keyword in t['title'].lower() or keyword in t['description'].lower()
        ]
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()
    def search_tasks(self, keyword):
        """Returns a list of tasks where the keyword is in the title."""
        return [t for t in self.tasks if keyword.lower() in t['title'].lower()]    

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    self.tasks = json.load(f)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, description, priority="Medium", category="General", due_date="N/A"): 
        new_id = max([t['id'] for t in self.tasks], default=0) + 1
        task = {
            "id": new_id,
            "title": title,
            "description": description,
            "priority": priority, 
            "category": category,
            "due_date": due_date, # NEW: Added due date
            "completed": False
        }
        self.tasks.append(task)
        self.save_to_file()
        return task

    def get_tasks_by_category(self, category_name):
        """NEW: Returns only tasks that match a specific category."""
        return [t for t in self.tasks if t.get('category', 'General').lower() == category_name.lower()]

    def get_all_tasks(self):
        return self.tasks

    def toggle_complete(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["completed"] = not t["completed"]
                self.save_to_file()
                return True
        return False
    def edit_task(self, task_id, title=None, due_date=None):
        """Updates a task's title or due date by its ID."""
        for t in self.tasks:
            if t["id"] == task_id:
                if title:
                    t["title"] = title
                if due_date:
                    t["due_date"] = due_date
                self.save_to_file()
                return True
        return False

    def delete_task(self, task_id):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) < initial_count:
            self.save_to_file()
            return True
        return False