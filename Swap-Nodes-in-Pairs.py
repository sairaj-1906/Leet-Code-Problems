1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # Create a dummy node to act as the preceding node to thr head
9        dummy = ListNode(0, head)
10        prev = dummy
11
12        # We need at least two nodes to perform a swap
13        while head and head.next:
14            # 1. Identify the two nodes to be swapped
15            first_node = head
16            second_node = head.next
17
18            # 2. Perform the swap by updating pointers
19            prev.next = second_node
20            first_node.next = second_node.next
21            second_node.next = first_node
22
23            # 3. Move the pointers forward for the next pair
24            prev = first_node
25            head = first_node.next
26
27        return dummy.next