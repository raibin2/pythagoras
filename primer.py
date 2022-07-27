# coding=utf-8
import random

# R-1.1
# Write a short Python function, is multiple(n, m), that takes two integer values and returns
# True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def is_multiple(m, n):
    return True if m % n == 0 else False

print(is_multiple(10, 3))
print(is_multiple(10, 2))

# R-1.2
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even,
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return False if k & 1 else True

print(is_even(2))
print(is_even(3))

# R-1.3
#Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]

print(minmax(alpha))


# R-1.4
# Write a short Python function that takes a positive integer n and returns the sum of the squares
#  of all the positive integers smaller than n.


def sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total


print('sum of squares')
print(sum_of_squares(4))

# R-1.5
# give a single command that computes the sum from exercise r-1.4, relying on python's comprehension syntax and built in sum function

def sum_of_squares2(n):
    return sum([k * k for k in range(0, n+1)])


print(sum_of_squares2(4))

# R-1.6
#Write a short Python function that takes a positive integer n and returns the sum of the squares
# of all the odd positive integers smaller than n.


def sum_of_squares_odd(n):
    n -= 1
    total = 0
    while n > 0:
        if n % 2 != 0:
            total += n * n
        n -= 1
    return total


print('sum of squares odd')
print(sum_of_squares_odd(4))
# R-1.7

# give a single command that computes the sum from r-1.6, relying on python's comprehension syntax and built in sum function



def sum_of_squares_odd2(n):
    return sum([k * k for k in range(0, n) if k % 2 != 0])


print(sum_of_squares_odd2(4))


# R-1.8
# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used
# for index -n <= k < 0, what is the equivalent index j >= 0 such that s[j]
# references the same element?

s = "pythonstring"
n = len(s)

for k in range(-n, 0):
    print(s[k])


for j in range(-n, 0):
    print(s[j + n])

# R-1.9
# What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?

print(range(50, 90, +10))

# R-1.10
# what parameters should be sent to the range constructor to produce a range with values
# 8, 6, 4, 2, 0, -2, -4, -6, -8

print(range(8, -10, -2))

# R-1.11
# Demonstrate how to use Python's list comprehension syntax to produce the list
# [1, 2, 4, 8, 16, 32, 64, 128, 256].

print([pow(2, k) for k in range(0, 9, +1)])

# R-1.12

# Python's random module includes a function choice(data) that returns a random element
# from a non-empty sequence. The random module in- cludes a more basic function randrange,
# with parameterization similar to the built-in range function, that return a random choice
# from the given range. Using only the randrange function, implement your own version of the choice function.


def my_choice(data):
    return data[random.randrange(0, len(data) - 1)]


print(my_choice(alpha))

# C-1.13

# Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before, and compare
# this method to an equivalent Python function for doing the same thing.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp


print(my_list)

print(reverse(my_list))

# C-1.14
# Write a short Python function that takes a sequence of integer values and determines
# if there is a distinct pair of numbers in the sequence whose product is odd.

def odd_pair(data):
    count = 0
    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1
    return True if count >= 2 else False


evens = [2, 4, 6, 8]
print(odd_pair(my_list))
print(odd_pair(evens))

# C-1.15
# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def are_distinct(data):
    count = 0
    for k in data:
        for j in range(1, len(data) - 1):
            if k == j:
                count += 1
                if count == 2:
                    return False
    return True


print(are_distinct(evens))
print(are_distinct(alpha))

# C-1.18
# Demo list comprehension to create the following
# list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

print([k * (k - 1) for k in range(1, 11)])

# C-1.19
# Demonstrate how to use python's
# list comprehension syntax to produce
# the list [ a , b , c ,..., z ],without typing  characters literally.

print([chr(k) for k in range(97, 123)])

# C-1.20
# python's random module includes a function shuffle(data) that accepts a list
# of elements and randomly reorders the elements so that each possible order
# occurs with equal probability. The random module includes a more basic function
#  randint(a, b) that returns a uniformly random integer from a to b
# (including both endpoints). Using only the randint function,
#  implement your own version of the shuffle function.

def shufl(data):
    for k in range(0, len(data)):
        random_index = random.randint(0, k)
        tmp = data[random_index]
        data[random_index] = data[k]
        data[k] = tmp


shufl(alpha)
print(alpha)

# C-1.21
# Write a Python program that repeatedly reads lines from standard input until an EOFError
# is raised, and then outputs those lines in reverse order
#  (a user can indicate end of input by typing ctrl-D).

# done = False
# lines = []
#
# while not done:
# try:
#         line = raw_input('Enter text, i shall print it in reversed order, ctrl-d to stop')
#         lines.append(line)
#     except (EOFError):
#         for l in range(len(lines) - 1, -1, -1):
#             print(lines[l])
#             done = True

# C-1.22
# Write a short Python program that takes two arrays a and b of length n storing int values,
# and returns the dot product of a and b. That is, it returns an array c of length n such that
# c[i] = a[i]·b[i],
# for i = 0,...,n−1.

first = [1, 2, 3, 4]
second = [1, 2, 3, 4]


def dot_product(a, b):
    # assume n is the same for both
    c = []
    for k in range(0, len(a)):
        c.append(a[k] + b[k])
    return c


third = dot_product(first, second)

print(third)

# C-1.23
# Give an example of a Python code fragment that attempts
# to write an ele- ment to a list based on an index that may be out of bounds.
# If that index is out of bounds, the program should
# catch the exception that results, and print the following error message:
# “Don’t try buffer overflow attacks in Python!”


a_list = [1, 2, 3, 4]

try:
    a_list[4] = 5
except IndexError:
    print("Don't try buffer overflow attacks in Python")


# C-1.24
# Write a short Python function that counts the number of vowels in a given
# character string.
#
given_string = "There are 9 vowels in this string"
count = 0

for c in given_string:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == "u":
        count += 1

print(count)

# C-1.25
#WriteashortPython function thattakes astrings,representing asentence,
#and returns a copy of the string with all punctuation removed. For example,
#if given the string "Let s try, Mike.", this function would return "Lets try Mike".
#
given_string = 'Let\'s try, Mike.'

punctuations = ''''~!@#$%^*()_-{}[]|\:'";<>,./'''  # Take help of your keyboard to remember this.

newstring = ''
for i in given_string:
    if i not in punctuations:
        newstring += i

print(newstring)

#C-1.28 
# For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. 
#For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of√42 +32 =√16+9 =√25 = 5. 
#Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v.

n=[1,2,3,4,5] # You can create a custom list by using for loop and append

def norm(n,p=2):
    sum = 0
    for i in n:
        sum += i**p
    return sum ** (1/p)

print(norm(n))
print(norm(n,3))

You may assume that v is a list of numbers.


