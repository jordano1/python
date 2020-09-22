# map, filter, zip, reduce
# if your or my list are tuples it'll still work
from functools import reduce

# lambda param: action(param)

my_list = [1, 2, 3]

def timestwo(item):
  return item*2

def is_odd(item):
  return item % 2 != 0

def is_even(item):
  return item % 2 == 0

def accumulator(acc, item):
  print(acc, item)
  return acc + item

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda num: num % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

