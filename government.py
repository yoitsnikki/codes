"""
Nikki Agrawal
Carl Shan
Intro to Cryptocurrency

This blockchain will be a simulation of a blockchain that could be used to keep track of citizens
"""

import hashlib
import keyboard

#make the blockchain class
class Blockchain(object):

    #define the beginning parameters
    def __init__(self):
        self.chain = []
        self.citizen = []

        #create the first block to the chain
        self.newBlock(nonce=10, previousCitizen=None, citizenHash=None)

    #adding a new block
    def newBlock(self, nonce, previousCitizen, citizenHash):

        #block should be represented with an index, list of citizens, nonce, and hash id of previous block
        block = {
            "index": len(self.chain) + 1,
            "citizen": self.citizen,
            "nonce": nonce,
            "previous block": previousCitizen,
            "digital signature": citizenHash
        }

        #append the block to the chain and print it
        self.citizen = []
        self.chain.append(block)

        return block

    def newHash(self, nonce, previousCitizen):
        hashedCitizen = {
            "index": len(self.chain) + 1,
            "citizen": self.citizen,
            "nonce": nonce,
            "previous block": previousCitizen,
        }

        return hashedCitizen

    #log a new citizen
    def newCitizen (self, firstName, lastName, birthday, nationality, gender):

        self.citizen.append({
            "First Name": firstName,
            "Last Name": lastName,
            "Birthday": birthday,
            "Nationality": nationality,
            "Gender": gender,
        })

        return self.lastBlock()["index"] + 1

    def newInfo(self, information):
        self.citizen.append({
            "Information": information
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

    # this is the new citizen with the information
    blockchain.newCitizen(
        firstName=input("first name: "),
        lastName=input("last name: "),
        birthday=input ("birthday:"),
        nationality=input("nationality: "),
        gender = input("gender:")
        )

    # this is the new block made with that citizen and nonce
    previousCitizen = blockchain.hash(lastBlock)

    citizenInfo = str(blockchain.newHash(nonce, previousCitizen)).encode('utf-8')
    citizenHash = hashlib.sha256(citizenInfo).hexdigest()

    block = blockchain.newBlock(nonce, previousCitizen, citizenHash)
    print(block)


program = Program()

def Edit():
    # get the nonce set up
    lastBlock = blockchain.lastBlock
    previousNonce = lastBlock()["nonce"]
    nonce = blockchain.proofOfWork(previousNonce)

    # this is the new citizen with the information
    blockchain.newInfo(
        information=input("New Information: ")
    )

    citizenHash = input("citizen's digital signature: ")

    # this is the new block made with that new info and nonce
    previousCitizen = blockchain.hash(lastBlock)
    block = blockchain.newBlock(nonce, previousCitizen, citizenHash)
    print(block)

'''
add a citizen in terminal: press "space" to add a citizen
press "a" to add new info to an already existing citizen
press "e" to end program
sudo python 3 government.py
'''

#terminal, use spacebar

while True:
    if keyboard.is_pressed("space"):
        program = Program()
    if keyboard.is_pressed("a"):
        edit = Edit()
    if keyboard.is_pressed("b"):
        print("")
        print(blockchain.chain)
        print("")
    if keyboard.is_pressed("e"):
        break
