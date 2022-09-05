#!/usr/bin/python3
import prompt
import random


def main():
    print("Welcome to the brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(0, 100)
        print("Question:", random_number)
        answer = prompt.string("Your answer: ")
        
        if random_number % 2 == 0:
            if answer == "yes":
                print("Correct!")
                i += 1
            elif answer == "no":
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
                break
            else:
                print(f"is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
                break
        if random_number % 2 != 0:
            if answer == "no":
                print("Correct!")
                i += 1
            elif answer == "yes":
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
                break
            else:
                print(f"is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {name}!")
                break
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
