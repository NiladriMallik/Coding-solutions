class Solution:
    def mySqrt(self, x: int) -> int:
    
        if x in [0, 1]:
            return x

        for i in range(x):
            if i ** 2 <= x and (i + 1) ** 2 > x:
                return i

#######################################################################

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i = 2
        while i * i <= x:
            i += 1
        return i - 1

#######################################################################

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x

        lower = 2
        higher = x
        while lower <= higher:
            mid = lower + (higher - lower) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lower = mid + 1
            if mid * mid > x:
                higher = mid - 1

        return higher