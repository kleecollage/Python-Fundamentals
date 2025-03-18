from Day3.dictionary import client

series = "N-02"
if series == "N-01":
    print("Samsung")
elif series == "N-02":
    print("Nokia")
elif series == "N-03":
    print("Motorola")
else:
    print("Not available")

# Match
match series:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Not available")

client = {'name': 'John',
          'age': 22,
          'occupation': 'instructor'}

movie = {'title': 'Matrix',
         'technical_sheet': {'protagonist': 'Keanu Reeves',
                             'director': 'Lana and Lilly Wachowski'}}

items = [client, movie, 'book']

for i in items:
    match i:
        case {'name': name,
            'age': age,
            'occupation': occupation}:
            print("Is a client")
            print(name, age, occupation)
        case {'title': title,
              'technical_sheet': {'protagonist': protagonist,
                                  'director': director}}:
            print("Is a movie")
            print(title, protagonist, director)
        case _:
            print("Not Information")