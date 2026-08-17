class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            if i not in mapping.keys():
                mapping[i] = 1
            else:
                mapping[i] += 1

        for i, ic in mapping.items():
            if ic == 1:
                return i


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            else:
                if nums[i] != nums[i+1]:
                    return nums[i]