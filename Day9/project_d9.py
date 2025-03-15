import math
import shutil, os, re, datetime
import time
from pathlib import Path

# shutil.unpack_archive('Proyecto+Dia+9.zip', 'ProjectD9', 'zip')
# print(os.listdir('ProjectD9'))

# instructions = open('ProjectD9/Instrucciones.txt', 'r')
# content = instructions.read()
# print(content)

path = '/home/mrrobot/Documents/PycharmProjects/PythonProject/Day9/ProjectD9/Mi_Gran_Directorio'
files_dic = {}

def get_content():
    for directory, subdir, files in os.walk(path):
        for file in files:
            file_path = Path(directory, file)
            found = open(file_path , 'r')
            content = found.read()
            has_series(file, content)
            found.close()

def has_series(file, content):
    regex = r'N\w{3}-\d{5}' # Nryu-12365
    search = re.search(regex, content)
    if search is not None:
        serial = search.group()
        files_dic[file] = serial

def print_results():
    date = datetime.date.today()
    print('-'*35)
    print(f'Search Date: {date.day}/{date.month}/{date.year}')
    print('\n FILE \t\t\t\t SERIAL NO.')
    print('-'*16 + '\t' + '-'*16)
    for file, serial in files_dic.items():
        print(file + '\t\t  ' + serial)
    print('\nFiles Found:', len(files_dic))
    print(f'Search Duration: {duration} seconds')
    print('-' * 35)

def format_date():
    current_date = str(datetime.date.today())
    current_date = current_date.split('-')
    current_date.reverse()
    current_date = '/'.join(current_date)
    return current_date

start = time.time()
get_content()
end = time.time()
duration = math.ceil(end - start)
print_results()