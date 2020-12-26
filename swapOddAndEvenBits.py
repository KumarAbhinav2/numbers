"""
Swap the odd and even bits of a positive integer with as few operations as possible

Input =  1001 0010
output = 0110 0001
"""

class Solution:
    def swapBits(self, a):
        evenMask = 0xAAAAAAAA
        oddMask = 0x55555555

        evenbits = a & evenMask
        oddbits = a & oddMask

        # shift oddbits by left and evenbits by right
        # for swapping odd bits need to be moved by 1 pos left and even bits by right
        evenbits >>= 1
        oddbits <<= 1

        return evenbits | oddbits

# Time Complexity: O(n), n number of bits
# Space Complexity: O(n), n number of bits