##CS 333 - Final Project - Vanessa Quijano
import hangman
import rules
import printing

def main():
    #initialize word
    word = rules.choose_word()
    dashes = "_" * len(word)     
    guesses_max = 5   

    #welcome
    printing.welcome_message(word)

    #Game
    while True:       
        printing.display_dashes(dashes)
        guess = input("Guess a letter: ").lower()

        #checking guess
        dashes, guesses_max = hangman.check_guess(guess, word, dashes, guesses_max)

        #checking results
        if rules.check_win(dashes, word):
            break
        elif rules.check_lose(guesses_max):
            break
        print()
        print()

    #end of game
    print("\tThe word was: ", word)

if __name__ == '__main__':
    main()

