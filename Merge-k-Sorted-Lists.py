1import heapq
2# Definition for singly-linked list.
3# class ListNode:
4#     def __init__(self, val=0, next=None):
5#         self.val = val
6#         self.next = next
7
8class Solution:
9    def mergeKLists(self, lists):
10        # Initialize the heap
11        heap = []
12        
13        # Step 1: Push the head of each linked list into the min-heap
14        for i, lst in enumerate(lists):
15            if lst:
16                # Tuple format: (node_value, tie_breaker, node)
17                heapq.heappush(heap, (lst.val, i, lst))
18        
19        # Step 2: Create a dummy head for the merged list
20        dummy = ListNode()
21        current = dummy
22        # We start the tie-breaker counter at the length of the lists 
23        # to ensure every node gets a unique tie-breaker ID.
24        tie_breaker = len(lists)
25        
26        # Step 3: Extract the minimum node and push its next node
27        while heap:
28            val, _, node = heapq.heappop(heap)
29            
30            # Attach the popped node to the merged list
31            current.next = node
32            current = current.next
33            
34            # If there's a next node in the extracted node's list, push it to the heap
35            if node.next:
36                heapq.heappush(heap, (node.next.val, tie_breaker, node.next))
37                tie_breaker += 1
38                
39        return dummy.next