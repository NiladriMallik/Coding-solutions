    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []

        for i, num in enumerate(nums):
            print(i, num)
            j = target - num
            if j in hashmap:
                return [hashmap[j], i]

            hashmap[num] = i
        return []

######################################################

