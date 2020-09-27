import pdb

def sum(n1, n2):
    pdb.set_trace()
    return n1+n2

print(sum(10, 'asdf'))


# pdb can type help to get more info
# s or step will go to the next line
# list will list code that pdb is currently in
# a gives all arguments in function you're in
# w clarifies with additional information on each line
# continue which goes through the code and returns an error