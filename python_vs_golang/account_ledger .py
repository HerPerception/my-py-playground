def Account_Ledger_Analyser(transactions):
    total = sum(transactions)
    if total == 0:
        return [total, "BALANCED"]
    if total < 0:
        return [total, "DEBT"]
    if total > 0:
        return [total, "PROFIT"]
    # return total

val = Account_Ledger_Analyser([10, -25, -10, 25])
print(val)