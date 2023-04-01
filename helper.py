
def array2matrix(array, rows = 4, cols = 4):
    return [array[i:i+cols] for i in range(0, rows*cols, cols)]

def matrix2array(matrix):
    return [item for sublist in matrix for item in sublist]

def to_blocks(plaintext, n):
    blocks = []
    for i in range(0, len(plaintext), n):
        blocks.append(plaintext[i:i+n])
    return blocks

def from_blocks(blocks):
    plaintext = []
    for block in blocks:
        plaintext += block
    return plaintext