import csv

# Open the CSV file for reading
with open('MotorPHEmployeeData.csv', 'r') as file:
    reader = csv.reader(file)

    # Get the headers
    headers = next(reader)

    # Create a list to store the updated information
    updated_info = []

    # Loop through each row
    for row in reader:
        # Get the user ID
        user_id = row[0]

        # Display the user's current information
        print("User ID:", row[0])
        print("LastName:", row[1])
        print("FirstName:", row[2])
        print("Phone:", row[5])
        print("Address:", row[4])
        print("Birthday:", row[3])

        # Prompt the user for updates
        LastName = input("Enter new LastName (leave blank to keep current): ")
        FirstName = input("Enter new FirstName (leave blank to keep current): ")
        phone = input("Enter new phone (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        birthday = input("Enter new birthday (leave blank to keep current): ")

        # Add the updated information to the list
        updated_info.append([user_id, LastName or row[1], FirstName or row[2], phone or row[5], address or row[4], birthday or row[3]])

# Open the CSV file for writing
with open('updated_user_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the headers
    writer.writerow(headers)

    # Write the updated information
    writer.writerows(updated_info)

print("User information updated successfully!")
