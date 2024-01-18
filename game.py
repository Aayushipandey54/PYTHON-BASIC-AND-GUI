import random

def get_user_choice():
    print("Choose a snack:")
    print("1. Chocolate")
    print("2. Chips")
    print("3. Fruits")
    print("4. Ice Cream")
    print("5. Pizza")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_snack_response(choice):
    snacks = {
        1: "You chose Chocolate. Yum!",
        2: "Chips are a great choice for a snack!",
        3: "Fruits are a healthy and delicious snack!",
        4: "Ice Cream is a delightful treat!",
        5: "Pizza is a classic choice. Enjoy!"
    }
    return snacks.get(choice, "Invalid choice. Please choose a valid snack.")

def snack_game():
    print("Welcome to the Snack Game!")
    user_choice = get_user_choice()
    response = get_snack_response(user_choice)
    print(response)

if __name__ == "__main__":
    snack_game()

