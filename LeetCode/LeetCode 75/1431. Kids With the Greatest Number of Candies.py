class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_2 = [i + extraCandies for i in candies]
        return [i >= max(candies) for i in candies_2]