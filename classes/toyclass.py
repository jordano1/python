class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,

        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('you called?')

    def fefe(self, i):
        return self.my_dict[i]
        
    def __getitem__(self, i):
        return self.my_dict[i]
action_figure = Toy('red', 0)


print(str(action_figure)) #puts obj into a string object
print(len(action_figure)) #length
print(action_figure())

# getitem allows you to iterate I think?
# can also create a method that just does this
def fefe(self, i):
    return self.my_dict[i]

print(action_figure.fefe('name'))
    
def __getitem__(self, i):
    return self.my_dict[i]
        
print(action_figure['name'])
