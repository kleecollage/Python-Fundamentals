my_file = open('test1.txt', 'w')

my_file.write('Hello World\n')
my_file.write('I AM THE NEW TEXT!')
my_file.write('''This is
awesome content
generated in python
''')
my_file.writelines(['Hello', 'Python', 'From', 'Linux'])

list_words = ['Hello', 'Python', 'From', 'Linux']
for word in list_words:
    my_file.write(word + '\n')
my_file.close()


my_file = open('test.txt', 'a')
my_file.write("Goodbye")
my_file.close()





