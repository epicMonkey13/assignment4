# Gulmira Z 26/09/2022 Worksheet
# python string exercises
def palindrome(a):
    # finding the mid, start
    # and last index of the string
    mid = (len(a) - 1) // 2  # you can remove the -1, or you add <= sign in line 21
    start = 0  # so that you can compare the middle elements also.
    last = len(a) - 1
    flag = 0

    # A loop till the mid of the
    # string
    while start <= mid:

        # comparing letters from right
        # from the letters from left
        if a[start] == a[last]:

            start += 1
            last -= 1

        else:
            flag = 1
            break

    # Checking the flag variable to
    # check if the string is palindrome
    # or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")


# Function to check whether the
# string is symmetrical or not
def symmetry(a):
    n = len(a)
    flag = 0

    # Check if the string's length
    # is odd or even
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid

    while start1 < mid and start2 < n:

        if a[start1] == a[start2]:
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")


# Driver code
string = 'Gulmira'
palindrome(string)
symmetry(string)

# To reverse words in a given string
string = "apple banana cherries"
# reversing words in a given string
s = string.split()[::-1]
list_of_words = []
for i in s:
    # appending reversed words to l
    list_of_words.append(i)
# printing reverse words
print(" ".join(list_of_words))

# ways to remove i'th character from string in Python
test_str = "Cats like milk"

# Removing char at pos 5
new_str = ""

for i in range(len(test_str)):
    if i != 5:
        new_str = new_str + test_str[i]

# Printing string after removal
print("The string after removal of i'th character : " + new_str)

# finding len of a string (4 ways)
my_string = "Gleb"
print(len(my_string))


def find_len(my_string_2):
    counter = 0
    for i in my_string_2:
        counter += 1
    return counter


my_string_2 = "Barcelona"
print(find_len(my_string_2))


def find_len_method_3(my_string_three):
    counter = 0
    while my_string_three[counter:]:
        counter += 1
    return counter


my_string_3 = "London"
print(find_len_method_3(my_string_3))


def find_len_method_4(my_city):
    if not my_city:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(my_city)).count(some_random_str) + 1


a = "Kash"
print(find_len_method_4(a))

# Python Tuple exercises
# find tuple size
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deanship")
Tuple3 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))

# print the sizes of sample Tuples
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")
print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")
print("Size of Tuple3: " + str(Tuple3.__sizeof__()) + "bytes")

# max and min K elements in Tuple
test_tup = (5, 20, 3, 7, 6, 8)

print("The original tuple is : " + str(test_tup))

# initializing K
K = 2
# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()
test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])

print("The extracted values : " + str(res))

# sum of tuple elements
test_tup = ([7, 8], [9, 1], [10, 7])

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))

print("The sum of tuple elements are : " + str(res))

# Row-wise element Addition in Tuple Matrix
test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Custom eles
cus_eles = [6, 7, 8]

# Row-wise element Addition in Tuple Matrix
# Using enumerate() + list comprehension
res = [[sub + (cus_eles[idx],) for sub in val] for idx, val in enumerate(test_list)]

# printing result
print("The matrix after row elements addition : " + str(res))

# Create a list of tuples from given list having number and its cube in each tuple
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, val ** 3) for val in list1]

# print the result
print(res)


# Python dictionary exercises
# sort by key
def dictionairy():
    # Declare hash function
    key_value = {}

    # Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")

    print("key_value", key_value)

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")


def main():
    # function calling
    dictionairy()


# Main function calling
if __name__ == "__main__":
    main()


def dictionairy():
    # Declaring the hash function
    key_value = {}

    # Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value", key_value)

    print("Task 2:-\nKeys and Values sorted in",
          "alphabetical order by the key  ")

    # sorted(key_value) returns an iterator over the
    # Dictionary’s value sorted in keys.
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


def main():
    # function calling
    dictionairy()


# main function calling
if __name__ == "__main__":
    main()

# handling missing keys
import collections

# declaring default dict
# sets default value 'Key Not found' to absent keys
defd = collections.defaultdict(lambda: 'Key Not found')

# initializing values
defd['a'] = 1

# initializing values
defd['b'] = 2

# printing value
print("The value associated with 'a' is : ", end="")
print(defd['a'])

# printing value associated with 'c'
print("The value associated with 'c' is : ", end="")
print(defd['c'])

# dict with keys having multiple inputs, an example with long and lat
places = {("19.07'53.2", "72.54'51.0"): "Mumbai",
          ("28.33'34.1", "77.06'16.6"): "Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)


# find the sum of all items in a dict
def returnSum(dict):
    return sum(dict.values())


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

# find the size of a dict
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# print the sizes of sample Dictionaries
print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")
print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")

# Python set exercises
# find the size of a set
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), (2, "Tiger"), (3, "Fox")}

# print the sizes of sample Sets
print("Size of Set1: " + str(Set1.__sizeof__()) + "bytes")
print("Size of Set2: " + str(Set2.__sizeof__()) + "bytes")
print("Size of Set3: " + str(Set3.__sizeof__()) + "bytes")

# iterate over a set
test_set = set("geEks")

for val in test_set:
    print(val)


# max and min in a set
def MAX(sets):
    return (max(sets))


# Driver Code
sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(MAX(sets))


def MIN(sets):
    return (min(sets))


# Driver Code
sets = set([4, 12, 10, 9, 4, 13])
print(MIN(sets))


# remove items from a set
def Remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)


# Driver Code
initial_set = set([12, 10, 13, 15, 8, 9])
Remove(initial_set)

# check if 2 lists have at least one element in common
def common_data(list1, list2):
    result = False

    # traverse in the 1st list
    for x in list1:

        # traverse in the 2nd list
        for y in list2:

            # if one common
            if x == y:
                result = True
                return result

    return result


# driver code
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))
