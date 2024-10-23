from collections import deque, defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level_sums = defaultdict(int)
        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()
            level_sums[level] += node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        max_sum = max(level_sums.values())
        return min(level for level, sum_ in level_sums.items() if sum_ == max_sum)