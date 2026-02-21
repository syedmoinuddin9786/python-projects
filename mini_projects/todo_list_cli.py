task = []


while True:
  print("/n1. Add Task")
  print("2. View Task")
  print("3. Delete Task")
  print("4. Exit")




choice = input("Enter your choice:   ")


if choice == "1":
  task = input("Enter new task:  ")
  task.append(task)
  print("Task added!")


elif choice == "2":
  if len task == 0:
    print("no tasks yet.")
    else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
