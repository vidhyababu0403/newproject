def add_record(dictionary):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dictionary[key] = value
    print("Record added successfully.")

def edit_record(dictionary):
    key = input("Enter the key to edit: ")
    if key in dictionary:
        value = input("Enter the new value: ")
        dictionary[key] = value
        print("Record updated successfully.")
    else:
        print("Key not found.")

def delete_record(dictionary):
    key = input("Enter the key to delete: ")
    if key in dictionary:
        del dictionary[key]
        print("Record deleted successfully.")
    else:
        print("Key not found.")

def print_dictionary(dictionary):
    print("Dictionary Contents:")
    for key, value in dictionary.items():
        print(key + ": " + value)

dictionary = {}

while True:
    print("\nOptions:")
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Print")
    print("5. Stop/Exit")

    option = input("Enter your option: ")

    if option == '1':
        add_record(dictionary)
    elif option == '2':
        edit_record(dictionary)
    elif option == '3':
        delete_record(dictionary)
    elif option == '4':
        print_dictionary(dictionary)
    elif option == '5':
        break
    else:
        print("Invalid option. Please try again.")

print("Program stopped.")
