from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        while (l1.next == None):
            print(l1.val)
            print(l2.val)
            print(2)
            l1 = l1.next
            l2 = l2.next
            


sol = Solution()
sol.addTwoNumbers([2,4,3],[5,6,4])