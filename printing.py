#hangman printing

def welcome_message(word):
    ## -- Only Printing the welcome message
    length = len(word)
    print()
    print("\t\t* * Hangman Game * *")
    print("\t\tWelcome. The word has", length, "letters.")
    print("\t\tTopic: Food\n")

def display_dashes(dashes):
    ## - - Only Printing the game dashes
    display = ""
    count = 0
    for dash in dashes:
        if dash == "_":
            display += " __ "
        else:
            result = " "
            result += dashes[count]
            result += " "
            display += result
        count += 1
    print()
    print("\t\t",display, "\n")
