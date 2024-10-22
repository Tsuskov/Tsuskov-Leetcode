#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
 
        nodes = []
        current = head
        while current:
            nodes.append(current.val)
            current = current.next
        

        max_twin_sum = 0
        n = len(nodes)
        for i in range(n // 2):
            twin_sum = nodes[i] + nodes[n - 1 - i]
            max_twin_sum = max(max_twin_sum, twin_sum)
        
        return max_twin_sum