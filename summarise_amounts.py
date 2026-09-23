def summarise_amounts(raw_values):
    rejected = 0
    total = 0
    for raw in raw_values:
        try:
            temp = int(raw)
           
        except ValueError:
            rejected += 1
            continue
        if temp < 0:
                rejected += 1
        else:
                total += temp
    return {"total": total, "rejected": rejected}

result = summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""])
print(result)
