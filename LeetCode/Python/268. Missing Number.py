class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if mid < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left