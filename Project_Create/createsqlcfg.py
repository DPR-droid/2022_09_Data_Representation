import os

# Request MySQL connection details from the user
host = input("Enter MySQL host: ")
user = input("Enter MySQL user: ")
password = input("Enter MySQL password: ")
database = input("Enter MySQL database: ")

# Create the dbconfig.py file with the MySQL connection details
with open("dbconfig.py", "w") as f:
    f.write("mysql = {\n")
    f.write(f"'host':'{host}',\n")
    f.write(f"'user':'{user}',\n")
    f.write(f"'password':'{password}',\n")
    f.write(f"'database':'{database}'\n")
    f.write("}")

print("dbconfig.py file created successfully.")