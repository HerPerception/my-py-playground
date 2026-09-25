def staircase(n):
    count = 0
    i = 1
    while count < n:
        text = ' ' * (n - i)
        text += '#' * i
        print(text)
        count+=1
        i+=1

staircase(6)
