class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_value = int(a, 2)
        print(f'Value of {a} is {a_value}')

        b_value = int(b, 2)
        print(f'Value of {b} is {b_value}')

        summ = a_value + b_value
        print(f'Sum = {b_value + a_value}')
        return bin(summ)[2:]
        


