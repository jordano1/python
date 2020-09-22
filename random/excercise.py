import sys
import random
def run_guess_game(guess):

    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])

    print(f'hello, welcome to this stupid game random number game, we will be using a number between {number1} and {number2}')
    random_num = random.randint(number1, number2)

    while True:
        try:
            user_num = int(input("please put in a number\n"))
            if user_num == random_num:
                print(f"your number matches!, I chose {random_num} and you chose {user_num}")
                break
            if user_num > random_num:
                print(f"your number is greater")
                continue
            if user_num < random_num:
                print(f"your number is less")
                continue
            else:
                "bozo"
        except ValueError:
            print("you put in a string(letters), instead of numbers")    


# answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))
# while True:
#     try:
#         user_num = int(input("please put in a number\n"))
#         if user_num == answer:
#             print(
#                 f"your number matches!, I chose {answer} and you chose {user_num}")
#             break
#         if user_num > answer:
#             print(f"your number is lower")
#             continue
#         if user_num < answer:
#             print(f"your number is greater")
#             continue
#     except ValueError:
#         print("You put in text, put in a number\n")
#         continue
