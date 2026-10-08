resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def parse_value(user_input):
    try:
        return int(user_input)
    except ValueError:
        print("Not a valid option. Choose from option numbers provided.")
        return None

def available_resource(resources_list, resource_identifier):
    for each_resource in resources_list:
        if each_resource["id"] == resource_identifier or each_resource["name"].lower() == resource_identifier.lower():
            return each_resource
    return None

def valid_ids(fellow_id, fellows_dict):
    if fellow_id not in fellows_dict:
        return "Invalid ID"
    return "valid"

def borrow_resource(resource_dict, quantity, fellow_id, records):
    if quantity <= 0:
        return "Quantity must be greater than zero."
    elif quantity > resource_dict["available"]:
        return "Insufficient available resource."
    else:
        resource_dict["available"] -= quantity
        records.append({"fellow_id": fellow_id, "resource_id": resource_dict["id"], "quantity": quantity})
        return f"Borrow successful! Available {resource_dict['name']}: {resource_dict['available']}."

def return_resource(fellow_id, resource_dict, quantity, records):
    if quantity <= 0:
        return "Rejected. Quantity can not be negative or zero."
    
    borrowed_quantity = sum(r["quantity"] for r in records if r["fellow_id"] == fellow_id and r["resource_id"] == resource_dict["id"])
    
    if quantity > borrowed_quantity:
        return "Rejected. Returned resources can not be more than the quantity borrowed."
    
    records.append({"fellow_id": fellow_id, "resource_id": resource_dict["id"], "quantity": -quantity})
    resource_dict["available"] += quantity
    return f"Return successful! Available {resource_dict['name']}: {resource_dict['available']}."

def search_resource(resources_list, search_term):
    results = [r for r in resources_list if search_term.lower() in r["name"].lower()]
    return results

def reports(resources_list, records):
    overall_unit = 0
    available = 0
    borrowed = 0
    low_resources = []
    
    borrowed_counts = {}
    for r in resources_list:
        amt_borrowed = sum(rec["quantity"] for rec in records if rec["resource_id"] == r["id"])
        borrowed_counts[r["name"]] = amt_borrowed

    max_borrowed_val = max(borrowed_counts.values()) if borrowed_counts else 0

    for each_resource in resources_list:
        overall_unit += each_resource["total"]
        available += each_resource["available"]
        amt_borrowed = sum(rec["quantity"] for rec in records if rec["resource_id"] == each_resource["id"])
        borrowed += amt_borrowed
        
        if each_resource["available"] < 3:
            low_resources.append({each_resource["name"]: each_resource["available"]})

    print(f"\n--- REPORT ---")
    print(f"overall_unit {overall_unit}")
    print(f"available {available}")
    print(f"borrowed {borrowed}")
    
    for each_resource in low_resources:
        for key in each_resource.keys():
            print(f"{key} low stock ({each_resource[key]})")

    for name, amt in borrowed_counts.items():
        if amt == max_borrowed_val and max_borrowed_val > 0:
            print(f"{name} is most borrowed ({amt})")

def main():
    print("Welcome!")
    while True:
        choice = input("Choose options. 1. Borrow 2. Return 3. Search 4. List/Report 5. Exit\n")
        user_input = parse_value(choice)
        
        if user_input == 5:
            break
            
        if user_input == 1:
            f_id = input("Input Fellow ID > ").strip()
            if valid_ids(f_id, fellows) != "valid":
                print("Invalid ID")
                continue
            res_input = input("Input resource name or ID > ").strip()
            resource = available_resource(resources, res_input)
            if resource is None:
                print("Resource not available")
            else:
                qty = parse_value(input("Input quantity > "))
                if qty is not None:
                    print(borrow_resource(resource, qty, f_id, borrow_records))

        elif user_input == 2:
            f_id = input("Input Fellow ID > ").strip()
            if valid_ids(f_id, fellows) != "valid":
                print("Invalid ID")
                continue
            res_input = input("Input resource name or ID > ").strip()
            resource = available_resource(resources, res_input)
            if resource is None:
                print("Resource not available")
            else:
                qty = parse_value(input("Input quantity > "))
                if qty is not None:
                    print(return_resource(f_id, resource, qty, borrow_records))
                    
        elif user_input == 3:
            search_term = input("Enter search term: > ").strip()
            results = search_resource(resources, search_term)
            print(f"Found: {results}" if results else "No matches found.")
            
        elif user_input == 4:
            reports(resources, borrow_records)

if __name__ == "__main__":
    main()
