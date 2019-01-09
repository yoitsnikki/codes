'''
Tic Tac Toe Game
By: Niharika Agrawal
Advanced Computers D1
Date: Sep 27, 2017
'''

#The table object which will keep track of the table.
#It will indicate if there is a winner, a tie or a space is free.
#This class will draw the board to the screen and update the board with player's moves.

class Table:
    def __init__(self):
        self.lop = [" "] * 10

    def drawTable(self):
        print(" | | ")
        print(" " + self.lop[1] + " | " + self.lop[2] + " | " + self.lop[3])
        print(" | | ")
        print("-----------")

        print(" | | ")
        print(" " + self.lop[4] + " | " + self.lop[5] + " | " + self.lop[6])
        print(" | | ")
        print("-----------")

        print(" | | ")
        print(" " + self.lop[7] + " | " + self.lop[8] + " | " + self.lop[9])
        print(" | | ")



    def isSpaceAvailable(self, pos):
        if (self.lop[pos] != " "):
            return False
        else:
            return True

    def updateTable(self, letter, position):
        self.lop[position] = letter

    def isWinner(self, letter):
        #check horizontal lines
        if (self.lop[1] == letter and self.lop[2] == letter and self.lop[3] == letter):
            return True
        elif (self.lop[4] == letter and self.lop[5] == letter and self.lop[6] == letter):
            return True
        elif (self.lop[7] == letter and self.lop[8] == letter and self.lop[9] == letter):
            return True
    
        #check vertical lines
        elif (self.lop[1] == letter and self.lop[4] == letter and self.lop[7] == letter):
            return True
        elif (self.lop[2] == letter and self.lop[5] == letter and self.lop[8] == letter):
            return True
        elif (self.lop[3] == letter and self.lop[6] == letter and self.lop[9] == letter):
            return True

        #diagonal lines
        elif (self.lop[1] == letter and self.lop[5] == letter and self.lop[9] == letter):
            return True
        elif (self.lop[3] == letter and self.lop[5] == letter and self.lop[7] == letter):
            return True

        else:
            return False

    def isTie(self):
        #assume the list of positions is completely taken
        empty = False

for i in range(1, len(self.lop)):
    if (self.lop[i] == " "):
        #found an empty space
        empty = True
        break

    return not empty
