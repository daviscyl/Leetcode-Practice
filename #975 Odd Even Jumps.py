""" #975 Odd Even Jumps

You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd,
5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series
are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is
the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such
index j. During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j]
and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the
smallest such index j. (It may be the case that for some index i, there are no legal jumps.) A starting index
is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some
number of times (possibly 0 or more than once.)

Return the number of good starting indexes.
"""

from random import sample


class Solution:
    def oddEvenJumps(self, A: [int]) -> int:
        L = len(A)
        if L < 2:
            return L

        odds = [False]*(L-1) + [True]
        evens = [False]*(L-1) + [True]

        indexes = sorted(range(L), key=lambda i: A[i])
        odd_jump = self.jump_dests(indexes)
        indexes = sorted(range(L), key=lambda i: -A[i])
        even_jump = self.jump_dests(indexes)

        for i in range(L-2, -1, -1):
            odds[i] = evens[odd_jump[i]] if odd_jump[i] else False
            evens[i] = odds[even_jump[i]] if even_jump[i] else False

        return sum(odds)

    def jump_dests(self, indexes):
        dests = [None] * len(indexes)
        stack = []
        for i in indexes:
            while stack and i > stack[-1]:
                dests[stack.pop()] = i
            stack.append(i)
        return dests


# test solution
solution = Solution()
A = sample(range(100000), 20000)
print(solution.oddEvenJumps(A))
