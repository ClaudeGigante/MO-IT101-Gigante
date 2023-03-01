import csv

# Open the Employee Database file
with open('MotorPHEmployeeData.csv', 'r') as file:

    # Create a CSV reader object
    reader = csv.reader(file)

    # Read the header row
    header = next(reader)

    # Create an empty dictionary to store the employee information
    employees = {}

    # Iterate over each row in the file
    for row in reader:

        # Extract the employee information from the row
        employee_id = row[0]
        LastName = row[1]
        FirstName = row[2]
        Birthday = row[3]
        Position = row[11]

        # Add the employee information to the employees dictionary
        employees[employee_id] = {"LastName": LastName, "FirstName": FirstName, "Birthday": Birthday, "Position": Position}

# Prompt the user to enter an employee ID
employee_id = input("Enter an employee ID to view their information: ")

# Check if the employee ID is valid
if employee_id not in employees:
    print("Invalid employee ID.")
else:
    # Display the employee information
    print("Employee ID:", employee_id)
    print("LastName:", employees[employee_id]["LastName"])
    print("FirstName:", employees[employee_id]["FirstName"])
    print("Birthday:", employees[employee_id]["Birthday"])
    print("Position:", employees[employee_id]["Position"])