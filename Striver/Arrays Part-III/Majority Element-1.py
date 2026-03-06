class Solution:
    def majorityElement(self, nums):
        hmp = {}

        for i in nums:
            if i in hmp:
                hmp[i] += 1
            else:
                hmp[i] = 1

        for nums, count in hmp.items():
            if count > len(hmp) // 2:
                return nums

        return -1

sol = Solution()
num_list = [1, 1, 1, 2, 1, 2]
num_list = [-1, -1, -1, -1]
me = sol.majorityElement(num_list)
print(me)