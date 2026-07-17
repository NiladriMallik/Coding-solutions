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
        

#################################################################

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)

        first = strs[0]
        last = strs[-1]
        minLength = min(len(first), len(last))

        i = 0

        # Find the common prefix between the first and last strings
        while i < minLength and first[i] == last[i]:
            i += 1

        return first[:i]