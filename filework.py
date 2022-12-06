# r - read mode
# a - append mode
# w - write mode
# r+ - read & write mode
# w+ - write and read mode
# a+ + append and read mode

# read data from file
# obj = open('test_doc.txt', 'r')

# read all data from file
# print(obj.read())

# read 1 by 1 line from file
# print(obj.readline())
# print(obj.readline())

# read only few characters from file
# print(obj.read(10))

# read all char from the file and show 1 by 1
# for i in obj: # line by line
#     for char in i: #char by char in line
#         print(char)
#
# obj = open('test_doc.txt', 'w') # rewrite file with new data
# obj.write('Add new line\n')
# obj.close()
#
# obj = open('test_doc.txt', 'a') # append data to the file
# obj.write('Add new line #2')
# obj.close()

# obj = open('test_doc.txt', 'r')
# print(obj.tell()) # show curent position of cursor
# obj.readline()
# print(obj.tell())
# obj.seek(10)
# print(obj.tell())