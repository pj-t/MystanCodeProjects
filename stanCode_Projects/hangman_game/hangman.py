"""
File: hangman.py
Name: Baron
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    It is a hangman game.

    Decomposition
    1. First check boundary condition (i.e illegal format)
    2. Use while loop because there is a infinite guess
    3. Determine guessed letter if it is in the assigned word
    4. If not, break the while loop after seven guesses
    5. If yes, the re-string is used based on three different conditions:
       new letter, letter already guessed and dash
    """

    #
    word = random_word()
    # Concept: assign variable out of the while loop.
    current = '-' * len(word)
    n = N_TURNS

    print('THe word looks like ' + current)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')

    while True:
        # The str.upper() is used to avoid case-sensitive
        guess = input('Your guesses: ').upper()

        if guess.isdigit() or len(guess) != 1:
            print('Illegal format.')

        else:
            if guess not in word:
                n -= 1
                if n == 0:
                    print('There is no ' + guess + '\'s ' + 'in the world')
                    print('You are completely hang : (')
                    print('The word was: ' + word)
                    break
                else:
                    print('There is no ' + guess + '\'s ' + 'in the world')
                    print('THe word looks like ' + current)
                    print('You have ' + str(n) + ' wrong guesses left.')

            else:

                ans = ""
                for i in range(len(word)):
                    if guess == word[i]:
                        ans += guess
                    elif word[i] in current:
                        ans += word[i]
                    else:
                        ans += "-"
                current = ans
                print('You are correct!')
                print('THe word looks like ' + current)
                print('You have ' + str(n) + ' wrong guesses left.')

                if current == word:
                    print('You are correct!')
                    print('You win!!')
                    print('The word was: ' + word)
                    break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
