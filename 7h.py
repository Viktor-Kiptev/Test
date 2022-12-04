# num1 = num2 = 3
# print(num1, num2)
#
# num1, num2 = 2, 5
# print(num1, num2)
#
# swap1 = 88
# swap2 = 99
# print(f'swap1 = {swap1} swap2 = {swap2}')
# swap1, swap2 = swap2, swap1
# print(f'swap1 = {swap1} swap2 = {swap2}')
# swap2 -=swap1
# print(swap2)

# x, y, z, = [1, 'test', 3]
# print(f'x:{x}, y:{y}, z:{z}')

# x, y, *z, = [1, 2, 3, 4, 5, 5, 6, 6]
# print(f'x:{x}, y:{y}, z:{z}')
#
# x, *y, z, = [1, 2, 3, 4, 5, 5, 6, 6]
# print(f'x:{x}, y:{y}, z:{z}')

# Date type

# a = None
# print(type(a))
# a = 1
# print(type(a))
# a = 1.0
# print(type(a))
# a = 1 + 1j
# print(type(a))
# a = '1'
# print(type(a))
# a = [1, 'string', True]
# print(type(a))
# a = (1, 'string', True)
# print(type(a))
# a = {1:1, 2:'string', 3:True}
# print(type(a))
# a = {1, 'string', True}
# print(type(a))
# a = True
# print(type(a))

# while True:
#     x = int(input())
#     count = 0
#     factorial = 1
#     while count < x:
#         count +=1
#         factorial *=count
#
#     else:
#         print(f'Factorial {x} is {factorial}')

# x = ''
#
# while len(x) < 6:
#     user_input = input()
#     if len(user_input) > 1:
#         continue # skip 1 iteration when condition true
#     if user_input == 'q' or 'Q':
#         break # interrupt loop
#     x += user_input
#
# else:
#     print(x)

# import os
#
# sayt = input('Enter site to open \n')
#
# if 'https://' in sayt:
#     os.system('start ' + sayt)
# elif 'www.' in sayt:
#     sayt = 'https://' + sayt
#     os.system('start ' + sayt)
# else:
#     sayt = 'https://www.' + sayt
#     os.system('start ' + sayt)

# alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
# user_input = input('Enter text\n')
# for i in alphabet:
#     counter = 0
#     for leter in user_input:
#         if i == leter:
#            counter += 1
#     if counter > 0:
#         print(f'there are {counter} leter {i}')

# list

# m = [1, 2, 3, ['w', 'z', 'd'], {2, 4, 6}]
# print(m[2], m[3][1], m[4])
#
# m[1], m[2] = m[2], m[1]
# m.append(2)
# new_m = m.copy()
# car_dict = {'ford':'Edge'}
# m.append({'Ford':'Edge'})
# m.extend(car_dict)
# x = m.index('ford')
# m.pop(x)
# m.insert(2, 'Candy')
# new_m.remove(3)
# m.reverse()
# new_m.clear()
# new_m = list(range(0, 8, 2))
# new_m2 = list('Some string some')
# new_m2.sort(reverse=False)
# new_m *= 2
# print(m)
# print(new_m)
# print(new_m2)

# tuple

# x = (2, 1, 3, 3, 4, 6, 5)
# z, s, *r = x
# print(r)
# print(x[1:5])
# for i in range(len(x)):
#     x[i] +=3
# print(x)