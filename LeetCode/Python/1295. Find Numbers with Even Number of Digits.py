class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            count += int(len(str(i)) % 2 == 0)
        
        return count
