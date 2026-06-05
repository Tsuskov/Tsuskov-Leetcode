# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: # If left is equal to right
            return head # Return the head
        dummy = ListNode() # Create a dummy node
        dummy.next = head # Set the next node of the dummy node to the head
        prev = dummy # Set the previous node to the dummy node
        for _ in range(left - 1): # Loop through the left - 1 times
            prev = prev.next # Move the previous node to the next node
        cur = prev.next # Set the current node to the next node of the previous node
        for _ in range(right - left): # Loop through the right - left times
            temp = prev.next   # 1
            prev.next = cur.next # 2
            cur.next = cur.next.next  # 3
            prev.next.next = temp # 4
        return dummy.next # Return the next node of the dummy node
    
x = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(x.reverseBetween(l1, 2, 4).val) # 1