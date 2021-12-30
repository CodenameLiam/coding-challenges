# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# if not duplicate, result.next = head
# if duplicate, ignore

class Solution:

    appeared = {}

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head


# List 1
list1 = ListNode(1)
list1.next = ListNode(1)
list1.next.next = ListNode(2)


test = Solution().deleteDuplicates(list1)

print()