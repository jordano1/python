from collections import Counter, defaultdict, OrderedDict

# li = [1,2,3,4,5,6,7]
# sentence = 'blah blah python here'
# print(Counter(li))
# print(Counter(sentence))

# dictionary = {'a': 1, 'b': 2}
# dictionary = defaultdict(lambda: 'does not exist',{'a':1,'b':2})
# print(dictionary['a'])
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)
