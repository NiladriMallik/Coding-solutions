class Solution:
    def mySqrt(self, x: int) -> int:
    
        if x in [0, 1]:
            return x

        for i in range(x):
            if i ** 2 <= x and (i + 1) ** 2 > x:
                return i