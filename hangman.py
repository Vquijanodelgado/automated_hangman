#hangman

def check_guess(guess, word, dashes, guesses_max):
    #length checking input
    if len(guess) != 1:
        print("Please guess one letter at a time!")
    else:
        #good guess - update dashes
        if guess in word:
            dashes = update_dashes(word, dashes, guess)
        #wrong guess - decrement guesses left
        else:
            guesses_max = minus_guesses(guesses_max)
            print("Incorrect. Guesses left:", guesses_max)
    return dashes, guesses_max

def update_dashes(word, dashes, guess):
    result = ""
    for i in range(len(word)):
        if word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result

def minus_guesses(guesses_max):
    guesses_max -= 1
    return guesses_max