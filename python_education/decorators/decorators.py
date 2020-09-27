# decorator adds functionality to functions
# @decorator
# def hello():
#     pass

# hight order function accepts funcs as a parameter
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func()
    
print(greet2())