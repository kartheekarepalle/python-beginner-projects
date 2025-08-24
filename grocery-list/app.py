grocery_list = []

while True:
    print("\n--- Grocery List App ---")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        grocery_list.append(item)
        print(f"{item} added to your list!")

    elif choice == "2":
        if grocery_list:
            print("\nYour Grocery List:")
            for i, item in enumerate(grocery_list, 1):
                print(f"{i}. {item}")
        else:
            print("Your list is empty!")

    elif choice == "3":
        if grocery_list:
            remove = input("Enter item to remove: ")
            if remove in grocery_list:
                grocery_list.remove(remove)
                print(f"{remove} removed!")
            else:
                print("Item not found in the list.")
        else:
            print("List is empty!")

    elif choice == "4":
        print("Ok... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
