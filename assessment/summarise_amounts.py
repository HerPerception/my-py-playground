def summarise_amounts(raw_values):
    total = 0
    rejected = 0

    for raw in raw_values:
        try:
            amount = int(raw)
            if amount >= 0:
                total += amount
            else:
                rejected += 1
        except ValueError:
            rejected += 1

    return {"total": total, "rejected": rejected}

assert summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]) == {
    "total": 15,
    "rejected": 3
}

assert summarise_amounts([]) == {
    "total": 0,
    "rejected": 0
}

assert summarise_amounts(["bad", "-2", ""]) == {
    "total": 0,
    "rejected": 3
}

assert summarise_amounts(["0"]) == {
    "total": 0,
    "rejected": 0
}

result = summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""])
print(result)

#==============================================================================
# Original Function
# def summarise_amounts(raw_values):
#     total = 0
#     for raw in raw_values:
#         try:
#             total += int(raw)
#         except:
#         pass

#     return {"total": total, "rejected": 0}

# Output for ["10", " 5 ", "bad", "-3", "0", ""] : {"total": 15, "rejected": 0}

# Defects of the Supplied Function
# 1. Negative values are incorrectly accepted -> total += int(raw)
# 2. rejected is never incremented -> {"total": total, "rejected": 0}
# 3. The bare except: is too broad -> except: pass. A bare except catches almost 
# any exception, not just the expected ValueError from int(raw)
# For example, if there were an unrelated programming error inside the try block, 
# the except: could silently swallow it. This makes bugs difficult to detect 
# because the program continues as though nothing went wrong.

# Why Checking Only total Could Miss a Bug
# Checking only total doesn't verify that invalid values are being counted as 
# rejected. total could be correct and rejected would be wrong.
#==============================================================================
