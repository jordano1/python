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
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with your bow, you have {self.num_arrows} left')

wizard1 = Wizard('jordan', 50)
archer1 = Archer('bab', 100)

(archer1.attack())
archer1.sign_in()