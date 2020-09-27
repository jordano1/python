import re
# at least 8 char long
# contain any sort letters, numbers $%#@
# last should be a digit
password = input("please input your password\n")
if re.fullmatch(r'[A-Za-z0-9@#$%^&]{8,}\d', password):
    print("matched!")
else:
    print("no match!")
