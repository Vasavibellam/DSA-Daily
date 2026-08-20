class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return bool(False)
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return bool(False)
            count[char] -= 1
        return bool(True)
        