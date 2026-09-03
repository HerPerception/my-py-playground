def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count  # Pauses here and returns the current count
        count += 1   # Resumes here on the next call

# Using the generator in a loop
for number in count_up_to(5):
    print(number)

# executable_list = ["e", "a", "c", "h"]
# for item in executable_list:
#     yield item

# Output:
# 1
# 2
# 3
