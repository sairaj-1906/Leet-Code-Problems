1#Definition for singly-linked list.
2#class ListNode:
3#    def __init__(self, val=0, next=None):
4#        self.val = val
5#        self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)  # Placeholder head
9        current = dummy
10        carry = 0
11        # Continue while there are digits left in l1, l2, or a remaining carry
12        while l1 or l2 or carry:
13            # Get values, using 0 if we've reached the end of a list
14            val1 = l1.val if l1 else 0
15            val2 = l2.val if l2 else 0
16            # Calculate sum and new carry
17            total = val1 + val2 + carry
18            carry = total // 10
19            new_digit = total % 10
20            # Add new node to result
21            current.next = ListNode(new_digit)
22            current = current.next
23            # Move pointers if possible
24            if l1: l1 = l1.next
25            if l2: l2 = l2.next
26        return dummy.next
27        