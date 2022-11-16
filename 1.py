# import sys
# import random
# name = sys.argv[1]
# user_value = sys.argv[2]
# print('Lats go playing')
# print(f'{name} you must gase number what will be shown you select {user_value}')
# print('Lets go start')
# sis_value = random.randint(1, 10)
# if user_value == sis_value:
#     print(f'You win sister show {sis_value}')
# else:
#     print(f'Sory you didn\'t ges sistem select {sis_value}')

import pyjokes
joke = pyjokes.get_joke('en', 'neutral')
print(joke)


