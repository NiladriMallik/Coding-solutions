class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            if i not in mapping.keys():
                mapping[i] = 1
            else:
                mapping[i] += 1

        for i, n in mapping.items():
            if n > len(nums) / 2:
                return i


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]