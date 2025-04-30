tasks = []


def todo_list():
    while True:
        print("="*50)
        print("\t\tTo Do App")
        print("="*50)
        print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == '2':
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet!")
        elif choice == '3':
            if tasks:
                num = int(input("Enter task number to delete: "))
                if 0 < num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task deleted!")
                else:
                    print("Invalid number!")
            else:
                print("No tasks to delete!")
        elif choice == '4':
            print("Bye bro!")
            break
        else:
            print("Invalid choice!")


todo_list()