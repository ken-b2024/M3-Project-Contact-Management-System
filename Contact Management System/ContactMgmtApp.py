import re
import json
contact_dict = {}

menu_items = ["1. Add a new contact",
            "2. Edit an existing contact",
            "3. Delete a contact",
            "4. Search for a contact",
            "5. Display all contacts",
            "6. Export contacts to a text file",
            "7. Import contacts from a text file",
            "8. Quit"
]
def main_menu():
    print("\nWelcome to the Contact Management System!")
    print("\nMenu:", *menu_items, sep="\n")

def new_contact():
    unique_identifier = input("Enter the email address of contact: ")
    pattern = (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}")
    if re.search(pattern, unique_identifier):
        print("\nEmail successfully added")
    else:
        print("\nEmail address is not valid. Please enter a valid email.")
        unique_identifier = input("Enter the email address of contact: ")
    user_name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number (format:xxx-xxx-xxxx): ")
    for number in phone_number:
        pattern = (r"\d{3}-\d{3}-\d{4}")
        if re.search(pattern, phone_number):
            print("\nPhone number successfully added.")
            break
        else:
            print("Phone number is not valid. Please enter a valid phone number.")
            phone_number = input("Enter the phone number (format:xxx-xxx-xxxx): ")
    user_address = input("Enter the address: ")
    add_info = input("Would you like to add any additional notes? (yes/no): ")
    if add_info == "yes":
        notes = input("Add notes here: ")
    else:
        notes = "no additional notes"
    contact_dict[unique_identifier] = {
                    "Name": user_name,
                    "Phone": phone_number,
                    "Email": unique_identifier,
                    "Additional": {"Address": user_address,
                                    "Notes": notes
                    }
            }
    print(f"\n{unique_identifier} has been successfully added!")
    print("\nContact:", contact_dict[unique_identifier], sep="\n")

def edit_contact():
    unique_identifier = input("Enter the email of the contact you want to edit: ")
    if unique_identifier in contact_dict:
        print("\nContact:", contact_dict[unique_identifier], sep="\n ")
        while True:
            action = input("\nWhat do you want to edit? (Name/Email/Phone/Address/Notes): ")
            if action == "Name":
                new_name = input("Enter new name: ")
                contact_dict[unique_identifier]['Name'] = new_name
                print(f"\nName has been changed to {new_name}")
            if action == "Email":
                new_email = input("Enter new email: ")
                contact_dict[unique_identifier] = new_email
                print(f"\nEmail has been changed to {new_email}")
            if action == "Phone":
                new_phone = input("Enter new phone number: ")
                contact_dict[unique_identifier]['Phone'] = new_phone
                print(f"\nPhone number has been changed to {new_phone}")
            if action == "Address":
                new_address = input("Enter the new address: ")
                contact_dict[unique_identifier]['Additional']['Adress'] = new_address
                print(f"\nAddress has been changed to {new_address}")
            if action == "Notes":
                add_notes = input("Add additional notes here: ")
                contact_dict[unique_identifier]['Additional']['Notes'] = add_notes
                print("\nNotes have been successfully added")
            next_edit = input("\nWould you like to edit anything else? (y/n): ")
            if next_edit == "n":
                break
    else:
        print("\nEmail does not exist. Try again.")

def delete_contact():
    unique_identifier = input("Enter the email of the contact you want to delete: ")
    if unique_identifier in contact_dict[unique_identifier]:
        print("\nContact:", contact_dict[unique_identifier], sep="\n ")
        action = input("Are you sure you want to delete this contact? (y/n): ")
        if action == "y":
            contact_dict[unique_identifier].clear()
            print("Contact has been deleted.")
        else:
            return
    else:
        print("Email is not valid. Please try again.")

def search_contact():
    unique_identifier = input("Enter the email of the contact you want to view: ")
    if unique_identifier in contact_dict:
        print("\nContact:", contact_dict[unique_identifier], sep="\n ")
        while True:
            action = input("\nDo you want to search another contact? (y/n): ")
            if action == "y":
                unique_identifier = input("Enter the email of the contact you want to view: ")
                if unique_identifier in contact_dict[unique_identifier]:
                    print("\nContact:", contact_dict, sep="\n ")
            else:
                break
    else:
        print("\nEmail is not valid. Try again.")

def show_contacts():
    if contact_dict:
        print("\nContacts:", contact_dict, sep="\n ")
    else:
        print("\nThere are no contacts to display.")

def export_contacts():
    with open("Contacts.txt", "w") as file:
        json.dump(contact_dict, file, indent=4)
        print("\nContacts exported successfully")

def import_contacts():
        try:
            with open("Contacts.txt", "r") as file:
                contact_dict = json.load(file)
                print("\nContacts were succesfully imported.")
                print("\n")
                print(contact_dict, sep="\n ")
        except FileNotFoundError:
            print("\nThere is no text file in this directory. Please add one and try again.")
while True:
    main_menu()
    try:
        menu_item = int(input("\nPlease select a menu item: "))
        if menu_item == 1:
            new_contact()
        if menu_item == 2:
            edit_contact()
        if menu_item == 3:
            delete_contact()
        if menu_item == 4:
            search_contact()
        if menu_item == 5:
            show_contacts()
        if menu_item == 6:
            export_contacts()
        if menu_item == 7:
            import_contacts()
        if menu_item == 8:
            print("\nThank you for using the Contact Management System! Goodbye!")
            break
    except ValueError:
        print("\nInvalid selection. Please try again.")