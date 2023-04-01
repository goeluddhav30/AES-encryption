
from copy import deepcopy

a = [[0x02, 0x03, 0x01, 0x01], 
     [0x01, 0x02, 0x03, 0x01],
     [0x01, 0x01, 0x02, 0x03],
     [0x03, 0x01, 0x01, 0x02]] 

# learned from https://web.archive.org/web/20100626212235/http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda b: (((b << 1) ^ 0x1B) & 0xFF) if (b & 0x80) else (b << 1)

def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)

def mixColumns(state):
    # temp = deepcopy(state)
    # for i in range(4):
    #     state[0][i] = ((a[0][0] * temp[0][i]) % 256) ^ ((a[0][1] * temp[1][i]) % 256) ^ ((a[0][2] * temp[2][i]) % 256) ^ ((a[0][3] * temp[3][i]) % 256)
    #     state[1][i] = ((a[1][0] * temp[0][i]) % 256) ^ ((a[1][1] * temp[1][i]) % 256) ^ ((a[1][2] * temp[2][i]) % 256) ^ ((a[1][3] * temp[3][i]) % 256)
    #     state[2][i] = ((a[2][0] * temp[0][i]) % 256) ^ ((a[2][1] * temp[1][i]) % 256) ^ ((a[2][2] * temp[2][i]) % 256) ^ ((a[2][3] * temp[3][i]) % 256) 
    #     state[3][i] = ((a[3][0] * temp[0][i]) % 256) ^ ((a[3][1] * temp[1][i]) % 256) ^ ((a[3][2] * temp[2][i]) % 256) ^ ((a[3][3] * temp[3][i]) % 256)
    for i in range(4):
        mix_single_column(state[i])

def invMixColumns(state):
    # temp = deepcopy(state)
    # for i in range(4):
    #     state[0][i] = ((a[0][0] * temp[0][i]) % 256) ^ ((a[1][0] * temp[1][i]) % 256) ^ ((a[2][0] * temp[2][i]) % 256) ^ ((a[3][0] * temp[3][i]) % 256)
    #     state[1][i] = ((a[0][1] * temp[0][i]) % 256) ^ ((a[1][1] * temp[1][i]) % 256) ^ ((a[2][1] * temp[2][i]) % 256) ^ ((a[3][1] * temp[3][i]) % 256)
    #     state[2][i] = ((a[0][2] * temp[0][i]) % 256) ^ ((a[1][2] * temp[1][i]) % 256) ^ ((a[2][2] * temp[2][i]) % 256) ^ ((a[3][2] * temp[3][i]) % 256)
    #     state[3][i] = ((a[0][3] * temp[0][i]) % 256) ^ ((a[1][3] * temp[1][i]) % 256) ^ ((a[2][3] * temp[2][i]) % 256) ^ ((a[3][3] * temp[3][i]) % 256)
    for i in range(4):
        u = xtime(xtime(state[i][0] ^ state[i][2]))
        v = xtime(xtime(state[i][1] ^ state[i][3]))
        state[i][0] ^= u
        state[i][1] ^= v
        state[i][2] ^= u
        state[i][3] ^= v

    mixColumns(state)