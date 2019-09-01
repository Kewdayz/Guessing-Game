import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
import matplotlib.pyplot as plt
from random import *


def add_hashes_to_list():
    print("#" * b)


def add_guess_to_list():
    guess_list.append(b)
    hash_list.append("#" * b)


guess_list = []
hash_list = []

random_number = (randint(1, 100))
guess_list.append(random_number)

while True:
    try:
        b = int(input("what is the number between 1 and 100: "))
        add_guess_to_list()
        add_hashes_to_list()
    except ValueError:
        print("Unknown number, please try again")
        pass
    else:
        break


while True:
    if b > random_number:
        print("The number is lower")
        try:
            b = int(input("Guess again: "))
            add_guess_to_list()
            add_hashes_to_list()
        except ValueError:
            print("Unknown number, please try again")
            pass

    elif random_number == b:
        print("YOU GOT IT!!!    " * 3)
        print("Your guesses:")
        print(guess_list[1:])
        p = len(guess_list)
        print("How many times u guessed:")
        print(p - 1)

        with open('output.txt', 'w') as file:
            for output in guess_list[1:]:
                file.write("%i\n" % output)
        with open('output_hash.txt', 'w') as file:
            for output in hash_list:
                file.write('%s\n' % output)

        tg = [x for x in range(len(guess_list))]

        plt.scatter(tg, guess_list, label='Scatter Plot', color='b', s=50)
        plt.xlabel('Guesses\n0 = Number trying to guess')
        plt.ylabel('Number guessed')
        plt.title('Scatter Plot Chart\nof your choices')
        plt.show()
        break

    else:
        print("The number is higher")
        try:
            b = int(input("Guess again:"))
            add_guess_to_list()
            add_hashes_to_list()
        except ValueError:
            print("Unknown number, please try again")
            pass
