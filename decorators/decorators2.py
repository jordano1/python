# my_list = []
# for char in 'hello':
#     my_list.append(char)
# print(my_list)
def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('******')
    return wrap_func

@my_decorator
def hello():
    print('hello')

hello()