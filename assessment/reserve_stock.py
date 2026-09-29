def reserve_stock(stock, order):
    remaining = stock.copy()

    for item, quantity in order:
        if item not in stock:
            raise ValueError("Unknown item")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > remaining[item]:
            raise ValueError("Insufficient stock")

        remaining[item] -= quantity

    return remaining

stock = {"pen": 5}
order = [("pen", 3), ("pen", 2), ("bic", 2)]
result, newresult = reserve_stock(stock, order)
print(result, newresult)

# 1. Successful repeated items
stock = {"pen": 10, "book": 5}
result = reserve_stock(stock, [("pen", 3), ("pen", 2)])

assert result == {"pen": 5, "book": 5}
assert stock == {"pen": 10, "book": 5}


# 2. Repeated items exceed stock
stock = {"pen": 5}

try:
    reserve_stock(stock, [("pen", 3), ("pen", 3)])
    assert False, "Expected ValueError"
except ValueError:
    pass

assert stock == {"pen": 5}


# 3. Unknown item
stock = {"pen": 5}

try:
    reserve_stock(stock, [("pencil", 1)])
    assert False, "Expected ValueError"
except ValueError:
    pass


# 4. Zero quantity
stock = {"pen": 5}

try:
    reserve_stock(stock, [("pen", 0)])
    assert False, "Expected ValueError"
except ValueError:
    pass

# ===================================================================================================================================================================================================
# Original Function

# def reserve_stock(stock, order):
#     remaining = stock.copy()
#     for item, quantity in order:
#         if quantity > stock[item]:
#             raise ValueError("Insufficient stock")
#         remaining[item] = stock[item] - quantity
#     return remaining

# With stock = {"pen": 5}, trace order = [("pen", 3), ("pen", 3)], the supplied code incorrectly succeeds because it checks each request against the oriiginal stock, rather than the already-reduced
# remaining stock.

# Other validation gaps:

# 1. It fails to validate an unknown item. ("pencil", 1)
# 2. Zero quantity. Should raise ValueError. ("pen", 0)
# 3. Negative quantity. ("pen", -2)
# 4. Repeated items. It doesn't accumulate reservations correctly because each calculation uses stock[item] rather than the updated remaining[item]. Availability must be checked against the 
# progressively reduced remaining stock, not the original stock.

# Why Editing a Local Copy Protects the Caller When a Later Line Fails: 
# stock.copy() creates a separate dictionary for the function to modify, so only remaining (the copied dicitionary) is modified.
# ====================================================================================================================================================================================================
