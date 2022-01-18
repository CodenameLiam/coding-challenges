from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # # O(n) memory
        # headASet = set()

        # current = headA
        # while current is not None:
        #     headASet.add(current)
        #     current = current.next

        # current = headB
        # while current not in headASet and current is not None:
        #     current = current.next

        # return current

        # O(1) memory
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1

intersection = ListNode(8, ListNode(4, ListNode(5)))

listA = ListNode(4, ListNode(1, intersection))
listB = ListNode(5, ListNode(6, ListNode(1, intersection)))



solution = Solution().getIntersectionNode(listA, listB)

print()
