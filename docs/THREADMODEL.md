# 🧩 Threat Model – Secure Inventory App

## 🎯 Purpose
This Threat Model identifies potential risks in the Secure Inventory App (CLI) and defines the controls implemented to mitigate them.

---

## 📦 Assets (Things to protect)
| ID  | Asset                | Description                                      |
|-----|--------------------|--------------------------------------------------|
| A1  | User credentials     | Usernames and hashed passwords in `data/users.txt` |
| A2  | Inventory data       | Product info (name, quantity, price) in `data/products.txt` |
| A3  | Log file             | Audit logs of user actions and errors in `logs/log.txt` |
| A4  | Program integrity    | Source code and logic enforcing access control |

---

## ⚠️ Threats (Possible attacks)
| ID  | Threat                | Description |
|-----|---------------------|-------------|
| T1  | Brute force login     | Repeated attempts to guess passwords |
| T2  | Data manipulation     | Manual modification of `.txt` files to alter users or products |
| T3  | Unauthorized access   | Regular users trying to perform admin-only actions |
| T4  | Injection attempts    | Malicious input like `' OR 1=1 --` |
| T5  | Overflow / underflow  | Input exceeding expected limits causing logic errors |
| T6  | Log tampering         | Deleting or altering audit logs |

---

## 🕳️ Vulnerabilities (Weak points)
| ID  | Vulnerability         | Description |
|-----|--------------------|-------------|
| V1  | Plaintext input validation | User input not properly validated |
| V2  | Weak password handling      | Storing raw or unhashed passwords |
| V3  | File permissions           | Data files readable/editable by anyone |
| V4  | Missing access control     | Lack of role-based restrictions |
| V5  | Poor error handling        | Displaying stack traces or sensitive info |

---

## 🛡️ Controls (Mitigations implemented)
| ID  | Control               | Description |
|-----|---------------------|-------------|
| C1  | Password hashing       | Use SHA-256 to store passwords securely |
| C2  | Input validation       | Validate type, length, and format of user input |
| C3  | Role-based access control | Admin and user roles restrict sensitive actions |
| C4  | Logging and auditing    | Record all CRUD actions and login attempts |
| C5  | Error handling          | Show friendly messages without sensitive info |
| C6  | File integrity checks   | Prevent unauthorized changes to data files |

---

## ✅ Summary
By applying **secure coding practices**, validating all user input, and hashing passwords, the Secure Inventory App minimizes risks of unauthorized access, data corruption, and injection attacks.
