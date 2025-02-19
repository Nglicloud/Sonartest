import os

# 🚨 1. Syntax Error - Missing colon (SyntaxError)
def greet(name)
    print("Hello, " + name)

# 🚨 2. Security Vulnerability - Hardcoded Password
DB_PASSWORD = "SuperSecret123"  # Hardcoded credentials are unsafe

# 🚨 1. Syntax Error - Missing colon (SyntaxError)
def greet(name)
    print("Hello, " + name)

# 🚨 2. Security Vulnerability - Hardcoded Password
DB_PASSWORD = "SuperSecret123"  # Hardcoded credentials are unsafe

def connect_to_db():
    # 🚨 3. Security Vulnerability - SQL Injection Risk
    user_input = input("Enter username: ")
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    print("Executing query:", query)  # Debugging statement (should be removed)
    return query  # Fake DB call for demonstration

# 🚨 4. Duplicate Code - Repeated function
def add_numbers(a, b):
    return a + b

def sum_numbers(a, b):  # Duplicate of add_numbers()
    return a + b

# 🚨 5. Code Smell - Large Function with Multiple Responsibilities
def process_data(data):
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item * 2)
        else:
            result.append(item * 3)
    print("Processed data:", result)  # 🚨 Code Smell - Print statement in function
    log_data(result)  # 🚨 Function should not handle logging

# 🚨 6. Poor Exception Handling - Catching all exceptions blindly
try:
    x = 5 / 0  # This will cause a division by zero error
except:
    print("Something went wrong!")  # 🚨 Bad practice: Hides the actual error

# 🚨 7. Unused Variable
unused_var = 100  # This variable is never used

# 🚨 8. Function Without a Return Statement (Bad Practice)
def faulty_function():
    x = 10  # Function does nothing

# 🚨 9. Hardcoded File Paths (Security Issue)
def read_file():
    file = open("/home/user/secret.txt", "r")  # Hardcoded path
    print file.read()

