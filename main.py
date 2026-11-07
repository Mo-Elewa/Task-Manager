from task import Task
from manager import TaskManager
from operation import(
   add_task,
   show_tasks,   
   search_task,
   update_task,
   delete_task,
   complete_task,
   save_tasks,
   load_tasks  

)
manager = TaskManager()
load_tasks(manager)

while True:
    print("\n--Task Manager--")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Search Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Complete Task")
    print("7. Save Tasks")
    print("8. Exit")
    choice = input("choice: ")

    if choice == '1':
        task_id = int(input("Enter task ID: "))
        title = input("Enter task title: ")
        task = Task(task_id, title)
        add_task(manager,task)        
        save_tasks(manager)

    elif choice == '2':
        show_tasks(manager)

    elif choice == '3':
        task_id = int(input("Enter task ID: "))
        search_task(manager, task_id)    

    elif choice == '4':
        task_id = int(input("Enter task ID to update: "))
        new_title = input("Enter new title: ")
        update_task(manager, task_id, new_title)
        save_tasks(manager)

    elif choice == '5':
        task_id = int(input("Enter task ID to delete: "))
        delete_task(manager, task_id)
        save_tasks(manager)

    elif choice == '6':
        task_id = int(input("Enter task ID to complete: "))
        complete_task(manager, task_id) 
        save_tasks(manager)

    elif choice == '7':
        save_tasks(manager) 

    elif choice == '8':
        break
    else:
        print("Invalid choice")

