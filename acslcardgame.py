'''
Nikki Agrawal
Adv. Computers D1
Mrs. Dastur
15 May 2017
'''

inputStr = input("Give me an input")
cardDeck = list(inputStr)

print(cardDeck)
'''
#Establish the card deck and direction of the game for testing faster, and for inputting in

cardDeck = [87, 5, 8, 9, 7, 4, 6, 3, 9, 0, 2]
cardDeck = [78, 2, 4, 8, 3, 8, 5, 0, 6, 9, 8]
cardDeck = [85, 7, 9, 7, 6, 5, 9, 4, 5, 0, 1]
cardDeck = [84, 8, 4, 2, 7, 9, 0, 1, 9, 8, 3]
cardDeck = [95, 9, 0, 9, 0, 1, 0, 1, 0, 2, 5]
'''

#Establish all the changing variables
pointTotal = cardDeck[0]
playerHand = [cardDeck[1], cardDeck[2], cardDeck[3]]
dealerHand = [cardDeck[5], cardDeck[7], cardDeck[9]]

x = 2
y = 0
playerWin = False
playerTurn = True

#print("pointsTotal: " + str(pointTotal))
#print("playerHand: " + str(playerHand))
#print("dealerHand: " + str(dealerHand))
#print("")

while pointTotal < 100 and len(playerHand) > 0:
    #print("x: " + str(x) + " y: " + str(y) + " pointTotal: " + str(pointTotal))
    #print("playerHand: " + str(playerHand))

    # Player Turn
    if playerTurn == True:
        if playerHand[0] == 4:
            pointTotal = pointTotal - 10
            playerHand.remove(playerHand[0])
        elif playerHand[0] == 9:
            playerHand.remove(playerHand[0])
        elif playerHand[0] == 0:
            if pointTotal + 11 <= 99:
                pointTotal = pointTotal + 11
                playerHand.remove(playerHand[0])
            else:
                pointTotal = pointTotal + 1
                playerHand.remove(playerHand[0])
        else:
            pointTotal = pointTotal + playerHand[0]
            playerHand.remove(playerHand[0])

        x = x + 2
        if x < 11:
            playerHand.append(cardDeck[x])
        if pointTotal >= 100:
            playerWin = False
            break
        playerTurn = False

    # Dealer Turn
    else: 
        if dealerHand[y] == 4:
            pointTotal = pointTotal - 10
        elif dealerHand[y] == 9:
            pointTotal = pointTotal
        elif dealerHand[y] == 0:
            if pointTotal + 11 <= 99:
                pointTotal = pointTotal + 11
            else:
                pointTotal = pointTotal + 1
        else:
            pointTotal = pointTotal + dealerHand[y]

        y = y + 1
        if pointTotal >= 100:
            playerWin = True
            break
        playerTurn = True

# After the while loop is over
if playerWin == False:
    print(str(pointTotal) + ", Dealer")
else:
    print(str(pointTotal) + ", Player")


