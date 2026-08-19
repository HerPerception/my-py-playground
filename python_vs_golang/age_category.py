def Age_category(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 18:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print(Age_category(18))
print(Age_category(70))
print(Age_category(14))