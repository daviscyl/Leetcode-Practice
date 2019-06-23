""" #336 Palindrome Pairs
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the
concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
"""


class Solution:
    def palindromePairs(self, words: [str]) -> [[int]]:
        return None


# test solution
solution = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(solution.palindromePairs(words))
