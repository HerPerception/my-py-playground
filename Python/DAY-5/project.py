#=======================================================================================================
#Create a program that processes five fictional sales amounts and reports the total, largest amount, and
#number of sales above a chosen threshold.
#=========================================================================================================

sale_amounts = [45.99, 120.50, 15.00, 340.25, 89.99, 12.50, 550.00, 78.40, 210.10, 99.99]
total = 0
largest_amount = 0
threshhold = 50
sales_above_threshhold = 0

for sale in sale_amounts:
    total += sale
    if sale > largest_amount:
        largest_amount = sale
    if sale >= threshhold:
        sales_above_threshhold += 1

print(f"The total is {total}")
print(f"The largest amount is {largest_amount}")
print(f"The sales above threshhold is {sales_above_threshhold}")
