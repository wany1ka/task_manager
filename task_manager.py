from datetime import datetime

# File paths
TASKS_FILE = "tasks.txt"
USERS_FILE = "users.txt"

def read_users():
    users = {}
    with open(USERS_FILE, 'r') as file:
        for line in file:
            username, password = line.strip().split(', ')
            users[username] = password
    return users

def write_users(users):
    with open(USERS_FILE, 'w') as file:
        for username, password in users.items():
            file.write(f"{username}, {password}\n")

def read_tasks():
    tasks = []
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            task_data = line.strip().split(', ')
            tasks.append(task_data)
    return tasks

def write_task(task):
    with open(TASKS_FILE, 'a') as file:
        file.write(', '.join(task) + '\n')

def login():
    users = read_users()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Please try again.")

def add_user():
    new_username = input("Enter a new username: ")
    users = read_users()
    if new_username in users:
        print("Username already exists!")
        return

    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm password: ")
    if new_password != confirm_password:
        print("Passwords do not match!")
        return

    users[new_username] = new_password
    write_users(users)
    print("User added successfully!")

def add_task(username):
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (format: DD MMM YYYY): ")

    assigned_date = datetime.now().strftime('%d %b %Y')

    with open(TASKS_FILE, 'a') as file:
        file.write(f"{username}, {title}, {description}, {assigned_date}, {due_date}, No\n")
    print("Task added successfully!")

def view_all_tasks():
    tasks = read_tasks()
    for task in tasks:
        print(", ".join(task))

def view_my_tasks(username):
    tasks = read_tasks()
    for task in tasks:
        if task[0] == username:
            print(", ".join(task))

def display_statistics():
    users = read_users()
    tasks = read_tasks()
    print(f"Total number of users: {len(users)}")
    print(f"Total number of tasks: {len(tasks)}")

def handle_login():
    while True:
        username = login()
        if username:
            return username

def main_menu(username):
    while True:
        print("\nMain Menu:")
        print("r - Register a new user" if username == "admin" else "")
        print("a - Add a new task")
        print("va - View all tasks")
        print("vm - View my tasks")
        print("s - Display statistics" if username == "admin" else "")
        print("e - Exit")

        option = input("Enter your choice: ").lower()

        if option == 'r' and username == "admin":
            add_user()
        elif option == 'a':
            add_task(username)
        elif option == 'va':
            view_all_tasks()
        elif option == 'vm':
            view_my_tasks(username)
        elif option == 's' and username == "admin":
            display_statistics()
        elif option == 'e':
            print("Goodbye!!!")
            exit()
        else:
            print("You have entered an invalid input. Please try again")

def main():
    logged_in_user = handle_login()
    main_menu(logged_in_user)

if __name__ == "__main__":
    main()
