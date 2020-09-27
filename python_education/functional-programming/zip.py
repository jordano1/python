# map, filter, zip, reduce
# if your or my list are tuples it'll still work


my_list = [1, 2, 3, 4, 5]
your_list = [6, 12, 18, 24, 36]
def timestwo(item):
  return item*2

def is_odd(item):
  return item % 2 != 0

def is_even(item):
  return item % 2 == 0
print(list(filter(is_odd, my_list)))
print(list(zip(my_list, your_list)))