# Contact management system to store student details
Contact_details = {}

def add():
    name = input("Enter Name of the Student: ")
    mobile_num = input("Mobile Number: ")
    reg_num = input("Registration Number: ")
    email_id = input("Email ID: ")

    # Store inside dictionary
    Contact_details[name] = {
        "mobile_num": mobile_num,
        "reg_num": reg_num,
        "email_id": email_id
    }

    print("\nAdded Successfully\n")


def search():
    search_name = input("Enter name of the student: ")

    if search_name in Contact_details:
        info = Contact_details[search_name]
        print("\nStudent Found:")
        print("Student Name =", search_name)
        print("Mobile Number =", info["mobile_num"])
        print("Registration Number =", info["reg_num"])
        print("Email ID =", info["email_id"], "\n")
    else:
        print("\nNo contacts available on that name\n")


def Display_Contacts():
    if not Contact_details:
        print("\nNo Contacts Are Available\n")
    else:
        print("\n.....Contact Details.....")
        for name, info in Contact_details.items():
            print(f"Name: {name}, Mobile: {info['mobile_num']}, Reg No: {info['reg_num']}, Email: {info['email_id']}")
        print()


while True:
    print("1. Add Details")
    print("2. Search Contacts")
    print("3. Display Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        search()
    elif choice == "3":
        Display_Contacts()
    elif choice == "4":
        print("Exit the Database")
        break
    else:
        print("Invalid Your choice\n")
