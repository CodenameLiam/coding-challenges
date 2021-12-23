from typing import Optional

class ListNode:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None


# List 1
list1 = SLinkedList()
list1.headval = ListNode(1)
list1.headval.nextval = ListNode(2)
list1.headval.nextval.nextval = ListNode(4)

# List 2
list2 = SLinkedList()
list2.headval = ListNode(1)
list2.headval.nextval = ListNode(3)
list2.headval.nextval.nextval = ListNode(4)

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # list3 = SLinkedList()

    merged = None

    if list1 is None:
        return list2

    if list2 is None:
        return list1


    if list1.dataval <= list2.dataval:
        merged = list1
        merged.nextval = mergeTwoLists(list1.nextval, list2)
    else:
        merged = list2
        merged.nextval = mergeTwoLists(list1, list2.nextval)

    return merged

merged = mergeTwoLists(list1.headval, list2.headval)

print()