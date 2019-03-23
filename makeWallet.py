'''
Nikki Agrawal
Carl Shan
Intro to Cryptocurrency

Generate a public key and hash it to create an address in Bitcoin
Warning, the final is in bytes
'''

#import the softwares necessary
from hashlib import sha256 #sha256 is the hashing function
from Crypto.PublicKey import RSA #RSA is used to generate the original key
import hashlib
import base58check #base58 is what the final key is in

#generate my key with RSA
key = RSA.generate(2048)

#turn it into a public key
publicKey = key.publickey()

#export the key, because currently it is an object holding the key
publicKey = publicKey.exportKey()

#hash the key with sha256
key256 = hashlib.new('sha256', publicKey).digest()

#hash the key with ripemd160
key160 = hashlib.new('ripemd160', key256).hexdigest()

#turn it into bytes
base58 = bytes(key160, encoding= 'utf-8')

#base58 encode it
finalKey = base58check.b58encode(base58)
print(finalKey)
