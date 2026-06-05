from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while True:
            min_val = float("inf")
            min_idx = -1

            # Für jede Liste schauen, welcher Kopf am kleinsten ist
            for i, node in enumerate(lists):
                if node and node.val < min_val:
                    min_val = node.val
                    min_idx = i

            # Kein Knoten mehr gefunden → alle Listen leer
            if min_idx == -1:
                break

            # Kleinsten Knoten anhängen und Liste weiterrücken
            current.next = lists[min_idx]
            current = current.next
            lists[min_idx] = lists[min_idx].next

        return dummy.next
