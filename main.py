import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f"guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    print(f"You guessed {random_number} correctly!")

guess(10)