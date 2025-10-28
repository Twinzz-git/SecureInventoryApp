from validator import validar_username, validar_email, validar_password
from getpass import getpass

def register():
    username = input("Username: ")
    email = input("Email: ")
    password = getpass("Password: ")
    password2 = getpass("Confirm password: ")

    if not validar_username(username):
        print("Invalid username (3-20 chars, letters and digits only).")
        return
    if not validar_email(email):
        print("Invalid email format.")
        return
    if password != password2:
        print("Passwords do not match.")
        return
    if not validar_password(password):
        print("Password must be at least 8 chars, include a letter and a number.")
        return

    # aquí llamarías register_user(username, email, password)
    print("Validation OK — proceed to register.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Register")
        print("2. Exit")
        choice = input("> ")

        if choice == "1":
            register()
        elif choice == "2":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
