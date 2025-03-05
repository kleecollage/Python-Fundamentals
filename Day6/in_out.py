my_file = open('test.txt')

# all_file = my_file.read()

one_line = my_file.readline()
print(one_line.upper())

one_line = my_file.readline()
print(one_line)

one_line = my_file.readline()
print(one_line.rstrip())

one_line = my_file.readline()
print(one_line)

# for line in my_file:
#     print("Here says:", line)

all_lines = my_file.readlines()
print(all_lines)
all_lines = all_lines.pop()
print(all_lines)

my_file.close()