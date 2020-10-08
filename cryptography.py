'''
Nikki Agrawal

just playing around with hashing functions
'''

#import the softwares necessary
import hashlib
import uuid


key = "abcdefghijklmnopqrstuvwxyz"

string = uuid.uuid4().hex
salt = bytes(string, 'utf-8')
print(salt)

key256 = hashlib.sha256(b'hello world' + salt).hexdigest()
print ("256: " + key256)

key512 = hashlib.sha512(b'hello world' + salt).hexdigest()
print ("512: " + key512)

key384 = hashlib.sha384(b'hello world' + salt).hexdigest()
print ("384: " + key384)

key224 = hashlib.sha224(b'hello world' + salt).hexdigest()
print ("224: " + key224)
