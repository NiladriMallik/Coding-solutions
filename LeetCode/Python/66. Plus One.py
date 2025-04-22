class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(list(map(str, digits)))
        num = list(map(int, str(int(num) + 1)))
        return num
