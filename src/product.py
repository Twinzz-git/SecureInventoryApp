# src/products.py
import json
from pathlib import Path

productfile = Path("data/inventory.json")


def loadproducts():
    """Carga todos los productos del archivo"""
    try:
        if productfile.exists():
            return json.loads(productfile.read_text(encoding="utf-8"))
        else:
            return []
    except Exception:
        return []


def saveproduct(products):
    """Guarda todos los productos en el archivo"""
    try:
        productfile.parent.mkdir(parents=True, exist_ok=True)
        productfile.write_text(
            json.dumps(products, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        return True
    except Exception:
        return False


def createproduct(name, price, stock):
    """Create a new product with the given name, price, and stock."""
    products = loadproducts()
    
    product = {
        'name': name,
        'price': price,
        'stock': stock
    }
    products.append(product)
    
    if saveproduct(products):
        print(f"✅ Product '{name}' created successfully.")
        return product
    else:
        print("❌ Error creating product.")
        return None


def readproducts():
    """Muestra todos los productos"""
    products = loadproducts()
    
    if not products:
        print("\n📦 No products in inventory.")
        return
    
    print("\n" + "="*60)
    print("📦 PRODUCT INVENTORY")
    print("="*60)
    
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} - Price: ${product['price']:.2f} - Stock: {product['stock']}")
    
    print("="*60)


def updateproduct(product_name, name=None, price=None, stock=None):
    """Update the product details with the given values."""
    products = loadproducts()
    
    # Buscar el producto por nombre
    product = None
    for p in products:
        if p['name'] == product_name:
            product = p
            break
    
    if not product:
        print(f"❌ Product '{product_name}' not found.")
        return None
    
    try:
        if name is not None:
            product['name'] = name
        if price is not None:
            product['price'] = price
        if stock is not None:
            product['stock'] = stock
        
        if saveproduct(products):
            print("✅ Product updated successfully.")
            return product
        else:
            print("❌ Error saving changes.")
            return None
    
    except Exception as e:
        print(f"❌ Error updating product: {e}")
        return None


def deleteproduct(product_name):
    """Delete the given product from the inventory."""
    products = loadproducts()
    
    # Buscar el producto por nombre
    product = None
    for p in products:
        if p['name'] == product_name:
            product = p
            break
    
    if not product:
        print(f"❌ Product '{product_name}' not found.")
        return False
    
    try:
        products.remove(product)
        if saveproduct(products):
            print(f"✅ Product '{product_name}' deleted successfully.")
            return True
        else:
            print("❌ Error saving changes.")
            return False
    except Exception as e:
        print(f"❌ Error deleting product: {e}")
        return False