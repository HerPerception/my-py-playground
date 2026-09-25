def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if num < 0:
            neg += 1
        elif num > 0:
            pos += 1
        elif num == 0:
            zero += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zero/len(arr))
