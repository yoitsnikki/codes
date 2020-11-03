'''
Nikki Agrawal
Password Coding Implementation for the Threat Model Assignment
'''

import hashlib
import uuid

#get a password
password = input ("insert password: ")
print(password)

#get a salt
string = uuid.uuid4().hex
salt = bytes(string, 'utf-8')
print(salt)

keyhash = bytes(password, 'utf-8')
print(keyhash)

savehash = hashlib.sha256(keyhash + salt).hexdigest()
print (savehash)
