import re
text = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

word = 'ayuda' in text
print(word)

pattern = 'Not in Text'
query = re.search(pattern, text)
print(query)

pattern = 'ayuda'
query = re.search(pattern, text)
print(query)
print(query.span())
print(query.start())
print(query.end())

query = re.findall(pattern, text)
print(query)
print(len(query))

for found in re.finditer(pattern, text):
    print(found.span())
    print(found.group())

text = "Call to 562-489-6588. Call Now!"
pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
query = re.search(pattern, text)
print(query)
print(query.group())

pattern = r'\d{3}-\d{3}-\d{4}'
query = re.search(pattern, text)
print(query.group())

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
query = re.search(pattern, text)
print(query.group(3))

#password = input("Enter password: ")
password = '<PASSWORD>'
pattern = r'\D{1}\w{7}'
check = re.search(pattern, password)
print(check)

text = "No atendemos los lunes por la tarde"
query = re.search('lunes|martes', text)
print(query)

# . = before or after
query = re.search('....demos...', text)
print(query)

# ^ = Starts with
query = re.search(r'^\D', text)
print(query)

# $ = Ends with
query = re.search(r'\D$', text)
print(query)

# [^\s] = Excludes empty spaces
query = re.findall(r'[^\s]', text)
print(query)

# + = 1 or more times
query = re.findall(r'[^\s]+', text)
print(query)
print(''.join(query))

email = 'usuario@hostcom'
regex = r'\w{1,}@\w{1,}\Wcom\w?\w?'
query = re.search(regex, email)
if query is not None:
    print(query)
else:
    print('No match')


greeting = 'Hello World'
regex = r'^Hello'
query = re.search(regex, greeting)
if query is None:
    print("No has saludado")
else:
    print("Ok")

cp = 'Ab5478'
regex = r'\w{2}\d{4}'
query = re.search(regex, cp)
if query is None:
    print("El código postal ingresado no es correcto")
else:
    print("Ok")