import random
import time
import requests

def main():
    # read a list of 10000 words from an online source
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)

    # convert words from bytes to strings
    word_bytes = response.content.decode('UTF-8')

    # all words should be lower case
    word_bytes = word_bytes.lower()
    
    # split words into a list
    WORDS = word_bytes.splitlines()

    keep_playing = True

    while keep_playing:
        print('Welcome to the game of hangman!')

        used_letters = []

        # system chooses a secret word from list
        secret_word = random.choice(WORDS)

        # populate a string with underscores
        invisible_word = ''
        for i in range(len(secret_word)):
            invisible_word = invisible_word + '_'

        invisible_word = list(invisible_word)

        # total guesses available to the user
        rounds = 8
        alive = True

        while alive:
            print(invisible_word)
            letter_guess = getGuess(s = used_letters)
            used_letters.append(letter_guess)
            print('Test', used_letters)
            count = 0
            prev_word = listToString(invisible_word)
            for i in secret_word:
                if i == letter_guess:
                    invisible_word[count] = letter_guess
                count = count + 1
            next_word = listToString(invisible_word)

            if prev_word == next_word:
                print('The letter was not in the secret word!')
                rounds = rounds - 1

            reveal_word = listToString(invisible_word)
            if reveal_word == secret_word:
                print('Congratulations! You have won the game!')
                print('The word was: ', reveal_word)
                break

            print('Lives remaining: ', rounds)
            if rounds == 0:
                print('You lost. The word was: ', secret_word)
                alive = False

        while True:
            answer = input('Would you like to keep playing? (yes/no)')
            if answer == 'yes':
                print('Enjoy your game!')
                break
            elif answer == 'no':
                print('Thank you for playing!')
                keep_playing = False
                break
            else:
                print('Invalid answer. Please enter yes/no.')



def getGuess(s):
    # request a character from the user
    while True:
        guess = input("Please enter a character: ")
        if guess.isalpha() and len(guess) == 1:
            if s.count(guess) > 0:
                print('This guess was already used! Try again.')
            else:
                return guess
        else:
            print('You\'re guess was invalid')

def listToString(s):
    str1 = ''
    for i in s:
        str1 += i
    return str1

if __name__ == "__main__":
    main()