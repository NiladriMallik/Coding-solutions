from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicta = Counter(s)
        for i in range(len(s)):
            if dicta[s[i]] == 1:
                return i

        return -1