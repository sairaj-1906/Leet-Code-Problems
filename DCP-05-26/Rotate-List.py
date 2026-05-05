1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next or k == 0:
9            return head
10        
11        length = 1
12        tail = head
13        while tail.next:
14            tail = tail.next
15            length += 1
16
17        tail.next = head
18
19        k = k % length
20        steps_to_new_head = length - k
21
22        new_tail = head
23        for _ in range(steps_to_new_head - 1):
24            new_tail = new_tail.next
25        
26        new_head = new_tail.next
27
28        new_tail.next = None
29
30        return new_head
31
32    def build_linked_list(values):
33        if not values:
34            return None
35        head = ListNode(values[0])
36        current = head
37        for val in values[1:]:
38            current.next = ListNode(val)
39            current = current.next
40        return head
41
42    def linked_list_to_list(head):
43        result = []
44        while head:
45            result.append(head.val)
46            head = head.next
47        return result