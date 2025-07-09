import csv
import sys

def select_option():
    while True:
        option = input("Choose an option (0-5): ")
        try:
            option = int(option)
            if 0 <= option <= 5:
                return option
            else:
                print("Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Enter an integer.")

def check_status():
    while True:
        status = input("Pending/Complete: ").strip()
        if status in ["Pending", "Complete"]:
            return status
        print("Invalid status. Type exactly 'Pending' or 'Complete'.")

def exit_program():
    sys.exit()

def view_task():
    try:
        with open("tasks.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            tasks = list(reader)
    except FileNotFoundError:
        tasks = []

    if not tasks:
        print("There are no saved tasks yet.")
        return

    print("-" * 10 + " Your saved tasks " + "-" * 10)
    print("Description".ljust(25), "Status")
    for row in tasks:
        if len(row) >= 2:
            print(row[0].ljust(25), row[1])

def add_task():
    description = input("Write the new task: ").strip()
    status = check_status()

    new_task = [description, status]

    try:
        file_exists = False
        try:
            with open("tasks.csv", "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                file_exists = (first_line == "Task,Status")
        except FileNotFoundError:
            pass

        with open("tasks.csv", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Task", "Status"])
            writer.writerow(new_task)

        print(f"Task '{description}' added with status '{status}'.")
    except Exception as e:
        print(f"Error adding task: {e}")

def update_task(description, new_status):
    updated = False
    try:
        with open("tasks.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            tasks = []
            for row in reader:
                if row[0] == description:
                    row[1] = new_status
                    updated = True
                tasks.append(row)

        with open("tasks.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Task", "Status"])
            writer.writerows(tasks)

        if updated:
            print(f"Task '{description}' marked as {new_status}.")
        else:
            print(f"Task '{description}' not found.")
    except Exception as e:
        print(f"Error updating task: {e}")

def delete_task():
    description = input("Delete task: ").strip()
    deleted = False

    try:
        with open("tasks.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            tasks = []
            for row in reader:
                if row[0] == description:
                    deleted = True
                else:
                    tasks.append(row)

        if deleted:
            with open("tasks.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Task", "Status"])
                writer.writerows(tasks)
            print(f"Task '{description}' deleted.")
        else:
            print(f"Task '{description}' not found.")
    except Exception as e:
        print(f"Error deleting task: {e}")

def menu():
    while True:
        print("\n" + "-" * 35)
        print("Welcome to your task list")
        print("-" * 35)
        print("0) Exit")
        print("1) View Task")
        print("2) Add Task")
        print("3) Mark as Complete")
        print("4) Mark as Pending")
        print("5) Delete Task")
        
        option = select_option()

        if option == 0:
            exit_program()
        elif option == 1:
            view_task()
        elif option == 2:
            add_task()
        elif option == 3:
            desc = input("Task to mark as complete: ").strip()
            update_task(desc, "Complete")
        elif option == 4:
            desc = input("Task to mark as pending: ").strip()
            update_task(desc, "Pending")
        elif option == 5:
            delete_task()