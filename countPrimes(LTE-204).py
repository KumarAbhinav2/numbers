"""
Count the number of prime numbers less than a non-negative number, n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""
from math import sqrt

class Solution:

    def countPrime(self, n):
        """
        Following Wikipedia's guide on Sieve of Eratosthenes algo
        """
        # for smaller numbers return quick
        if n < 2:
            return 0
        # Initialising the array to cross out non primes
        A = [1]*n
        # 0 and 1 are not prime numbers
        A[0] = A[1] = 0
        # why sqrt?:
        # let n = ab
        # Either 𝑎 ≤ √𝑛 or 𝑎 ≥ √𝑛 (or both).
        #
        # If 𝑎 ≤ √𝑛 then 𝑏 = 𝑛/𝑎 ≥ 𝑛 /√𝑛 = √𝑛.
        #
        # If 𝑎 ≥ √𝑛 then 𝑏= 𝑛/𝑎 ≤ 𝑛/√𝑛 = √𝑛.
        #
        # So either 𝑎 ≤ √𝑛 or 𝑏 ≤ √𝑛 (or both)
        # So if 𝑛 has any factors other than 1 and itself then some of them will be less than or equal to 𝑛√. (And some of them will be greater than or equal to 𝑛√.)
        # So if you get all the way up to the 𝑛√ and you haven't found any factors yet,
        # then you aren't going to find any because if there were any, some of them would have been found by then.
        # So you might as well quit looking.
        for i in range(2, int(sqrt(n))+1):
            if A[i]:
                # incrementing with i**2, i**2+i, i**3+2i.....n
                # for j in range(i**2, n, i):
                #     A[j] = 0
                A[i*i:n:i] = [0]*len(A[i*i:n:i])
        return sum(A)

        # Time Complexity: O(nloglogn)
        # Space Complexity: O(n)

