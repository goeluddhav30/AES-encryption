
def addRoundKey(state, key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key[i][j]