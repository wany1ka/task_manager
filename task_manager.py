from datetime import datetime

# File paths
TASKS_FILE = "tasks.txt"
USERS_FILE = "users.txt"

# function reads users from file
def read_users():
    users = {}
    with open(USERS_FILE, 'r') as file:
        for line in file:
            username, password = line.strip().split(', ')
            users[username] = password
    return users

# function writes users to file
def write_users(users):
    with open(USERS_FILE, 'w') as file:
        for username, password in users.items():
            file.write(f"{username}, {password}\n")

# function reads tasks from file
def read_tasks():
    tasks = []
    with open(TASKS_FILE, 'r') as file:
        for line in file:
            task_data = line.strip().split(', ')
            tasks.append(task_data)
    return tasks

# function writes tasks from file
def write_task(task):
    with open(TASKS_FILE, 'a') as file:
        file.write(', '.join(task) + '\n')

# function for user's login
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

# function adds a new user
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

# function adds a new task
def add_task(username):
    # task details
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (format: DD MMM YYYY): ")

    assigned_date = datetime.now().strftime('%d %b %Y')

    # adds task to txt
    with open(TASKS_FILE, 'a') as file:
        file.write(f"{username}, {title}, {description}, {assigned_date}, {due_date}, No\n")
    print("Task added successfully!")


# Function to view all tasks
def view_all_tasks():
    tasks = read_tasks()
    for task in tasks:
        print(", ".join(task))


# Function to view all of user's tasks
def view_my_tasks(username):
    tasks = read_tasks()
    for task in tasks:
        if task[0] == username:
            print(", ".join(task))


# Function to view number of tasks and users
def display_statistics():
    users = read_users()
    tasks = read_tasks()
    print(f"Total number of users: {len(users)}")
    print(f"Total number of tasks: {len(tasks)}")


# Function handles and returns user login
def handle_login():
    while True:
        username = login()
        if username:
            return username


# Function fot the main menu
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

# starting point
def main():
    logged_in_user = handle_login()
    main_menu(logged_in_user)

if __name__ == "__main__":
    main()
