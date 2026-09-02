login_name = "Joriel"
login_password = "secret12345"

name = input("Name: ")
password = input("Password: ")
if name == "" or password == "":
    print("Field can not be empty. Input name and password.")
elif name != login_name and password != login_password:
    print("Name or password incorrect. Try again.")
else:
    print("Login Successful!")