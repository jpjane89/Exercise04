# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for i in some_list:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for i in some_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_list = []
    for i in word_list:
        if len(i) >= 4:
            long_list.append(i)
    return long_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = some_list[0]
    for i in some_list:
        if i < smallest:
            smallest = i
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]
    for i in some_list:
        if i > largest:
            largest = i
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halves_list = []
    for i in some_list:
        halves_list.append(i/2.0)
    return halves_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []
    for i in word_list:
        length_list.append(len(i))
    return length_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total_sum = 0
    for i in numbers:
        total_sum += i
    return total_sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    string = ''
    for i in string_list:
        string += i
    return string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return float(sum_numbers(numbers)) / len(numbers)