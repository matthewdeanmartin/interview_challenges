# I solved this by converting it out of a linked list to a more familiar list
# then converting it back to a linked list.
# This can't possibly be optimal, wrt performance.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        assert list1 is not None, "expect a list1"
        assert list2 is not None, "expect a list"
        combined = []
        copy_list1 = list1
        copy_list2 = list2

        # ListNode doesn't support iterate. Not time to implement dunder method
        while list1 is not None:
            combined.append(list1.val)
            list1 = list1.next
        print(combined)
        assert combined, "Expect something"
        while list2 is not None:
            combined.append(list2.val)
            list2 = list2.next
        print(combined)
        assert combined, "Expect something"
        combined = list(sorted(combined))
        current_node = ListNode(combined[0])
        head_node = current_node
        for value in combined[1:]:
            next_node = ListNode(value)
            current_node.next = next_node
            current_node = next_node
        return head_node
