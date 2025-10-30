from auth import login_user, register_user
from validator import validar_username, validar_email, validar_password
from getpass import getpass
from logger import log_action

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
        log_action(username, "User registered")
        print("✅ User registered successfully!")
    else:
        log_action(username, "Registration failed - duplicate user")
        print("❌ Username or email already exists.")


def login():
    email = input("Email: ")
    password = getpass("Password: ")
    user = login_user(email, password)
    
    if user:
        log_action(user['username'], "Login successful")
        print(f"✅ Welcome back, {user['username']}!")
        
        # Mostrar menú según el rol
        if user['role'] == 'admin':
            admin_menu(user)
        else:
            user_menu(user)
    else:
        log_action(email, "Login failed")
        print("❌ Login failed. Check your email and password.")


def admin_menu(user):
    """Menú para administradores"""
    while True:
        print(f"\n--- ADMIN MENU ({user['username']}) ---")
        print("1. View products")
        print("2. Add product")
        print("3. Edit product")
        print("4. Delete product")
        print("5. View logs")
        print("6. Logout")
        choice = input("> ")

        if choice == "1":
            log_action(user['username'], "Viewed products")
            print("📦 View products - not implemented yet.")
        elif choice == "2":
            log_action(user['username'], "Attempted to add product")
            print("➕ Add product - not implemented yet.")
        elif choice == "3":
            log_action(user['username'], "Attempted to edit product")
            print("✏️ Edit product - not implemented yet.")
        elif choice == "4":
            log_action(user['username'], "Attempted to delete product")
            print("🗑️ Delete product - not implemented yet.")
        elif choice == "5":
            log_action(user['username'], "Viewed logs")
            print("📋 View logs - not implemented yet.")
        elif choice == "6":
            log_action(user['username'], "Logout")
            print("👋 Logged out successfully!")
            break
        else:
            print("❌ Invalid option.")


def user_menu(user):
    """Menú para usuarios regulares (solo lectura)"""
    while True:
        print(f"\n--- USER MENU ({user['username']}) ---")
        print("1. View products")
        print("2. Logout")
        choice = input("> ")

        if choice == "1":
            log_action(user['username'], "Viewed products")
            print("📦 View products - not implemented yet.")
        elif choice == "2":
            log_action(user['username'], "Logout")
            print("👋 Logged out successfully!")
            break
        else:
            print("❌ Invalid option.")


def main():
    while True:
        print("\n=== SECURE INVENTORY APP ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("> ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()