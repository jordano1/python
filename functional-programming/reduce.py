# map, filter, zip, reduce
# if your or my list are tuples it'll still work
from functools import reduce
my_list = [1,2,3]
def timestwo(item):
  return item*2

def is_odd(item):
  return item % 2 != 0

def is_even(item):
  return item % 2 == 0

def accumulator(i, item):
  print(i, item)
  return i+item

print(reduce(accumulator, my_list))
print(my_list)
