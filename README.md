# 🛡️ Secure Inventory App (CLI)

A CLI-based mini-application to manage a product inventory with user authentication, access control, and CRUD operations, following Secure Coding Practices.

## 🚀 Main Features
- User registration and login (with passwords hashed using SHA-256)
- User roles: **admin** and **user**
- CRUD operations for products (Create, Read, Update, Delete)
- Persistent storage using `.txt` or `.json` files
- Audit logging (`logs/log.txt`) that records user actions

## 🗂️ Folder Structure

data/ → Data files (users.txt, products.txt)  
logs/ → Action log file (log.txt)  
docs/ → Threat Model and documentation  
src/ → Source code  

## 👥 Authors
- Eli Samuel  
- [eayala2027@interbayamon.edu]

## 🐍 Language
Python 3.x

## ▶️ Execution (Simple Mode)
1. Activate the virtual environment:
   - Windows (PowerShell): `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
2. Run the program:
   ```bash
   python src/main.py

🧠 Project Objective

Develop a command-line mini-application that implements basic user authentication, access control, password hashing, and CRUD operations on an entity, demonstrating secure programming practices.