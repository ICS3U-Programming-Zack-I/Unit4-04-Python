# Created by: Zack Isingoma
# Created on: 11th Jan 2022.
# uses a while true loop to
# that doesnt let users exit untill they get
# they guess the right number

import random


def main():
    max_num = int(input("Enter the number range: "))
    correct_num = random.randint(1, max_num)
    while True:
        user_number = input("Guess a number between 1 and {}: "
                            .format(max_num))
        try:
            user_int = int(user_number)
            if user_int > correct_num:
                print("Your guess is too high.Try again")

            elif user_int < correct_num:
                print("Your guess is too low. Try again")

            elif user_int == correct_num:
                print("You guessed right.")
                break
        except Exception:
            print("invalid input")

    print("Thanks for playing")


if __name__ == "__main__":
    main()
