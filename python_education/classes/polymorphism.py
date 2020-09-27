# you can inheret the properties of a class by just passing the class into another class (aka class Wizard(User)) is taking the user class and it's properties
# in order for classes to work properly you need to use the self. property which essentially is universal in computer science, identifying the current object / class you're in, so you must pass class as a variable in your methods that you are using
# line 32 is archer inheriting from user the sign_in method


class User(object):
    def sign_in(self):
        return print('logged in')
    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        #can also do
        # User.attack(self)
        # which will actually do the method within User
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with your bow, you have {self.num_arrows} left')

wizard1 = Wizard('jordan', 50)
archer1 = Archer('bab', 30)


# for looping over classes
for char in [wizard1, archer1]:
    char.attack()

# basically calls the specific method defined in the class, even though they are named the same thing (attack)
# specific function call through class, able to get the unique method in wizard1 and archer1
# def player_attack(char):
#     char.attack()
# player_attack(wizard1)
# player_attack(archer1)


# (archer1.attack())
# archer1.sign_in()
# dunder methods
# if you type wizard1. you will get a list of a ton of methods part of classes
# you can use object because the classes are essentially made using an object structure, classes inherit from the object base class.
print(isinstance(wizard1, object))

# []. also brings up a ton of methods, this list also inherits from the object class cuz you can see it brings up methods that are also in the object base class