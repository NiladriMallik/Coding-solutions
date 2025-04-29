class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        import itertools
        letter_mapping = {
            '1': [],
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        lists = []
        l = len(digits)

        if l == 0:
            return []

        else:
            lists = [letter_mapping[digits[i]] for i in range(0, l)]
            result = list(itertools.product(*lists))
            return ["".join(i) for i in result]