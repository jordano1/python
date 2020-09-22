# inheriting a parent class method (user to wizard)
class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return ('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # can use super, super is I guess better, doesn't need self
        super().__init__(email)
        # can also use
        # User.__init__(self,email) requires self!
        self.name = name
        self.power = power
        # can also remove super, and do self.email = email

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

wizard1 = Wizard('jordan', 50, 'merlin@gmail.com')
archer1 = Archer('bab', 30)
print(wizard1.email)
print(wizard1.sign_in())
print(dir(wizard1))