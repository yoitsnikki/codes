"""
Nikki Agrawal
Carl Shan
Intro to Cryptocurrency

Create your own Blockchain, including a block, chain, and simulated mining
"""

import hashlib
import random
import keyboard

#make the blockchain class
class Blockchain(object):

    #define the beginning parameters
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

        #create the first block to the chain
        self.newBlock(nonce=10, previousTransaction=None)

    #adding a new block
    def newBlock(self, nonce, previousTransaction):

        #block should be represented with an index, list of transactions, nonce, and hash id of previous block
        block = {
            "index": len(self.chain) + 1,
            "transaction": self.currentTransactions,
            "nonce": nonce,
            "previous block": previousTransaction
        }

        #append the block to the chain and print it
        self.currentTransactions = []
        self.chain.append(block)

        return block

    #making a new transaction between people
    def newTransaction(self, sender, recipient, amount):

        self.currentTransactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

        return self.lastBlock()["index"] + 1

    #the last validated block (for the previous transaction part of the block)
    def lastBlock(self):
        return self.chain[-1]

    #the id of the block once it is hashed
    def hash(self, block):
        blockHash = str(block()).encode()
        blockHash = hashlib.sha256(blockHash).hexdigest()
        return blockHash

    #checks if the nonce is valid or not
    def validNonce(self, previousNonce, nonce):

        attempt = hashlib.sha256(f'{previousNonce}{nonce}'.encode()).hexdigest()
        return attempt[:3] == "000"

    #keeps generating new nonces if the old one doesn't work according to validNonce
    def proofOfWork(self, previousNonce):

        nonce = 0
        while self.validNonce(previousNonce, nonce) is False:
            nonce = nonce + 1

        return nonce

#deploys the blockchain
blockchain = Blockchain()

#what should be done to the blockchain
def Program():
    #get the nonce set up
    lastBlock = blockchain.lastBlock
    previousNonce = lastBlock()["nonce"]
    nonce = blockchain.proofOfWork(previousNonce)

    # this is the new transaction with the randomized amounts
    blockchain.newTransaction(
        sender=random.randint(100000, 1000000),
        recipient=random.randint(100000, 1000000),
        amount=random.randint(100000, 1000000)
        )

    # this is the new block made with that transaction and nonce
    previousTransaction = blockchain.hash(lastBlock)
    block = blockchain.newBlock(nonce, previousTransaction)
    print(block)

'''
two options for running the program - input how many transactions should be added in python
or go to terminal and using sudo, press the spacebar to add a transaction
'''

#input, in python
'''
#how many transactions/blocks should be added
testing = input("add ____ no. transactions to blockchain?")

#title
print("")
print("BLOCKCHAIN")
print("")

print(blockchain.chain)

#adds the number of transactions inputed
x = int(testing)
while x > 0:
    program = Program()
    x = x-1

'''

#terminal, use spacebar

while True:
    if keyboard.is_pressed("space"):
        program = Program()
    if keyboard.is_pressed("e"):
        break
