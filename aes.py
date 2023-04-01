
import random
from expandKey import expandKey
from addRoundKey import addRoundKey
from substitution import subBytes, invSubBytes
from shiftRows import shiftRows, invShiftRows
from mixColumns import mixColumns, invMixColumns
import cv2
import numpy as np
from helper import *

# Load the image
image = cv2.imread("image.png", flags=cv2.IMREAD_GRAYSCALE)
# Convert image to 1D list
plaintext = image.flatten().tolist()

print("plainText: ", plaintext)
# Convert plaintext to grey scale image
cv2.imshow("Source image", np.array(plaintext).reshape(64, 64).astype(np.uint8))
cv2.waitKey(0)

# Key/ message packet length in bytes
n = 16
# Number of rounds
r = 10

# Random 128 bit key
init_key = random.sample(range(0, 255), n)
key_matrix = expandKey(init_key, n)

# Convert plaintext to list of n-bit blocks
blocks = to_blocks(plaintext, n)

cipherText = []

def encrypt(blocks, key_matrix):
    for block in blocks:
        # Plain text block to matrix
        plain_block = array2matrix(block)
        # Add round key
        addRoundKey(plain_block, key_matrix[0])

        for i in range(1, r):
            subBytes(plain_block)
            shiftRows(plain_block)
            mixColumns(plain_block)
            addRoundKey(plain_block, key_matrix[i])
        
        subBytes(plain_block)
        shiftRows(plain_block)
        addRoundKey(plain_block, key_matrix[r])
        
        cipherText.append(matrix2array(plain_block))

encrypt(blocks, key_matrix)

# 1 dimensional list of cipher text in hex values
cipherText = from_blocks(cipherText)

print("\n\ncipherText: ", cipherText)
# Convert cipher text to grey scale image
cv2.imshow("Encrypted image", np.array(cipherText).reshape(64, 64).astype(np.uint8))
cv2.waitKey(0)

blocks = to_blocks(cipherText, n)

decryptedText = []

def decrypt(blocks, key_matrix):
    for block in blocks:
        # Cipher text block to matrix
        cipher_block = array2matrix(block)
        # Add round key
        addRoundKey(cipher_block, key_matrix[r])

        for i in range(r-1, 0, -1):
            invShiftRows(cipher_block)
            invSubBytes(cipher_block)
            addRoundKey(cipher_block, key_matrix[i])
            invMixColumns(cipher_block)
        
        invShiftRows(cipher_block)
        invSubBytes(cipher_block)
        addRoundKey(cipher_block, key_matrix[0])

        decryptedText.append(matrix2array(cipher_block))

decrypt(blocks, key_matrix)

# 1 dimensional list of decrypted text in hex values
decryptedText = from_blocks(decryptedText)

print("\n\ndecryptedText", decryptedText)
# Convert decrypted text to grey scale image
cv2.imshow("Decrypted image", np.array(decryptedText).reshape(64, 64).astype(np.uint8))
cv2.waitKey(0)

print("Are the original and decrypted images same? ", plaintext == decryptedText)