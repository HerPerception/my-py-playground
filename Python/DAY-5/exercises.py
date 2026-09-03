#===============================================
# EXERCISE 1
#===============================================
items = ["apple", "ball", "cat", "dog", "egg"]
for each_item in items:
    print(each_item)

print()
#===============================================
# EXERCISE 2
#===============================================
total_sum = 0
for i in range(5):
    total_sum += i
print(f"Total sum of 1 to 5 is {total_sum}")
print()

#===============================================
# EXERCISE 3
#===============================================
numbers = [10, 25, 5, 40, 18, 30]
threshold = 15

for each_num in numbers:
    if each_num > threshold:
        print(each_num)