class Solution:    
    def power(self, x, n):
        if n == 0:
            return 1.0000

        elif n == 1:
            return x

        if n % 2 == 0:
            return self.power(x * x, n // 2)

        elif n % 2 != 0:
            return x * self.power(x, n - 1)
        
    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.power(x, -n)
        
        return self.power(x, n)