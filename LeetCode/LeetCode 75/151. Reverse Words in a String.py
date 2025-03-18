class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i for i in s.strip().split(" ") if len(i) > 0]
        s.reverse()
        return " ".join(s)