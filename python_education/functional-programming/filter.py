# map, filter, zip, reduce


test = [1, 2, 3, 4, 5, ]
def timestwo(item):
  return item*2

def is_odd(item):
  return item % 2 != 0

def is_even(item):
  return item % 2 == 0
print(list(filter(is_odd, test)))
print(list(filter(is_even, test)))
