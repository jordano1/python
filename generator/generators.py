# iterable
# iterate
# generators




def generator_function(num):
    for i in range(num):
        yield i*2 # yield pauses
g = generator_function(100)

print(next(g))
print(next(g))
# for item in generator_function(1000):
#     print(item)


# def make_list(num):
#     new_list = []
#     for i in range(num):
#         new_list.append(i*2)
#     return new_list


# my_list = make_list(100)

# print(list(range(10000)))
