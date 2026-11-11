# 242. Valid Anagram (Easy)
# Idea: count the letters of s, then subtract the letters of t.
# If any count goes negative (or a letter is missing), it is not an anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if count.get(ch, 0) == 0:
                return False
            count[ch] -= 1
        return True
