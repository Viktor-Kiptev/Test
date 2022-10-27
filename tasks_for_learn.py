# 1 """
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

# 2 """
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

#3 """
# With a given integral number n, write a program to generate a dictionary that contains
# (i, i x i) such that is an integral number between 1 and n (both included). and then
# the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hint: In case of input data being supplied to the question,
# it should be assumed to be a console input.Consider use dict()
# """
