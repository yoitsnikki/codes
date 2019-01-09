'''
Tic Tac Toe Main Program
By: Nikki Agrawal
Advanced Computers D1
Date: Sep 27, 2017
'''

#This is the main program of the game Tic Tac Toe. It will run each command sequentially. It imports classes Table and Player. They are on separate codes.

import table
import player

print("Hello! Welcome to the Tic Tac Toe Game! To play, all you have to do is enter the position you want to play in. You will be playing against the AI.")
print("This is what the game board will look like in terms of positions. To enter a position you enter a number, like 1 or 2.")

print("")

#Visual of what the game board will look like.")
print(" | | ")
print(" 1 | 2 | 3 ")
print(" | | ")
print("-----------")
print(" | | ")
print(" 4 | 5 | 6 ")
print(" | | ")
print("-----------")
print(" | | ")
print(" 7 | 8 | 9 ")
print(" | | ")

print("")

#instantiate variables from classes Table and Player
tableForGame = table.Table()
player1 = player.Player()
player2 = player.Computer()

playerLetter = input("Player 1, pick a letter- X or O. Don't put a space after you type in the letter.")

#hard code player1 as x and player2 as O
player1.setLetter(playerLetter)

if playerLetter == "X":
    player2.setLetter("O")
else:
    player2.setLetter("X")

#sets the name in the player object
nameGiven1 = input("Player 1, please enter a name for yourself.")

#set the name in the player object
player1.setName(nameGiven1)
player2.setName(" The Computer")

while True:
    pos = player1.getNextMove(tableForGame, player2.letter)

if (tableForGame.isSpaceAvailable(pos) == True):
    tableForGame.updateTable(player1.letter, pos)

    tableForGame.drawTable()

if (tableForGame.isWinner(player1.letter) == True):
    print(player1.name + " is the winner!")
    break

if (tableForGame.isTie()):
    print(player1.name + " and " + player2.name + " have tied! NOBODY WINS!")
    break

#Player 2's turn
pos = player2.getNextMove(tableForGame, player2.letter)

if (tableForGame.isSpaceAvailable(pos) == True):
    tableForGame.updateTable(player2.letter, pos)

    tableForGame.drawTable()

if (tableForGame.isWinner(player2.letter) == True):
    print(player2.name + " is the winner!")
    break

if (tableForGame.isTie()):
    print(player1.name + " and " + player2.name + " have tied! NOBODY WINS!")
    break
