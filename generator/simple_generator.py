def gen(num):
    for i in range(num):
        yield i

for item in gen(100):
    print(item)