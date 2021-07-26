import binascii
import os


key = binascii.hexlify(os.urandom(64))
print(key)