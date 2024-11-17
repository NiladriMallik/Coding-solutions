class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = 0
        while True:
            if "" in strs:
                return ""
            if len(strs) == 1 or len(set(strs)) == 1:
                return strs[0]
            if len(set(s[:n] for s in strs)) == 1:
                set_ = set(s[:n] for s in strs)
                n += 1
            else:
                break
        return set_.pop()
        