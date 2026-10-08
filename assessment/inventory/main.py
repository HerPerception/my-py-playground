items = [2, 4, 6]
result = []
for item in items:
    if item % 4 == 0:
        continue
    result.append(item * 2)
print(result)

# def borrow(resource, quantity):
#     resource["available"] -= quantity
#     if resource["available"] < 0:
#         return "Not enough stock"
#     return "Success"


transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def total_quantity(transactions_dict):
    fellows_dict = {}
    for each_dict in transactions_dict:
        name = each_dict["fellow"]
        quantity = each_dict["quantity"]
        if name in fellows_dict:     
            fellows_dict[name] += quantity
        else:
            fellows_dict[name] = quantity
    return fellows_dict

print(total_quantity(transactions))


resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]
resources = [item for item in resources if item["available"] != 0]
print(resources["name"])

