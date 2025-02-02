import os

def todo():
    to_do_list = []
    condition = False
    while condition == False:
        prompt = input("To add new tasks: type |Add|\nTo view all tasks: type |View|\nTo mark tasks as complete: type |Mark|\nTo delete tasks: type |Delete|\nTo exit: type |Exit|\n")

        if prompt == "Add":
            add = input("Enter task name: ")
            to_do_list.append(add + "[]")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif prompt == "View":
            print("\n")
            for i in range(0, len(to_do_list)):
                print(to_do_list[i])
            i = input("Type |con| if you want to continue :")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif prompt == "Mark":
            print("\n")
            for i in range(0, len(to_do_list)):
                print(str(i) + ") " + to_do_list[i])
            i = int(input("Type the number of the task you want to mark as complete: "))
            current = str(to_do_list[i])
            to_do_list[i] = current[0:(len(current)-2)] + "[\u2713]"
            os.system('cls' if os.name == 'nt' else 'clear')
        elif prompt == "Delete":
            print("\n")
            for i in range(0, len(to_do_list)):
                print(str(i) + ") " + to_do_list[i])
            i = int(input("Type the number of the task you want to delete: "))
            to_do_list.remove(to_do_list[i])
            os.system('cls' if os.name == 'nt' else 'clear')
        elif prompt == "Exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            condition = True

todo()

