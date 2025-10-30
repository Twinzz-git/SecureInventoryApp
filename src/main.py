from auth import login_user, register_user
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

    # Registrar al usuario
    if register_user(username, email, password):
        print("✅ User registered successfully!")
    else:
        print("❌ Username or email already exists.")


def login():
    email = input("Email: ")
    password = getpass("Password: ")
    user = login_user(email, password)
    
    if user:
        print(f"✅ Welcome back, {user['username']}!")
    else:
        print("❌ Login failed. Check your email and password.")
        return

    def admin_user():
        while True:
            print(f"/ ADMIN USER MENU / {user['username']}")
            print("1. View products")
            print("2. Add product")
            print("3. Edit product")
            print("4. Delete product")
            print("5. View logs")
            print("6. Logout")

            choice = input("> ")

            if choice == "1":
                print("View products - not implemented yet.")
            elif choice == "2":
                print("Add product - not implemented yet.")
            elif choice == "3":
                print("Edit product - not implemented yet.")
            elif choice == "4":
                print("Delete product - not implemented yet.")
            elif choice == "5":
                print("View logs - not implemented yet.")
            elif choice == "6":
                break
            else:
                print("Invalid option.")
                
                
                def regular_user():
                    
                    while True:
                        print(f"/ USER MENU / {user['username']}")
                        print("1. View products")
                        print("2. Logout")

                        choice = input("> ")

                        if choice == "1":
                            print("View products - not implemented yet.")
                       
                        elif choice == "2":
                            break
                        else:
                            print("Invalid option.")
                        
                        
                        
                
                

    
  

   


def main():
    while True:
        print("\nSelect an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("> ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
