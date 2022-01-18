import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Get first value and the list index for all lists
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        # Put these values into a heap
        heapq.heapify(h)

        # Create nodes for storing the head and current nodes
        head = cur = ListNode(None)
        while h:
            # Get the smallest element from the heap
            val, idx = heapq.heappop(h)

            # Set the next node in the merged list to be the element from the heap
            cur.next = ListNode(val)
            # Move the the next node in the merged list
            cur = cur.next

            # Move the the next node in the current list (and store the result)
            node = lists[idx] = lists[idx].next

            # If the next node exists, add it to the heap
            if node:
                heapq.heappush(h, (node.val, idx))

        return head.next



list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))


sol = Solution().mergeKLists([list1, list2, list3])

print()