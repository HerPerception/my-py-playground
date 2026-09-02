import sys
age = input("Welcome to the Otukpo Grant  application page. Enter age to check eligibility: \n")

try:
    age = int(age)
except ValueError:
    print("Invalid age input.")
    sys.exit()

if age < 18:
    print("Not eligible at this time")
else:
    print("Congratulations! You can now go on with the application process.")