from typing import Optional

# Digit stored in reverse order in linked list
# [1,2,3] means 321

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_int(l1: Optional[ListNode]):
    print("--------")
    exponent = 1
    total = l1.val
    while l1.next:
        l1 = l1.next
        exponent += 1
        print(total, exponent, l1.val)
        total += (10 ^ exponent) * l1.val
    return total


class Solution:

    # this is broken
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1, l2)
        print(to_int(l1), to_int(l2))