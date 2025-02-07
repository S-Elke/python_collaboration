import os

def todo():
    to_do_list = []
    #condition for exiting out of the loop
    condition = False
    while condition == False:
        #clears terminal in between menu prints to look cleaner
        os.system('cls' if os.name == 'nt' else 'clear')
        #menu prompt
        prompt = input("To add new tasks: type |Add|\nTo view all tasks: type |View|\nTo mark tasks as complete: type |Mark|\nTo delete tasks: type |Delete|\nTo exit: type |Exit|\n")

        #allows user to enter task to the list
        if prompt == "Add":
            add = input("Enter task name: ")
            to_do_list.append(add + "[]")
            os.system('cls' if os.name == 'nt' else 'clear')

        #allows user to view the list
        elif prompt == "View":
            print("\n")
            for i in range(0, len(to_do_list)):
                print(to_do_list[i])
            print("\n")
            i = input("Type |con| if you want to continue :")
            os.system('cls' if os.name == 'nt' else 'clear')

        #allows user to mark a task as completed
        #uses unicode character to show a printed checkmark for completed tasks
        elif prompt == "Mark":
            print("\n")
            for i in range(0, len(to_do_list)):
                print(str(i) + ") " + to_do_list[i])
            i = int(input("Type the number of the task you want to mark as complete: "))
            current = str(to_do_list[i])
            to_do_list[i] = current[0:(len(current)-2)] + "[\u2713]"
            os.system('cls' if os.name == 'nt' else 'clear')

        #removes a task from the list
        elif prompt == "Delete":
            print("\n")
            for i in range(0, len(to_do_list)):
                print(str(i) + ") " + to_do_list[i])
            i = int(input("Type the number of the task you want to delete: "))
            to_do_list.remove(to_do_list[i])
            os.system('cls' if os.name == 'nt' else 'clear')

        #breaks the loop 
        elif prompt == "Exit":
            os.system('cls' if os.name == 'nt' else 'clear')
            condition = True

todo()

