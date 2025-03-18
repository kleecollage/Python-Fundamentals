import os
from path_lib import Path

path = os.getcwd()
print(path)

path = '/home/mrrobot/Documents/PycharmProjects/PythonProject/Day6/test.txt'
element = os.path.basename(path)
print("Basename", element)

element = os.path.dirname(path)
print("Dirname", element)

element = os.path.split(path)
print("Split", element)

# new_path = os.makedirs('/home/mrrobot/Documents/PycharmProjects/AlternativePath/Other')
# os.rmdir('/home/mrrobot/Documents/PycharmProjects/AlternativePath/Other')

path = '/home/mrrobot/Documents/PycharmProjects/AlternativePath/Alternative.txt'
file = open(path, 'r')
print(file.read())
file.close()

other_file = open('/home/mrrobot/Documents/PycharmProjects/AlternativePath/other_file.txt')
print(other_file.read())

directory = Path('/home/mrrobot/Documents/PycharmProjects/AlternativePath') / 'other_file.txt'
# file = directory / 'other_file.txt'
# my_file = open(file, 'r')

my_file = open(directory, 'r')
print(my_file.read())