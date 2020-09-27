# error handling

# syntax error
# def hoooohoooo():
#    1+name
# while True:
#     try:
#         age = int(input('what is your age? \n'))
#         print("this is your age: ", age)
#         10/age
#     except ValueError:
#         print('please enter a number! \n')
#     except ZeroDivisionError:
#         print('please enter age higher than 0 \n')
#     else:

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         return ("oops, can't divide by zero", err)
# print(sum(21,0))

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except TypeError as err:
#         return ("please input a number", err)
#     except ZeroDivisionError as err:
#         return ("can't divide by zero", err)
# print(sum(21,0))


while True:
    try:
        age = int(input('what is your age? \n'))
        10/age
        # raise ValueError('hey cut it out')
        # can also do: raise Exception('hey cut it out')
        # if we uncomment line 38, and remove the value error
        # on line 41-44, we can force an error to occur
    except ValueError:
        print('please enter a number! \n')
        # continue will basically restart this process
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0 \n')
        break
        # break will bust out of the loop and print "yolo"
    else:
        print('Thank you \n')
    finally:
        print('done computing')
    # to print yolo, you have to finish the program, which you can do by typing a number
    print("yolo")
