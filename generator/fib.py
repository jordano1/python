def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
    return num

for i in fib(15):
    print(i)
    
    
#list
# def fib_list(num):
#     b = 1
#     a = 0
#     result = []
#     for i in range(num):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result

# print(fib_list(20))
