simple_dictionary = {
    'a':1,
    'b':2,
}
my_dictionary = {key:value**2 for key, value in simple_dictionary.items()}

print(my_dictionary)