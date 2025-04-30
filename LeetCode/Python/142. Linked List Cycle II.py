# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        slow = head
        
        nodes = set()

        pos = None
        while slow.next:
            nodes.add(slow)
            slow = slow.next
            if slow in nodes:
                pos = slow
                break

        return pos
