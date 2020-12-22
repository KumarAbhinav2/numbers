"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

"""

class Solution:
    def powerOfTwo_intuitive(self, n):
        if n == 0:
            return False
        while n%2 == 0:
            n /= 2
        return n == 1

    # Time Complexity: O(logN)

    def powerOfTwo_GoodOne(self, n):
        if n==0:
            return False
        # X & (-X) i.e x and its complement will always keep rightmost bit set to 1
        # power of two numbers in binary representation will always have only only 1 bit
        return n & (-n) == n

    # Time Complexity: O(1)