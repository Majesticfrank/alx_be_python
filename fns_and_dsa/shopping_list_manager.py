def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1: Add, 2: Remove, 3: View, 4: Exit): ")
        
        if choice == "1":
            item_name = input("Enter item name to add: ")
            shopping_list.append(item_name)
            print(f"{item_name} added to your shopping list.")

        elif choice == "2":
            item_name = input("Enter item name to remove: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print(f"{item_name} removed from your shopping list.")
            else:
                print(f"{item_name} not found in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print("Your current shopping list:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
