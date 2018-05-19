#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

print("Welcome to Rock, Paper, Scissors!")

username1 = str(input('Player One, enter your name: '))
username2 = str(input('Player Two, enter your name: '))

player1 = str(input("{}, GO! Rock, Paper or Scissors?: ".format(username1)))
player2 = str(input("{}, GO! Rock, Paper or Scissors?: ".format(username2)))

# More creative solution by defining a function

def compare(p1, p2):
    if p1 == p2:
        return ("It's a Draw!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return ('Rock Wins!')
        else:
            return ('Paper Wins!')
    elif p1 ==  'paper':
        if p2 == 'rock':
            return ('Paper Wins!')
        else:
            return ('Scissors Win!')
    elif p1 == 'scissors':
        if p2 == 'paper':
            return ('Scissors Win!')
        else:
            return('Rock Wins!')
    else:
        return('Invalid input. Please select from: Rock, Paper or Scissors. ')

print(compare(player1, player2))
