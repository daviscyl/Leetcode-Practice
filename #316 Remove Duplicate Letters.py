""" 316. Remove Duplicate Letters
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear
once and only once. You must make sure your result is the smallest in lexicographical order among all possible
results.
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result


# test solition
solution = Solution()
s = "cbacdcbc"
print(solution.removeDuplicateLetters(s))
