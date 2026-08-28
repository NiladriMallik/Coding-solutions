class Solution:
    def isHappy(self, n: int) -> bool:
        happy_nums = []
        while True:
            n = str(n)
            result = 0
            for i in n:
                result += int(i) ** 2
            print(result)

            if result == 1:
                return True
            if result in happy_nums:
                return False
            else:
                happy_nums.append(result)
                n = result
