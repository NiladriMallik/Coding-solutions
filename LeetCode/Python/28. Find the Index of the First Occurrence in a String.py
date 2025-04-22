class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)

        if needle in haystack:
            indices = [index for index, value in enumerate(haystack) if value == needle[0]]
            for j in indices:
                if haystack[j : j + l] == needle:
                    return j
        else:
            return -1
