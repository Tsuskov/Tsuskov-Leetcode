
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode() # Create a dummy node
            cur = dummy # Set the current node to the dummy node
            carry = 0 # Initialize the carry to 0
            while l1 or l2 or carry: # While l1 or l2 or carry is not None
                x = l1.val if l1 else 0 # Get the value of l1 if l1 is not None, else set it to 0
                y = l2.val if l2 else 0 # Get the value of l2 if l2 is not None, else set it to 0
                total = x + y + carry # Calculate the total sum
                carry = total // 10 # Calculate the carry
                cur.next = ListNode(total % 10) # Set the next node to the remainder of the total sum
                cur = cur.next # Move the current node to the next node
                if l1: l1 = l1.next # Move l1 to the next node
                if l2: l2 = l2.next # Move l2 to the next node
            return dummy.next

x = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(x.addTwoNumbers(l1, l2).val) # 7cur.next = ListNode(total % 10)


          