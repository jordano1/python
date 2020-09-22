# has a mode which stands for 'r' which is read, if we want to read and write do r+, append mode (append end of file is a)
# w writes over all content in the text file
try:
    
    with open('sad.txt', mode='r') as my_file:
        text = my_file.write(':(')
        print(text)
        # print(my_file.readlines())
# file is not found
except FileNotFoundError as err:
    print('file does not exist')
    raise err
# when computer has some issue reading or writing
except IOError as err:
    print('io error')
    raise err
# my_file= open('test.txt')
# print(my_file.readlines())
# my_file.close()
# my_file.seek(0)
# seeking line 0
