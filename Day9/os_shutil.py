import os
import shutil
import send2trash

# CURRENT PATH
# print(os.getcwd())

# CREATE FILE IF NOT EXISTS
# file = open('course.txt', 'w')
# file.write('This is a test text')
# file.close()

# LIST FILES FROM A DIRECTORY
# print(os.listdir())

# MOVE FILES
# shutil.move('course.txt', 'course2.txt')

# REMOVE FILE
#os.unlink()

# REMOVE EMPTY DIRECTORY
#os.rmdir()

# REMOVE DIRECTORY WITH FILES RECURSIVELY
# shutil.rmtree('')

# SAFE DELETE
# send2trash.send2trash('course2.txt')

# GENERATOR
path = '/home/mrrobot/Documents/PycharmProjects/PythonProject'
print(os.walk(path))
for directory, subdir, files in os.walk(path):
    print(f'In directory: {directory}')
    print(f'Subdirectories are:')
    for sub in subdir:
        print(f'\t{sub}')
    print('Files are:')
    for file in files:
        if file.startswith('.'):
            print(f'\t{file}')
    print('\n')




