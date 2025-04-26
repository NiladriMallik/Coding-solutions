# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This code uses two loops
# This code does not use concept of carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        power = 0
        num1 = 0
        num2 = 0
        temp1 = l1
        temp2 = l2
        while(temp1 is not None or temp2 is not None):
            if temp1:
                num1 += temp1.val * (10 ** power)

            if temp2:
                num2 += temp2.val * (10 ** power)
            
            power += 1

            print(f'Num1: {num1}')
            print(f'Num2: {num2}\n')

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        result = str(num1 + num2)
        print(f'Result is {result}')
        result = list(str(result)[::-1])
        result = list(map(int, result))
        
        resultNode = ListNode()
        temp = resultNode
        for i in range(len(result)):
            temp.val = result[i]
            if i < len(result) - 1:
                temp.next = ListNode()
                temp = temp.next
        
        return resultNode
            
