
def get_user_information():
    print("Please enter your information:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    address = input("Address: ")

    print("\nThank you! Here is the information you provided:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Address: {address}")

if __name__ == "__main__":
    get_user_information()
