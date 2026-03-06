class Solution:
    def findMaxConsecutiveOnes(self, nums):
        c = 0
        c1 = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                if c > c1:
                    c1 = c
                c = 0
        return c1