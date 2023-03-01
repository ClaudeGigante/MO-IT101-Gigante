import csv

FILE_PATH = "MotorPHEmployeeData.csv"

def add_employee():
    id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = input("Enter employee Birthday: ")
    position = input("Enter employee position: ")
    department = input("Enter employee Address: ")
    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, name, age, position, department])
        print("Employee added successfully.")

def remove_employee():
    id = input("Enter employee ID to remove: ")
    with open(FILE_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        employees = list(reader)
    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        removed = False
        for employee in employees:
            if employee[0] == id:
                removed = True
                continue
            writer.writerow(employee)
        if removed:
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

def search_employee():
    id = input("Enter employee ID to search: ")
    with open(FILE_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        for employee in reader:
            if employee[0] == id:
                print("Employee found:")
                print(f"ID: {employee[0]}")
                print(f"LastName: {employee[1]}")
                print(f"Name: {employee[2]}")
                print(f"Birthday: {employee[3]}")
                print(f"Position: {employee[11]}")
                print(f"Address: {employee[4]}")
                return
        print("Employee not found.")

def display_employees():
    with open(FILE_PATH, "r", newline="") as f:
        reader = csv.reader(f)
        print("List of employees:")
        for employee in reader:
            print(f"ID: {employee[0]}, LastName: {employee[1]}, Name:{employee[2]}, Birthday: {employee[3]}, Position: {employee[11]}, Address: {employee[4]}")

while True:
    print("\nEmployee Information Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Search Employee")
    print("4. Display Employees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        remove_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
