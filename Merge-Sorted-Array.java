1class Solution {
2    public void merge(int[] nums1, int m, int[] nums2, int n) {
3        // Inotialize 3 pointers
4        int p1 = m - 1;         // Points to the last actual element in nums1
5        int p2 = n - 1;         // Points to the last element in nums2
6        int p = m + n - 1;      // Points to the last available position in nums1
7
8        // Traverse and compare from the back
9        while (p1 >= 0 && p2 >= 0){
10            if (nums1[p1] > nums2[p2]){
11                nums1[p] = nums1[p1];
12                p1--;
13            } else {
14                nums1[p] = nums2[p2];
15                p2--;
16            }
17            p--;
18        }
19        // If there are leftover elements in nums2, copy them over
20        // If there ane leftover elements in nums1, we dont'n need to do anything
21        // because they are already in their correct sorted positions at the front
22        while (p2 >= 0) {
23            nums1[p] = nums2[p2];
24            p2--;
25            p--;
26        }
27    }
28}