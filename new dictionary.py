Dict = {}
Dict = dict({1: 'kutty', 2: 'zaali', 3: 'deesha',4:'denzu'})
print(Dict)

while True:
    print("Options:")
    print("1. Add the dict")
    print("2. Edit the dict")
    print("3. Delete the dict")
    print("4. Print the dict")
    print("5. Stop/Exit")

    option = input("Enter your option: ")

    if option == "1":
        key = input("key: ")
        value = input("value: ")
        Dict[key] = value
        print("Record added")

    elif option == "2":
        key = input("Enter the key to edit: ")
        if key in Dict:
            value = input("new value: ")
            Dict[key] = value
            print("Record updated")
        else:
            print("Key not found")

    elif option == "3":
        key = input("Enter the key to delete: ")
        if key in Dict:
            del Dict[key]
            print("Record deleted")
        else:
            print("Key not found.")

    elif option == "4":
        print("Dictionary:")
        for key, value in Dict.items():
            print(key, ":", value)

    elif option == "5":
        print("Exit")
        break

    else:
        print("Please try again")
