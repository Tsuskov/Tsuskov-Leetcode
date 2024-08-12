
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x) # Node value
        self.next = next # Next node
        self.random = random # Random node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        oldTocopy = {None: None} # Create a dictionary to store the old node to the copied node null mapping to null
        cur = head # Set the current node to the head
        while cur: # While the current node is not None
            copy = Node(cur.val) # Create a new node with the value of the current node
            oldTocopy[cur] = copy # Add the current node to the copied node mapping
            cur = cur.next # Move the current node to the next node
            
        cur = head # Set the current node to the head
        while cur: # While the current node is not None
            copy = oldTocopy[cur] # Get the copied node of the current node
            copy.next = oldTocopy[cur.next] # Set the next node of the copied node to the copied node of the next node
            copy.random = oldTocopy[cur.random] # Set the random node of the copied node to the copied node of the random node
            cur = cur.next # Move the current node to the next node
        return oldTocopy[head] # Return the copied node of the head
    
x = Solution()
l1 = Node(2, Node(4, Node(3)))