#This is for set - unordered.
my_set = {7, 'hello', 8.5}
print(my_set)

#This is for Dictionary.
my_dict = {'name': 'Alice', 'age': 25}
my_dict['yesterday'] = 'yes'
print(my_dict)

#This is for Tuple.
my_tuple = (2, 'hello', 7.5, 'nothing')
print(my_tuple)

#This is for range.
my_range = range(10)
print(my_range)

#This is for list.
my_list = [22, 'Hello', 3.14, True]
print(my_list)

#To get the type of a variable, use type()
print(type(my_set))

#To check if a variable's value matches a specific data type, use isinstance()
#You can check for multiple datatypes, it will return 
# True if any of the datatypes provided matches.
print(isinstance(my_set, (str, int)))

#To check if a character exists in a string, use in.
my_str = 'Hallo'
print('s' in my_str)

#To get length of a string or any of the other data types, use len.
print(len(my_str))
print(len(my_set))

#To get the position of each character in a string, use [index]
#Negative indexing is also allowed.
print(my_str[0])
#This would print the 3rd value from behind.
print(my_str[-3])

#String is an immutable data type. You can point its variable
# to something new but you can't change the original object by
#adding, removing or replacing any of its elements.

#For instance, this works:
greeting = 'Hello'
greeting = 'hi'

#But this doesn't:
# greeting = 'hello'
# greeting[0] = 'e'
# print(greeting)
# It throws this error: TypeError: 'str' object does not support item assignment

#String Concatenation
#Strings can only be concatenated with strings. To concatenate
#a different data type, you have to convert it to the string representation
#of the given object using str().
str_concat = 'Alice is ' + 'just 8 years old!' 
age  = 8
str_concat = 'Alice is ' + str(age)
print(str_concat)

#You could also use the augmented assignment operator += for concatanation
details = 'John Dee '
age = 24
details += str(age)
print(details)

#String Repitition
sound = 'ha'
str_repeat = sound * 3
print(str_repeat)

#String interpolation is the process of inserting variables and expressions
#into a string. F-strings also known as formatted string literals allows you 
#to do this. It starts with f before the quotes.
intro = f'My name is Dee and I am {age} years old today.'
instruct = f'Print {my_set} and {my_list}.'
print(intro)
print(instruct)
#Notice how you don't need to convert the non-string types to string,
#it is done under the hood during the interpolation process.

#To slice a string, string[start:stop], stop index is excluded.
my_str = my_str[0:2]
print(my_str)
print(len(my_str))
#Giving a stop index greater than the length of the string would have
# it reset to 0. This is done under the hood.
my_str = my_str[0:5]
print(my_str)
print(len(my_str))#Length of my_str is 2
#Omitting the start index gives it a default of 0
my_str = 'Hello there'
my_str = my_str[:4]
print(my_str)
#Omitting the stop index gives it a default of len(string)
my_str = 'Joseph'
my_str = my_str[0:]
print(my_str)
#Omitting the start and stop index gives them a default of 0 and len(string).
my_str = 'John'
my_str = my_str[:]
print(my_str)
#There's also an optional step parameter used to specify 
#the increment between each index in the slicing.
my_str = 'Joseph is really young'
my_str = my_str[0:21:2]
print(my_str)#Jsp sral on: J_s_p_ _s_r_a_l_ _o_n_ > Jumping two steps every time.
#Let's reverse a string with this.
my_str = 'Nothing to do'
my_str = my_str[len(my_str):0:-1]
print(my_str)
#Or this.
my_str = 'Nothing to do'
my_str = my_str[::-1]
print(my_str)

#A method is a function that belongs to a specific object or class.
#Like upper() is a method of the str class.
my_str = my_str.upper()
print(my_str)
#Other methods are lower(), strip() which removes trailing or leading spaces,
#replace(old, new) replaces every occurrences of old with new.
#split() splits a string on a specified seperator. If no seperator is specified, it splits
#on whitespace.
#join(iterable) joins element of an iterable like lists into a string with a seperator.
join_str = ' '.join(my_list)
print(join_str)


