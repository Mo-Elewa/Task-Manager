import json     
from task import Task 

def add_task(self, task):
    self.tasks.append(task)
def show_tasks(self):
    for task in self.tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"Task ID: {task.task_id}, Title: {task.title}, Status: {status}") 

def complete_task(self, task_id):
    for task in self.tasks:
        if task.task_id == task_id:
            task.completed = True
            print("Task  completed.")
            return
    print("Task not found.")

def search_task(self, task_id):
    for task in self.tasks:
        if task.task_id == task_id:                
            print(task.title)
            return
    print("Task not found.") 

def update_task(self, task_id, new_title):
    for task in self.tasks:
        if task.task_id == task_id:
            task.title = new_title
            print("Task updated.")
            return
    print("Task not found.")

def delete_task(self, task_id):
    for task in self.tasks:
        if task.task_id == task_id:
            self.tasks.remove(task)
            print("Task deleted.")
            return
print("Task not found.")     

def save_tasks(self):
    data = [task.__dict__ for task in self.tasks]
    with open("tasks.json", "w") as file:
        json.dump(data, file)
    print("Tasks saved")

def load_tasks(self):
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
        for item in data:
            task = Task(item["task_id"], item["title"])
            task.completed = item["completed"]
            self.tasks.append(task)
    except FileNotFoundError:
        print("No saved tasks")

        