# Question 1

# """
# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#  Hint: Consider use range(#begin, #end) method.
# """
# my_list = []
# for item in range(2000, 3201):
#     if item % 7 == 0 and item % 5 != 0:
#         my_list.append(item)
# print(my_list)
#
# print(list(filter(lambda item: item % 7 == 0 and item % 5 != 0, range(2000, 3201))))
#
# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

# Question 2

# """
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
# """
# import math
#
# n = int(input('Enter num for factorial '))
# n1 = n
#
# print(math.factorial(n))
#
# factorial1 = 1
# for i in range(2, n + 1):
#     factorial1 *= i
# print(factorial1)
# factorial2 = 1
#
# while n > 1:
#     factorial2 *= n
#     n -= 1
# print(factorial2)
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
#
#
# print(factorial(n1))

# Question 3

# """
# With a given integral number n, write a program to generate a dictionary that contains
# (i, i x i) such that is an integral number between 1 and n (both included). and then
# the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hint: In case of input data being supplied to the question,
# it should be assumed to be a console input.Consider use dict()
# """

# try:
#     your_num = int(input('Enter your number to create new dict '))
# except ValueError as err:
#     print(f'Use number {err}')
#
#
# def create_dict(num):
#     test_dict = {}
#     my_range = range(1, num + 1)
#     for i in my_range:
#         test_dict.update({i: i * i})
#     return test_dict
#
#
# print(create_dict(your_num))
#
#
# def create_dict2(num):
#     test_dict = {}
#     my_range = range(1, num + 1)
#     for i in my_range:
#         test_dict[i] = i * i
#     return test_dict
#
#
# print(create_dict2(your_num))
#
# test_dict2 = {i: i * i for i in range(1, your_num + 1)}
# print(test_dict2)
#
# print(dict(enumerate([i * i for i in range(1, your_num + 1)], 1)))

# Question 4

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
# In case of input data being supplied to the question,
# it should be assumed to be a console input.tuple() method can convert list to tuple


# def return_list_and_tuple(counter):
#     my_list = []
#     while counter != 0:
#         try:
#             my_list.append(int(input(f'Enter your data for list left {counter} \n')))
#             counter -= 1
#         except ValueError as err:
#             print(f'Use number {err}')
#     my_tuple = tuple(my_list)
#     return my_list, my_tuple
#
#
# print(return_list_and_tuple(6))

# my_list2 = list(input('Enter your data ').split(','))
# my_tuple2 = tuple(my_list2)
# print(my_list2, my_tuple2)

# Question 5

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints: Use init method to construct some parameters

# class MyString():
#
#     def __init__(self):
#         self.x = ''
#
#     def get_string(self):
#         self.x = input('Enter your string \n')
#
#     def print_string_uper(self):
#         print(self.x.upper())
#
#
# test_str = MyString()
# test_str.get_string()
# test_str.print_string_uper()
# print(test_str)

# Question 6

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.For example Let us assume the following comma separated input sequence is
# given to the program: 100,150,180
# The output of the program should be: 18,22,24

# Hint: If the output received is in decimal form, it should be rounded off
# to its nearest value (for example, if the output received is 26.0, it should be printed
# as 26).In caseof input data being supplied to the question,
# it should be assumed to be a console input.

# from math import sqrt

# c = 50
# h = 30
# my_list = input('Enter values using coma ').split(',')
# new_list = []
# for d in my_list:
#     new_list.append(str(round(sqrt((2 * c * int(d) / h)))))
# print(','.join(new_list))

# Qestion 7
'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i _ j.*
Note: i=0,1.., X-1; j=0,1,¡Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hint: Note: In case of input data being supplied to the question,
it should be assumed to be a console input in a comma-separated form.
'''

# x,y = map(int,input('enter values').split(','))
# my_list = []
#
# for i in range(x):
#     tmp = []
#     for j in range(y):
#         tmp.append(i*j)
#     my_list.append(tmp)
#
# print(my_list)

# Question 8

'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# my_list = sorted(list(input('Enter your words using coma \n').split(',')))
# print(','.join(my_list))
#
# def my_func(e):
#     return e[0]
#
# my_list = input('Enter a comma separated string: ').split(",")
# my_list.sort(key=my_func)
# print(",".join(my_list))

# Question 9
'''
Write a program that accepts sequence of lines as input and 
prints the lines after making all characters in the sentence capitalized.

'''
# text = list(input('to separate line use come ').split(','))
# test_list = []
# for i in text:
#     test_list.append(i.upper())
#
# print('\n'.join(test_list))

# def user_input():
#     while True:
#         x = input()
#         if not x:
#             break
#         yield x
# print(*(line.upper() for line in user_input()), sep='\n')

# Question 10
'''
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
'''
# word1 = set(input().split(' '))
# list(word1).sort()
# print(' '.join(word1))
#
# word2 = sorted(list(set(input().split())))
# print(' '.join(word2))
#
# word3 = input().split()
# for i in word3:
#     if word3.count(i) > 1:
#         word3.remove(i)
#
# word3.sort()
# print(" ".join(word3))

# Question 11

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Answer:1010
'''

# my_list = input().split(',')
#
#
# def bin2dec(s):
#     i = 0
#     d = 0
#     while len(s) > 0:
#         d = d + int(s[-1]) * 2 ** i
#         i = i + 1
#         s = s[:-1]
#     return d
#
# print(*(i for i in my_list if bin2dec(i) % 5 == 0), sep=',')
# a = '0100'
# x = int(a,2)
# print(x)

# Question 12

'''
Write a program, which will find all such numbers between 1000 and 3000 (both included)
 such that each digit of the number is an even number.
 The numbers obtained should be printed in a comma-separated sequence on a single line.
 
 Hint: In case of input data being supplied to the question, it should be assumed to be a console input
'''
# selected_value = []
# for i in range(1000, 3001):
#     check = 0
#     for x in str(i):
#         if ord(x) % 2 != 0:
#             check = 1
#     if check == 0:
#         selected_value.append(str(i))
# print(','.join(selected_value))
#
# selected_value1 = [str(i) for i in range(1000, 3001)]
# selected_value1 = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), selected_value1))
# print(",".join(selected_value1))

# Question 13
'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
Answer:
LETTERS 10
DIGITS 3
'''
# our_str = input()
# letters = 0
# digits = 0
# for i in our_str:
#     if i.isdigit():
#         digits +=1
#     elif i.isalpha():
#         letters +=1
# print(f'LETTER {letters} \nDIGIT {digits}')
#
# import re
#
# input_string = input('> ')
# print()
# counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}
#
# print(counter)

# Question 14
'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program: Hello world!
Answer: 
UPPER CASE 1
LOWER CASE 9
'''
# my_input = input('Enter data:\n')

# def summ_upper_low(some_str):
#     upper_case = 0
#     lower_case = 0
#     for i in some_str:
#         if i.isalpha() and i.islower():
#             lower_case += 1
#         elif i.isalpha() and i.isupper():
#             upper_case += 1
#     print(f'Upper case {upper_case} \nLower case {lower_case}')
#
# summ_upper_low(my_input)

# Question 15
'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program: 9
Then, the output should be: 11106
'''
# from functools import reduce
#
# x = input('please enter a digit:')
# print(reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1,5)]))
#
# sum = 0
# for i in range(1,5):
#     sum = sum + int(x*i)
# print(sum)

# Question 16

'''
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. 
Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
Then, the output should be: 1,9,25,49,81
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# our_list = input().split(',')
# shown_list =[]
# for i in our_list:
#     if int(i) % 2 !=0:
#         shown_list.append(str(pow(int(i),2)))
# print(','.join(shown_list))
#
# lst = [str(int(i)**2) for i in input().split(',') if int(i)%2!=0]
# print(','.join(lst))

# Question 17

'''
Write a program that computes the net amount of a bank account
 based a transaction log from console input. 
 The transaction log format is shown as following: D 100 W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500
Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# def user_transactions():
#     total = 0
#     while True:
#         x = input().split()
#         if not x:
#             break
#         type, value = map(str, x)
#         if type =='D':
#             total +=int(value)
#         else:
#             total -=int(value)
#     print(total)
# user_transactions()

# Question 18

'''
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# import re
# a = None
# while a == None:
#     password = input('Enter your pass (use a-Z@#$% and min 8 sings): ')
#     password_patern = re.compile(r'[a-zA-Z0-9@%$#]{8,}\d$')
#     a = password_patern.fullmatch(password)
#     if a != None:
#         break
#     else:
#         print('You wrote wrong password')
# print('You may use it password')

# import re
# pas_list = input().split(',')
# print(pas_list)
# match_pas = []
# for i in pas_list:
#     pas_patern = re.compile('(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}')
#     if pas_patern.fullmatch(i):
#         match_pas.append(i)
# print(','.join(match_pas))

# Question 19

'''
You are required to write a program to sort the (name, age, score) tuples by
 ascending order where name is string, age and score are numbers. 
The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
# from operator import itemgetter
# list_of_tuple =[]
# while True:
#     element = tuple(input('Enter data:\n').split(','))
#     if not element[0]:
#         break
#     list_of_tuple.append(element)
# list_of_tuple = [('Tom','19','80'), ('John','20','90'), ('Jony','17','91'), ('Jony','17','93'), ('Json','21','85')]
# list_of_tuple2 = list_of_tuple
# list_of_tuple.sort(key=lambda x:(x[0], x[1], x[2]))
# list_of_tuple2.sort(key=itemgetter(0,1,2))
# print(list_of_tuple)

# Question 20

'''
Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.
Suppose the following input is supplied to the program: 7
Then, the output should be:
0
7
14
Hints: Consider use class, function and comprehension.
'''

# class MyGen():
#     current = 0
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 7
#             return num
#         raise StopIteration
#
#
# for i in MyGen(0, 100):
#     print(i)
#
#
# class MyGen2():
#     def seven(self, num):
#         for i in range(num):
#             if i % 7 == 0:
#                 yield i
#
#
# for i in MyGen2().seven(100):
#     print(i)

# Question 21
'''
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps.
Please write a program to compute the distance from current position 
after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Here distance indicates to euclidean distance.Import math module to use sqrt function.
'''
# from math import sqrt
# moving = []
# x,y = (0, 0)
# while True:
#     a = input().split()
#     if not a:
#         break
#     moving.append(a)
# for i in moving:
#     if i[0] == 'UP':
#         x +=int(i[1])
#     elif i[0] == 'DOWN':
#         x -=int(i[1])
#     elif i[0] == 'LEFT':
#         y -=int(i[1])
#     elif i[0] == 'RIGHT':
#         y +=int(i[1])
# short_distance_from_start = round(sqrt((x**2) + (y**2)))
# print(short_distance_from_start)

# Question 22

'''
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints: In case of input data being supplied to the question,
it should be assumed to be a console input.
'''
# some_dict = {}
# some_str = sorted(input().split())
# for i in some_str:
#     some_dict.update({i: (some_str.count(i))})
# for key, value in some_dict.items():
#     print(key, value, sep=':')

# Question 23

'''
Write a method which can calculate square value of number.
Hints: Using the ** operator which can be written as n**p where means n^p
'''

# def calculate_square(n, p):
#     return n ** p
# print(calculate_square(4, 4))

# Question 24

'''
Question:
Python has many built-in functions, and if you do not know how to use it,
 you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents,
 such as abs(), int(), raw_input()

And add document for your own function

Hints:
The built-in document method is __doc__
'''

# print(abs.__doc__)
# print(int.__doc__)
# print(map.__doc__)

# Question 25

'''
Define a class, which have a class parameter and have a same instance parameter.
'''


# class Car:
#     name = 'Car'
#
#     def __init__(self, name = None):
#         self.name = name
#
#
# ford = Car('Edge')
#
# print('%s name is %s' % (Car.name, ford.name))
#
# vw = Car()
# vw.name = 'Golf'
#
# print('%s name is %s' % (Car.name, vw.name))

