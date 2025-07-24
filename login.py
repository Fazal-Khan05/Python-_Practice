import os
import time 
set_username = input("Enter your username: ")
set_password = input("Enter your password: ")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("Login below !")

username = input("Username: ")
password = input("Password: ")
if username == set_username and password == set_password:
    print("Login successful!")
else:
    print("Login failed! Please check your username and password.")