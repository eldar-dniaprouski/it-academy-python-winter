import random

guesses_num = 0

name = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

while guesses_num < 6:

    guess = int(input('Take a guess: '))

    guesses_num += 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print('Good, {0}! Guessed right in {1} tries!'.format(name, guesses_num))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))
