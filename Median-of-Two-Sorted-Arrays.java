1class Solution {
2    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
3        // Ensure nums1 is the smaller array
4        if (nums1.length > nums2.length) {
5            return findMedianSortedArrays(nums2, nums1);
6        }
7
8        int m = nums1.length;
9        int n = nums2.length;
10        int half = (m + n + 1) / 2;
11
12        int left = 0;
13        int right = m;
14
15        while (left <= right) {
16            int i = (left + right) / 2;      // cut in nums1
17            int j = half - i;               // cut in nums2
18
19            int maxLeft1  = (i == 0) ? Integer.MIN_VALUE : nums1[i - 1];
20            int minRight1 = (i == m) ? Integer.MAX_VALUE : nums1[i];
21
22            int maxLeft2  = (j == 0) ? Integer.MIN_VALUE : nums2[j - 1];
23            int minRight2 = (j == n) ? Integer.MAX_VALUE : nums2[j];
24
25            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
26                // Correct partition found
27                if (((m + n) & 1) == 1) {
28                    return (double) Math.max(maxLeft1, maxLeft2);
29                } else {
30                    int leftMax = Math.max(maxLeft1, maxLeft2);
31                    int rightMin = Math.min(minRight1, minRight2);
32                    return (leftMax + rightMin) / 2.0;
33                }
34            } else if (maxLeft1 > minRight2) {
35                // i is too big, move left
36                right = i - 1;
37            } else {
38                // i is too small, move right
39                left = i + 1;
40            }
41        }
42
43        // Should never reach here if inputs are valid
44        throw new IllegalArgumentException("Input arrays are not valid sorted arrays.");
45    }
46
47}