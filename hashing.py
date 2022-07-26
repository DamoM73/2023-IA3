import hashlib

stored_password = hashlib.md5("Jayme".encode())

entered_password = input("Enter Password: ")
hashed_entered_password = hashlib.md5(entered_password.encode())

if hashed_entered_password.hexdigest() == stored_password.hexdigest():
    print("Logged in")
else:
    print("Wrong password")
    
print(hashed_entered_password.hexdigest())
print(stored_password.hexdigest())