class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        y = y[::-1]
        return y == str(x)