import re

string = "search this inside of this text please!"
# methods in re.search
print('search' in string)
a = re.search('this', string)
print('tells you where the string is index: ', a.span())  # 17, 21
print('start tells you when the text starts:', a.start()) # 17
print('tells you where the text ends: ' , a.end()) # 21
print('gives you the string: ', a.group()) # this, good for multiple searches

# re.search

# just one search, a pattern we're trying to match
a = re.search('this', string)
# a = re.search('thas', string) if it doesn't exist it will return nontype
print(a.group())

# recompile
pattern = re.compile('search this inside of this text please!')
string = "search this inside of this text please!"
# b = pattern.search('thIs', string) don't need to pass a string, take thIs out because we are putting 'this' as the pattern var on line 18, and we're using pattern.search(string)
b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)

pattern = re.compile('search this inside of this text please!')
string = "search this inside of this text please!"
d = pattern.match(string)
print(d)
