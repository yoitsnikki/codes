'''
Tic Tac Toe Game
By: Niharika Agrawal
Advanced Computers D1
Date: Sept 27, 2017
'''

import copy
import table

#The player class keeps track of attributes for each player. It will hold the letter of the player, retrieve the next move.

class Player:
    def __init__(self):
        self.letter = ""
        self.name = ""

    def setLetter(self, letterChoice):
        self.letter = letterChoice
    
    def setName(self, nameChoice):
        self.name = nameChoice

    def getNextMove(self, tableForGame, opponentLetter):
        nextMove = int(input(self.name + " Please enter the position for your move: "))
        return nextMove

#This second class is a child class for the original Player to code to AI version

class Computer(Player):
    def getNextMove(self, tableForGame, opponentLetter):

        #check for a winning move

        for index in range(1,10):
            cGame = copy.deepcopy(tableForGame)

        if (cGame.isSpaceAvailable(index)):
            cGame.updateTable(self.letter, index)

        if(cGame.isWinner(self.letter)):
            return index

        #Check for Opponents Move

        for index in range(1,10):
            cGame = copy.deepcopy(tableForGame)

            if (cGame.isSpaceAvailable(index)):
                cGame.updateTable(self.letter, index)

            if(cGame.isWinner(self.letter)):
                return index

            #Check the corners

        if (cGame.isSpaceAvailable(1)):
            return 1
        elif (cGame.isSpaceAvailable(3)):
            return 3
        elif (cGame.isSpaceAvailable(7)):
            return 7
        elif (cGame.isSpaceAvailable(9)):
            return 9

        #check the middle
        elif (cGame.isSpaceAvailable(5)):
            return 5
        elif (cGame.isSpaceAvailable(2)):
            return 2
        elif (cGame.isSpaceAvailable(8)):
            return 8
        elif (cGame.isSpaceAvailable(4)):
            return 4
        elif (cGame.isSpaceAvailable(6)):
            return 6

print("")
print("")

nextMove = int(input(self.name + " Please enter the position for your move: "))
return nextMove

