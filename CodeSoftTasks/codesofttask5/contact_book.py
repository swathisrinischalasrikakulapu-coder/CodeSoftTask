contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")

        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")

            contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            print("Contact Added Successfully!")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found!")
        else:
            print("\nContact List")
            for name, details in contacts.items():
                print(f"Name: {name} | Phone: {details['Phone']}")

    # Search Contact
    elif choice == "3":
        search = input("Enter Name to Search: ")

        if search in contacts:
            print("\nContac t Found")
            print("Name:", search)
            print("Phone:", contacts[search]["Phone"])
            print("Email:", contacts[search]["Email"])
            print("Address:", contacts[search]["Address"])
        else:
            print("Contact Not Found!")

    # Update Contact
    elif choice == "4":
        update = input("Enter Name to Update: ")

        if update in contacts:
            contacts[update]["Phone"] = input("Enter New Phone: ")
            contacts[update]["Email"] = input("Enter New Email: ")
            contacts[update]["Address"] = input("Enter New Address: ")

            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    # Delete Contact
    elif choice == "5":
        delete = input("Enter Name to Delete: ")

        if delete in contacts:
            del contacts[delete]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    # Exit
    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Enter 1 to 6.")