# File: sparkle256.py
"""
SPARKLE-256 Lightweight Cryptographic Implementation
Author: Aryan Srivastava (aryansrivastava708@gmail.com)
Reference: NIST LWC Specification v1.2
"""

def rotate_right(x, n, bits=32):
    return (x >> n) | ((x << (bits - n)) & (2**bits - 1))

class Sparkle256:
    RCON = [0xB7E15162, 0xBF715880, 0x38B4DA56, 0x324E7738,
            0xBB1185EB, 0x4F7C7B57, 0xCFBFA1C8, 0xC2B3293D]

    @staticmethod
    def alzette(x, y, rc):
        for _ in range(4):
            x = (x + rotate_right(y, 31)) & 0xFFFFFFFF
            y ^= rotate_right(x, 24)
            x ^= rc
            x, y = y, x  # Swap for next round
        return x, y

    @staticmethod
    def linear_layer(state):
        tmpx = state[0] ^ state[2] ^ state[4] ^ state[6]
        tmpy = state[1] ^ state[3] ^ state[5] ^ state[7]
        tmpx = rotate_right(tmpx ^ (tmpx << 16), 16)
        tmpy = rotate_right(tmpy ^ (tmpy << 16), 16)
        return tmpx, tmpy

    @staticmethod
    def sparkle(state, steps=10):
        for step in range(steps):
            # Add round constant
            state[1] ^= Sparkle256.RCON[step % 8]
            state[0] ^= step

            # ARX Layer
            for i in range(0, 8, 2):
                rc = Sparkle256.RCON[i//2 % 8]
                state[i], state[i+1] = Sparkle256.alzette(state[i], state[i+1], rc)

            # Linear Layer
            tmpx, tmpy = Sparkle256.linear_layer(state)
            
            # State update
            new_state = state[2:] + [state[0] ^ tmpx, state[1] ^ tmpy]
            state = new_state
        return state