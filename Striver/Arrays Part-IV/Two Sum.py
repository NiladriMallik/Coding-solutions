class Solution:
    def twoSum(self, nums, target):
        
        hm = {}
        for num in nums:
            if target - num in hm.values():
                return sorted([nums.index(num), nums.index(target - num)])
            else:
                hm[nums.index(num)] = num
            print(num, hm)