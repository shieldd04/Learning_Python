#Hangman

import random

def hangman(word):
    word_list = ["dave", "hilary", "jess", "steph"]
    index = random.randint(0, 4)
    word = word_list[index]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman! A word has been randomly selected for you.")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print ("\n".join(stages[0: e]))
        if "__" not in board:
            print("You Win! It was {}!".format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You Lose! It was {}."
              .format(word))
            
hangman("dave")
