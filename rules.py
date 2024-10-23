import random

def choose_word():
    words_list = ["soup", "chicken", "banana", "pasta", "orange", "eggs", "burger", "cereal", "salmon"]
    return random.choice(words_list)

def check_win(word, dashes):
    if word == dashes:
        print("\n\tGame End: You Win!")
        return True
    else:
        return False

def check_lose(max_guesses):
    if max_guesses == 0:
        print("\n\tGame End: You Lose!")
        return True
    else:
        return False