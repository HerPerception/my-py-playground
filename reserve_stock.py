def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if item not in remaining:
            raise ValueError("Item does not exist in stock.")
            continue
        if quantity > remaining[item]:
            raise ValueError("Insufficient stock")
        if quantity <= 0:
            raise ValueError("Quantity can not be 0")
        
        remaining[item] = remaining[item] - quantity
    return remaining, stock

stock = {"pen": 5}
order = [("pen", 3), ("pen", 2), ("bic", 2)]
result, newresult = reserve_stock(stock, order)
print(result, newresult)
