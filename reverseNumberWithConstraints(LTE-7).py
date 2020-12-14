"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed
integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows.


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
"""

class Solution:
    def reverseNumber(self, x):
        res = 0
        sign = [1, -1][x>0]
        x = abs(x)
        while x > 0:
            q, r = divmod(x, 10)
            res = res*10+r
            x = x//10
        if res > 2**31 - 1:return 0
        return res if sign < 0 else -res


    # Time Complexity: O(logx)
    # space Complexity: O(1)