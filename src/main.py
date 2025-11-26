from auth import login_user, register_user
from validator import validar_username, validar_email, validar_password, validar_price, validar_stock, maxprice, maxstock
from getpass import getpass
from logger import log_action
from product import readproducts, createproduct, updateproduct, deleteproduct, loadproducts

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
    #Menú para administradores
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
            readproducts()
        elif choice == "2":
            log_action(user['username'], "Attempted to add product")
            add_product_menu(user['username'])
        elif choice == "3":
            log_action(user['username'], "Attempted to edit product")
            edit_product_menu(user['username'])
        elif choice == "4":
            log_action(user['username'], "Attempted to delete product")
            delete_product_menu(user['username'])
        elif choice == "5":
            log_action(user['username'], "Viewed logs")
            view_logs()
        elif choice == "6":
            log_action(user['username'], "Logout")
            print("👋 Logged out successfully!")
            break
        else:
            print("❌ Invalid option.")


def user_menu(user):
    #Menú para usuarios regulares (solo lectura)
    while True:
        print(f"\n--- USER MENU ({user['username']}) ---")
        print("1. View products")
        print("2. Logout")
        choice = input("> ")

        if choice == "1":
            log_action(user['username'], "Viewed products")
            readproducts()
        elif choice == "2":
            log_action(user['username'], "Logout")
            print("👋 Logged out successfully!")
            break
        else:
            print("❌ Invalid option.")


def add_product_menu(username):
    #Menú para agregar producto
    print("\n➕ ADD NEW PRODUCT")
    print("-"*40)
    
    name = input("Product name: ").strip()
    if not name:
        print("❌ Product name cannot be empty.")
        return
    
    try:
        price = float(input("Price: $"))
        
        # Usar validar_price() con límites
        if not validar_price(price):
            if price <= 0:
                print("❌ Price must be greater than zero.")
            else:
                print(f"❌ Price cannot exceed ${maxprice:,.2f}")
            return
            
    except ValueError:
        print("❌ Price must be a number.")
        return
    
    try:
        stock = int(input("Stock quantity: "))
        
        # Usar validar_stock() con límites
        if not validar_stock(stock):
            if stock < 0:
                print("❌ Stock cannot be negative.")
            else:
                print(f"❌ Stock cannot exceed {int(maxstock):,} units.")
            return
            
    except ValueError:
        print("❌ Stock must be a number.")
        return
    
    createproduct(name, price, stock, username)


def edit_product_menu(username):
    #Menú para editar producto
    products = loadproducts()
    
    if not products:
        print("\n📦 No products to edit.")
        return
    
    readproducts()
    
    product_name = input("\nEnter product name to edit: ").strip()
    
    print("\n✏️ EDIT PRODUCT (leave blank to keep current value)")
    print("-"*40)
    
    new_name = input("New name: ").strip()
    if not new_name:
        new_name = None
    
    price_str = input("New price: $").strip()
    if price_str:
        try:
            new_price = float(price_str)
            
            # Usar validar_price() con límites
            if not validar_price(new_price):
                if new_price <= 0:
                    print("⚠️ Price must be greater than zero. Keeping old value.")
                else:
                    print(f"⚠️ Price cannot exceed ${maxprice:,.2f}. Keeping old value.")
                new_price = None
                
        except ValueError:
            print("⚠️ Invalid price. Keeping old value.")
            new_price = None
    else:
        new_price = None
    
    stock_str = input("New stock: ").strip()
    if stock_str:
        try:
            new_stock = int(stock_str)
            
            # Usar validar_stock() con límites
            if not validar_stock(new_stock):
                if new_stock < 0:
                    print("⚠️ Stock cannot be negative. Keeping old value.")
                else:
                    print(f"⚠️ Stock cannot exceed {int(maxstock):,} units. Keeping old value.")
                new_stock = None
                
        except ValueError:
            print("⚠️ Invalid stock. Keeping old value.")
            new_stock = None
    else:
        new_stock = None
    
    updateproduct(product_name, name=new_name, price=new_price, stock=new_stock, username=username)


def delete_product_menu(username):
    """Menú para eliminar producto"""
    products = loadproducts()
    
    if not products:
        print("\n📦 No products to delete.")
        return
    
    readproducts()
    
    product_name = input("\nEnter product name to delete: ").strip()
    deleteproduct(product_name, username)


def view_logs():
    """Muestra las últimas 20 líneas del log (solo para admin)"""
    from pathlib import Path
    
    LOG_FILE = Path("logs/log.txt")
    
    if not LOG_FILE.exists():
        print("\n📄 No logs available yet.")
        return
    
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        print("\n" + "="*70)
        print("📋 LAST 20 LOG ENTRIES")
        print("="*70)
        
        # Mostrar últimas 20 líneas
        for line in lines[-20:]:
            print(line.strip())
        
        print("="*70)
    except Exception:
        print("❌ Error reading logs.")


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