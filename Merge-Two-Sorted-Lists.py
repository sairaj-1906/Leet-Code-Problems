1# Definition for singly-linked list.
2class ListNode:
3     def __init__(self, val=0, next=None):
4         self.val = val
5         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        #1. Initialize dummy node and tail pointer
9        dummy = ListNode(-1)
10        tail = dummy
11        #2.Iterate while both lists have nodes
12        while list1 and list2:
13            if list1.val <= list2.val:
14                tail.next = list1
15                list1 = list1.next
16            else:
17                tail.next = list2
18                list2 = list2.next
19            #Move tail forward
20            tail = tail.next
21        #3.Attach the remaining node (if any)
22        if list1:
23            tail.next = list1
24        elif list2:
25            tail.next = list2
26        #4.Return the start of the merged list (skipping dummy)
27        return dummy.next
28        