# Fundamental Data types
# bool
# str
# list
# tuple
# set
# dict
# x=(int(2+2))
# print(type(2+6))
# print(type(8-20))
# print(type(2*8))
# print(9.1+ 1.1)

# print(3**3) # возведение в степень
# print(2//4) # деление без остатка
# print(9%2)

# Operator precedence

# ()
# **
# * /
# +-
# print(bin(5))
# print(int('0b101',2))
# user_iq=190
# print(user_iq)

# some_value = 42.5
# some_value %= 10
# print(some_value)

# print(type('Hollo'))
# username = 'Viktor'
# userpassword = 'password'
# londstring = '''

# WOW

# 0 0
# ___
# '''
# print(londstring)

# Type Conversion
# print(type(str(100)))

# #Escape Sequence
# weather = 'It\'s "kind of" weather"'
# print(weather)

# Formatted strings
# name = 'Viktor'
# age = 55
# print('Hi {}. You are {} years old'.format('Viktor', age))

# str

# test = '0123456789'
# # test[start:stop:stepover]
# print(test[0:10:2])
# print(test[0])

# first_string = input()
# second_string = input()
# main_string = first_string  + second_string
# print(main_string)
# print('Lent of main string =', (len(main_string)))

# qoute = 'to be or no to be'
# print(qoute.upper())
# print(qoute.capitalize())
# print(qoute.())

# booleans

# name = input()
# check_name = input()
# match = name == check_name
# print(match)

# conversation calues
# year=input('what year were you born? ')
# birth_year=int(year)
# age=(2022-birth_year)
# print('Your age is', (age), 'years old.')


# user_name = input('Enter your name: ')
# password = input('Enter your password: ')
# lenght_password = len(password)
# secret = '*' * lenght_password
# print('Hey {} your password {} is {} lethers long.'.format(user_name, secret, lenght_password))

# Data structure LIST
# li = [1, 2, 3, 4]
# li2 = ['a', 'b', 'c']
# li3 = [1, 'a', True]

# amazon_card = [
# 'glass',
# 'book',
# 'notebooks',
# 'game',
# 'toys'
# ]
# amazon_card[0] = 'laptor'
# print(amazon_card[0:6:2])
# print(amazon_card)
# print(amazon_card[1:3])

# Matrix
# matrix = [
#    [1,5,1],
#    [0,8,0],
#    [1,0,1]
#  ]

# print(matrix[1][1])

# basket = [1,2,3,4,5]

#  adding

# new_list = basket.append(100)
# print(basket)
# new_list = basket.insert(3, 50)
# print(basket)
# new_list = basket.extend([80,90,100,10.1])
# print(basket)

# removing

# basket = [1,2,3,4,5]
# # basket.pop()
# # basket.pop(0)
# # basket.remove(4)
# new_list = basket.pop(4)
# new_list = basket.clear()
# print(new_list)
# print(basket)

# basket = [1, 2, 3]
# print(1 in basket)

# basket = ['a','b', 'f', 'c','d', 'a','f']
# print(basket.index('c', 0, 4))
# print(basket.count('b'))
# basket.sort()
# print(sorted(basket))
# print (basket)
# basket.reverse()
# print(basket)

# basket = ['a','b', 'f', 'c','d', 'a','f']
# basket.sort()
# basket.reverse()
# print(len(basket))
# print(basket[::-1])
# print(list(range(1,100)))

# sentence = ' '
# print(sentence.join(['Hi', 'my', 'name', 'Viktor']))

# List unpacking
# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# None
# weapons = None
# print(weapons)

# Dictionary
# dictionary = {
#   'weapons' : [1,2,3],
#   'lvl' : 2,
#   'is_Magic' : True,
#   'hp_rer' : 0.5,
#   'nick_name' : 'Viktor'
# }
# my_list = [
# {
#   'a' : [1,2,3],
#   'b' : 2,
#   'f' : True,
#   'x' : 0.5,
#   'z' : 'Viktor'
# },
# {
#   'a' : [4,5,6],
#   'b' : 2,
#   'f' : True,
#   'x' : 0.5,
#   'z' : 'Viktor'
# }
# ]
# print(my_list[0]['a'][2])
# print(dictionary['a'][1])
# user = {
#   'lvl' : [1,2,3],
#   '123' : 2,
#    True : 'Viktor',
#   'age' : 10
# }
# user_2 = dict(name='valeu')
# print(user_2)

# print(user.get('age', 66))

# user = {
#   'lvl' : [1,2,3],
#   '123' : 2,
#    True : 'Viktor',
#   'age' : 10
# }
# print('lvl' in user)
# print('stop' in user)
# print('lvl' in user.keys())
# print([1,2,3] in user.values())
# print(user.items())
# # print(user.clear())
# user_2 = user.copy()
# print(user_2)
# # print(user.pop('age'))
# print(user.popitem())
# print(user.update({'ages' : 40}))
# print(user)

# Tuple
# user = {
#   'lvl' : [1,2,3],
#   '123' : 2,
#    True : 'Viktor',
#   'age' : 10
# }
# my_tuple = (1,2,3,4,5,3,3,3,6,7)
# new_tuple = my_tuple[1:2]
# print(new_tuple)
# print(my_tuple.count(3))
# print(my_tuple.index(3))
# print(len(my_tuple))

# Set
# my_set = {1,2,3,4,5,6,7,7,7,7,7}
# my_set.add(8)
# my_set.add(4)
# print(my_set)
# my_list = [1,2,3,4,5,6,6,7]
# print(set(my_list))
# my_set = {1,2,3,4,5,6,7}
# your_set = {6,7,8,9,10,11}

# print(my_set.difference(your_set))
# print(my_set.discard(1))
# print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set & your_set)
# print(my_set)
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))
# print(my_set.issubset(your_set))
# print(my_set.issuperset(your_set))
# print(my_set.union(your_set))
# print(my_set | your_set)


#  Conditional logik
# is_old = False
# is_licenced = True
# if is_old:
#   print('You are old enough to drive car!')
# elif is_licenced:
#   print('You have license.')
# else:
#   print('Sory, you are to yong to drive a car.')
# print('Test is executed')

# if is_old and is_licenced:
#   print('You are old enough to drive car and have got licence!')
# else:
#   print('Sory, you are to yong to drive a car.')
# print('Test is executed')


#                       Identation in Python
# is_old = False
# is_licenced = True
# if is_old:
#   print('You are old enough to drive car!')
# elif is_licenced:
#   print('You have license.')
# else:
#   print('Sory, you are to yong to drive a car.')
# print('Test is executed')


# Trurhy vs Falsey
# password = '123'
# user_name = 'Viktor'
# print(bool(''))
# print(bool(0))
# if password and user_name:
#   print('You are old enough to drive car!')
# else:
#   print('Sory, you are to yong to drive a car.')
# print('Test is executed')

# Ternary Operator

# condition_if_true if condition else conditiond_if_false
# is_friend = True
# can_message = 'message aloved' if is_friend else 'not aloved message'
# print(can_message)


# Short Circuting

# is_friend = False
# is_user = True
# print(is_friend and is_user)
# if is_friend or is_user:
#   print('best friends forever')
# else:
#   print('no they not friend')
# if is_friend and is_user:
#   print('best friends forever')
# else:
#   print('no they not friend')

#  Logical Operators
# >
# <
# ==
# print(4 > 5)
# print(4 < 5)
# print(4 == 5)
# print('hello' == 'hello')
# print('a' > 'b')
# print('a' > 'A')
# print(1 < 2 < 3 > 4)
# print(1 >= 0)
# print(0 != 0)
# print(0 == 0)

#  Logical Operators 1
# is_magician = False
# is_expert = True
# if is_magician and is_expert:
#   print('You are master magician')
# elif is_magician:
#   print('At least aou\'re geting there')
# elif is_expert:
#   print('You need magic powers')
# elif (not(is_expert) and (not(is_magician))):
#   print('Not player')
# print('Game over')

#  Logical Operators 2
# == check equality
# is check matching in memory
# print(True == 1) # true
# print('' == 1) #false
# print([] == 1) #false
# print(10 == 10.0) #true
# print([] == []) #true

# print(True is True) # true
# print('' is '') #true
# print([] is []) #false
# print(10 is 10) #true
# print([1,2,3] is [1,2,3]) #fals

#  Logical Operators loops (петли)
# for item in [1,2,3,4,5,6,7,8,9]:
#   for item2 in ('a', 'b', 'c'):
#     print(item, item2)
# print(item)
# print('for was finished')

#  Logical Operators iterable (итерабельность)
# iterable - list, dictionary, tuple, set, string
# iterated -> one by one check each item in the collection

# user = {
#   'name': 'Viktor',
#   'age': 8008,
#   'can_swim': False
# }
# for key, value in user.items():
#   print(key, value)
# for item in user.values():
#   print(item)
# for item in user.keys():
#   print(item)

#  Counter
# my_list = [1,2,3,4,5,6,7,8,9,10]
# print(sum(my_list))
# counter = 0
# number_of_value = 0
# for item in my_list:
#   counter = counter + item
#   number_of_value = number_of_value = item
#   print(number_of_value, counter)
# print('Number of elements ', number_of_value, 'Sum of elements ', counter)

# Range ()
# print(range(100))
# for number in range (0, 10):
#   print('Action', number)
# for _ in range(0, 10, 2):
#   print(_)
# for _ in range(10, 0, -2):
#   print(_)
# for _ in range(3):
#   print(list(range(10)))

# Enumerate()
# for i, char in enumerate('Hello'):
#   print(i, char)
# for i, char in enumerate({0,1,2,3,4}):
#   print(i, char)
# for i, char in enumerate([0,1,2,3,4]):
#   print(i, char)
# for i, char in enumerate((0,1,2,3,4)):
#   print(i, char)
# for i, char in enumerate(list(range(100))):
#   if char == 50:
#     print(f'index of 50 is: {i}')

# While lops
# i = 0
# while 0 < 50:
#   print(i)
#   break
# i = 0
# while i < 10:
#   print(i)
#   i += 1
# else:
#   print('Done with all the work')

# my_list = [1,2,3]
# for item in my_list:
#   print(item)

# i=0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1

# while True:
#   response = input('Say somthing: ')
#   if (response == 'bye'):
#     break
# print('Wish you a good day')

# break continue pass
# my_list = [1,2,3]
# for item in my_list:
#   print(item)
#   continue

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1
#   continue

# my_list = [1,2,3]
# for item in my_list:
#   #thinking about it (poss skip code in loop code)
#   pass

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1
#   pass

# Fist GUI
# picture = [
#     {0, 0, 0, 1, 0, 0, 0},
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
# for row in picture:
#     for value in row:
#         if value == 0:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')

# Redability, Clean
# predictability

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# fill = '@'
# empty = ' '
# for row in picture:
#   for value in row:
#     if value:
#       print(fill, end = '')
#     else:
#       print (empty, end = '')
#   print('')


# Check for duplicates in list:
# some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'n', 'm']
# duplicates = []
# for value in some_list:
#   if some_list.count(value) > 1:
#     if value not in duplicates:
#       duplicates.append(value)
# print(duplicates)

# Functions
# DRY Don't repeat yourself
# def say_hello():
#   print('Hello')
# say_hello()

# Parameters vs Arguments

# positional parameters
# Default parameters
# def say_hello(name = 'Darth Vaider', emojy='angry'):
# print(f'Hello {name} {emojy}')


# positional arguments
# say_hello('Viktor', 'smile')

# keyword arguments

# say_hello(emojy = '=)', name = 'Andrei')

# Default parameters
# say_hello()

# Return
# def sum(num1, num2):
#     def another_func(num1,num2):
#         return num1 + num2
#     return another_func(num1,num2)
# # Should do ine thing really well.
# # Should return something.
# total = sum(10,20)
# print(total)

# Exercise
# def check_of_age():
#     age = int(input('What is your age? : '))
#     if age >= 18:
#         return print('Power On. Enjoy the ride')
#     return print('Sorry, you are too young to drive this car. Powering off')
# check_of_age()

# Methods vs Functions
# list()
# print()
# max()
# min()
# input()

# def some_random_stuff():
#     pass
# some_random_stuff()
# def test(a):
#     '''
#     Info: This function tests and prints param a
#     '''
#     print(a)
#     return
# test(10)
# help(test)
# print(test.__doc__)

# Clean code
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
# print(is_even(25))

# *args **kwargs
# #  Rule: params, *args, default parameters, **kwargs
# def super_func(name, *args, i='Hi', **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
# print(super_func('Viktor', 1,2,3,4,5,6,7, num1 = 10, num2 = 20))

# Exercise
# def highest_even(li):
#     li.sort(reverse=True)
#     for item in li:
#         if item % 2 == 0:
#             return item
# print(highest_even([20, 18, 10, 2, 3, 44, 4, 8, 11 ]))
# Other devision
# def hihhest_event(li):
#     event = []
#     for item in li:
#         if item % 2 == 0:
#             event.append(item)
#     return max(event)
# print(hihhest_event([11, 44, 58, 24, 46, 11, 99]))

# Warlus operator
# a = 'Hellooooooooooo'
# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")
# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
# print(a)

# Scope
# Scope - what variables do i have access to?
# if True:
#     x = 10
# def some_value():
#     x = 20
#
# print(x)

# a = 1
# def parent():
#     def confusions():
#         return sum
#     return confusions()
#
# print(parent())
# print(a)
# 1 - start with local
# 2 - Parent local
# 3 - Global
# 4 - Build in python finctions


# total = 0

# def count():
#     global total
#     total += 1
#     return total
# count()
# print(count())
# def count(total):
#     total += 1
#     return total
# print(count(count(count(total))))

# non local Keyword
# def outer():
#     x = 'local'
#     def inner():
#         nonlocal x
#         x = 'nonlocal'
#         print('inner:' , x)
#     inner()
#     print('outher:', x)
#
# outer()

# 1 - start with local
# 2 - Parent local
# 3 - Global

# txt = ' Hello Word '
# x = txt.strip()
# txt = txt.upper()
# txt = txt.lower()
# txt = txt.replace('H', 'J')
# age = 36
# txt = f'My name is John, and I am {age}'
# fruits = ('apple', 'banana', 'cherry')
# fruits.append('orange')
# fruits.insert(1, 'lemon')
# fruits.remove('banana')
# fruits = {'apple', 'banana', 'cherry'}
# more_fruits = ['orange', 'mango', 'grapes']
# fruits.update(more_fruits)
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car['color'] ='red'
# car.pop('model')
# car.clear()
# print(car)

# a = 50
# b = 10
# if a == b :
#     print('1')
# elif a > b :
#     print('2')
# else:
#     print('3')
# if 5 > 2:
#     print("Five is greater than two!")
# import this
# class BigObject:  # Class
#     # code
#     pass
# obj1 = BigObject() # instanciate
# obj2 = BigObject() # instanciate
# obj3 = BigObject() # instanciate
#
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('Text'))
# print(type([]))
# print(type({}))
# print(type(()))
# print(type(obj1))

# class PlayerCharacter:
#     #  Clas Object Attribute
#     membership: bool = True
#
#     def __init__(self, name='anonymous', age=0):
#       if (age > 18):
#         self.name = name  # attributes
#         self.age = age
#
#     def shout(self):
#         print(f'my name is {self.name}')

# def shout(self):
#     print(f'my name is {PlayerCharacter.name}')


# player1 = PlayerCharacter('Tom', 19)
# player2 = PlayerCharacter()
# print(player1.shout())
# player2.attack = 50
# print(player1)
# print(player2)
# print(player2.attack)
# print(player1.run())
# print(player1.name)
# print(player2.age)
# print(player1.run('hello'))

# Given the below class:
# class Cat:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# cat1 = Cat('CatMin', 10)
# cat2 = Cat('CatMiddle', 15)
# cat3 = Cat('CatOld', 25)
#
#
# def get_oldest_cat(cats):
#     oldest_cat = Cat('', 0)
#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return oldest_cat
#
#
# oldestcat = get_oldest_cat([cat3, cat2, cat1])
# print(f'The oldest cat is {oldestcat.name}, he is {oldestcat.age} years old.')

# class PlayerCharacter:
#     memberhip = True
#
#     def __init__(self, name, age):
#         self.name = name  # atributes
#         self.age = age
#
#     def shout(self):
#         print(f'My name is {self.name}')
#
#     @classmethod
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)
#     @staticmethod
#     def adding_things(num1, num2):
#         return num1 + num2

# player1 = PlayerCharacter('Tom', 10)
# player3 = PlayerCharacter.adding_things(2, 3)
# print(player3.age)

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def run(self):
#         return self
# player1 = PlayerCharacter('Tonny', 10)
# player1.run()
# print(player1.run())


# class PlayerCharacters:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f'My name is {self.name}, and my age is {self.age} years old.')
# player1 = PlayerCharacters ('Viktor', 34)
# print(player1.speak())

# Private & Public Variables
# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def run(self):
#         print('run')
#     def speak(self):
#         print(f'My name is {self.name} and my age is {self.age}')
# player1 = PlayerCharacter('Viktor', 34)
# player1.name = '!!!!'
# player1.speak = 'BOOOO'
# print(player1.speak)

# Users
#     - Wizards
#     - Archers
#     - Wariors
# class User():
#     def sign_in(self):
#         print('Login')
#     def attack(self):
#         print('do nothin')
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.pover = power
#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of {self.pover}')
#
# class Archer(User):
#     def __init__(self, name, num_of_arrows):
#         self.name = name
#         self.num_of_arrows = num_of_arrows
#     def attack(self):
#         print(f'attacking with arrows and arrows left - {self.num_of_arrows}')
#
# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Legalas', 75)
# print(isinstance(wizard1, Wizard))
# def player_attack(char):
#     char.attack()
# player_attack(wizard1)
# player_attack(archer1)
# for char in [wizard1, archer1]:
#     char.attack()
# print(wizard1.attack())
#


# class Pets():
#     animals = []
#
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Fluffy(Cat):
#     def sing(self, sound):
#         return f'{sound}'
#
# fluffy = Fluffy('Fliffy', 5)
# sally = Sally('Sally', 3)
# simon = Simon('Simon', 12)
#
# my_cats = [fluffy, simon, sally]
#
# my_cats = Pets(my_cats)
#
# my_cats.walk()

# class User(object):
#     def __init__(self, email):
#         self.email = email
#
#     def sing_in(self):
#         print('Logged in')
#
# class Wizzard(User):
#     def __init__(self, name, pover, email):
#         # User.__init__(self, email)
#         super().__init__(email)
#         self.name = name
#         self.pover = pover
#
#     def attack(self):
#         print(f'attaking with power of {self.pover}')
#
# wizzard1 = Wizzard('Merlin', 3000, 'merlin@gmail.com')
# print(wizzard1.email)
#
# # Introspection
# wizzard1 = Wizzard('Merlin', 3000, 'merlin@gmail.com')
# print(dir(wizzard1))

# class Toy():
#     def __init__(self, colour, age):
#         self.colour = colour
#         self.age = age
#         self.my_dict = {
#             'name' : 'Yoyo',
#             'has_pets' : False
#         }
#     def __str__(self):
#         return f'{self.colour}'
#     def __len__(self):
#         return 5
#     def __call__(self):
#         return ('Yess???')
#     def __getitem__ (self, i):
#         return  self.my_dict[i]
#
# action_figure = Toy('blue', 10)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())
# print(action_figure['name'])

# class SuperList(list):
#     def __len__(self):
#         return 1000
#
# super_list1 = SuperList();
# print(len(super_list1))
# print(super_list1.append(5))
# print(super_list1[0])
# print(issubclass(SuperList, list))

# class User():
#     def __init__(self):
#         print('logged in')
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f'attaking with power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrow = arrows
#
#     def check_arrow(self):
#         print(f'attaking by arrows and damage is {self.arrow}')
#
#     def run(self):
#         print('ran very fast')
#
#
# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, power)
#
#
# hb1 = HybridBorg('Tiest nybryd', 50, 200)
# print(hb1.attack())

# MRO  -  Method Resolution Order

# class A:
#     num = 10
#
# class B(A):
#     pass
#
# class C(A):
#     num = 1
#
# class D (B,C):
#     pass

# class X:pass
# class Y:pass
# class Z:pass
# class A(X, Y):pass
# class B(Y, Z):pass
# class M(B, A, Z):pass
#
# print(M.__mro__)


# def multiply_list(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list
#
# print(multiply_list([2, 3, 4]))

#  map, filter zip, reduce
#  map
# my_list = [1, 2, 3]
#
#
# def multyply_list(item):
#     return item * 2
#
#
# print(list(map(multyply_list, [1, 2, 3])))
# print(my_list)

# filter

# my_list = [1, 2, 3]
#
#
# def multyply_list(item):
#     return item * 2
#
#
# def only_odd(item):
#     return item % 2 != 0
#
#
# print(list(filter(only_odd, [1, 2, 3])))
# print(my_list)

#  zip

# my_list = [1, 2, 3, 4]
# you_list = [20, 30, 50]
# their_tuple = ('t', 'a', 'c')
# test = {100, 200, 400}
#
# def multyply_list(item):
#     return item * 2
#
#
# def only_odd(item):
#     return item % 2 != 0
#
#
# print(list(zip(my_list, you_list, test, their_tuple)))
# print(my_list)

# # reduce
# from functools import reduce
# my_list = [1, 2, 3, 4]
#
# def multyply_list(item):
#     return item * 2
#
#
# def only_odd(item):
#     return item % 2 != 0
#
# def accumulator(acc, item):
#     print (acc, item)
#     return acc + item
#
#
# print(reduce(accumulator, my_list, 0))
# print(my_list)

# Exercise

# from functools import reduce
#
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
#
#
# def cappitalize_all(item):
#     return item.capitalize()
#
#
# print(list(map(cappitalize_all, my_pets)))
#
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
# my_numbers.sort()
#
# print(list(zip(my_numbers, my_strings)))
#
# scores = [73, 20, 65, 19, 76, 100, 88]
#
#
# def my_score_over_50(score):
#     return score >= 50
#
#
# print(list(filter(my_score_over_50, scores)))
#
#
# def accumulator(acc, item):
#     return acc + item
#
#
# print(reduce(accumulator, (my_numbers + scores)))

# Lambda Expressions

# from functools import reduce
#
# lambda param: action(param)
# my_list = [1, 2, 3]
#
#
#
# print(list(map(lambda item: item * 2, my_list)))
#
# print(list(filter(lambda item: item % 2 != 0, my_list)))
#
# print(reduce(lambda item, acc: item + acc, my_list))
# print(my_list)

# my_list = [5, 4, 3]
#
# new_list = list(map(lambda num: num ** 2, my_list))
# print(new_list)
# a = [(0,2), (4,3), (9,9), (10,-1)]
#
# print(a.sort(key=lambda x: x[1]))
# print(a)
# List
# my_list = [param for param in iterable]
# my_list = [char for char in 'Hello']
# my_list2 = [num for num in range(0, 100)]
# my_list3 = [num * 2 for num in range(0, 100)]
# my_list4 = [num ** 2 for num in range(0, 100)]
# my_list5 = [num * 2 for num in range(0, 100) if num % 2 == 0]
# print(my_list5)

# SET
# my_set = {param for param in iterable}
# my_set1 = {char for char in 'Hello'}
# my_set2 = {num for num in range(0, 100)}
# my_set3 = {num * 2 for num in range(0, 100)}
# my_set4 = {num ** 2 for num in range(0, 100)}
# my_set5 = {num * 2 for num in range(0, 100) if num % 2 == 0}
# print(my_set4)

# Dictionary
# simple_dict = {
#     'a' : 1,
#     'b' : 2
# }
# my_dict = {k:v ** 2 for k, v in simple_dict.items() if v %2 ==0 }
# my_dict = {num: num*2 for num in [1, 2, 3]}
# print(my_dict)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = set([char for char in some_list if some_list.count(char) >1])
# print(duplicates)

# Hight Order Functions HOS
# def hello():
#     print('Hello')
#
# def my_decorator(func):
#     def wrat_func():
#         print('*******')
#         func()
#         print('*******.')
#     return wrat_func
# # @my_decorator
# def hello():
#     print('Hello')
# # @my_decorator
# def bye ():
#     print('see you later')
# hello2 = my_decorator(hello)
# hello2()

# def my_decorator(func):
#     def wrat_func(*args, **kwargs):
#         print ('*********')
#         func(*args, **kwargs)
#         print('******.')
#     return wrat_func
#
# @my_decorator
# def hello(greating, emoji = '=('):
#     print(greating, emoji)
# hello('Viktor')
# from time import time
# def performance(fn):
#     def wrfunctions(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrfunctions
# @performance
# def long_time():
#     for i in range(100000000):
#         i*5
# long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

# Error Handling
# while True:
#    try:
#        age = int(input('What is your age?'))
#        10/age
#    except ValueError:
#        print('Please enter a numbe')
#    except ZeroDivisionError:
#        print('Please enter age higher than 0')
#    else:
#        print(f'Yot age is {age}')
#        break

# def sum(num1, num2):
#    try:
#        return num1 / num2
#    except (TypeError, ZeroDivisionError) as err:
#        print(err)
#
#
# print(sum(1, '2'))

# while True:
#    try:
#        age = int(input('What is your age?'))
#        10/age
#    except ValueError:
#        print('Please enter a numbe')
#        continue
#    except ZeroDivisionError:
#        print('Please enter age higher than 0')
#        break
#    else:
#        print(f'Your age is {age}')
#        break
#    finally:
#        print('ok it is finished')
#     print('We dont go to this part')

# Generator

# def denerator_function(num):
#     for i in range(num):
#         yield i
#
# for item in denerator_function(10):

# range(100)
# list(range(100))
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
# my_list = make_list(100)
# print(my_list)

# def generator_function (num):
#     for i in range (num):
#         yield i*2
# g = generator_function(100)
# print(g)

# for item in generator_function(1000):
#     print(item)

# class MyGen():
#     current = 0
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration
#
#
# gen = MyGen(0, 100)
# for i in gen:
#     print(i)

# Fibonacci numbers

# def fib(num):
#     n1 = 0
#     n2 = 1
#     for i in range(num):
#         yield n1
#         temp = n1
#         n1 = n2
#         n2 = temp + n2
#
# for x in fib(20):
#     print(x)
#
# def fib2(num):
#     n1 = 0
#     n2 = 1
#     result = []
#     for i in range(num):
#         result.append(n1)
#         temp = n1
#         n1 = n2
#         n2 = temp + n2
#     return result
#
# print(fib2(20))
import utility
import shoping.shoping_card
print(shoping.shoping_card.buy('lime'))
