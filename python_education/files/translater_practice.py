from translate import Translator
translator = Translator(to_lang='ja', src='en')
try:
    with open('test.doc', mode='r+', encoding='utf-8') as my_file:
        print('my file: ', my_file)
        text = my_file.read()
        translated_text = translator.translate(text)
        my_file.write(translated_text)

    my_file.close()

    # with open('test.txt', mode='w') as my_file:
    #     translated_text = translator.translate(text)
    # my_file.close()


except IOError as err:
    print('there was an IO error: ')
    raise err
except EnvironmentError as err:
    print('env error!')
    raise err
except FloatingPointError as err:
    print('float err')
    raise err







































# try:
#     with open('test.txt', mode='w') as my_file:
#         print(my_file)

# except IOError as err:
#     print('there was a ioerror')
#     raise err
