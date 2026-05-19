1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head
10        prev_group = dummy
11
12        while True:
13            kth = prev_group
14
15            for _ in range(k):
16                kth = kth.next
17                if not kth:
18                    return dummy.next
19            
20            group_next = kth.next
21
22            prev = group_next
23            curr = prev_group.next
24
25            while curr != group_next:
26                temp = curr.next
27                curr.next = prev
28                prev = curr
29                curr = temp
30            
31            temp = prev_group.next
32            prev_group.next = kth
33            prev_group = temp