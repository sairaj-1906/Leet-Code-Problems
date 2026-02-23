1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode removeNthFromEnd(ListNode head, int n) {
13        // Create a dummy node to handle edge cases (like removing the head)
14        ListNode dummy = new ListNode(0);
15        dummy.next = head;
16
17        ListNode slow = dummy;
18        ListNode fast = dummy;
19        // Move fast pointer n + 1 steps ahead
20        for (int i = 0; i <= n; i++){
21            fast = fast.next;
22        }
23        // Move both pointers simultaneously until fast goes out of bounds
24        while (fast != null){
25            slow = slow.next;
26            fast = fast.next;
27        }
28        // Remove the target node by skipping it
29        slow.next = slow.next.next;
30
31        // Return the actual head
32        return dummy.next;
33    }
34}