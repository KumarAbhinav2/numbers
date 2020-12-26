"""
Determine number of bits to flip to convert int a into int b

input = 11101 & 01111
output = 2
"""

class Solution:
    def flipBits(self, A, B):
        # doing xor to identify diff bits
        c = A ^ B
        count = 0
        # now counting all the diff bits
        while count:
            count += c & 1
            c >>= 1
        return count

    # Time Complexity: O(b), b is number of bits
    # Space Complexity: O(b), b is number of bits

    