mi_list = [1,1,1,1,1,1,1,1,1]
print(len(mi_list))
print(mi_list)

class Object:
    pass

my_object = Object()
print(my_object)

class CompactDisc:
    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):
        return f'Album: {self.title} from {self.author}'

    def __len__(self):
        return self.songs

    def __del__(self):
        print('CD removed')

my_cd = CompactDisc('Pink Floyd', 'The Wall', 24)
print(my_cd)
print('Songs:', len(my_cd))
del my_cd # delete

