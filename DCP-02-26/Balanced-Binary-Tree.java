1/**
2 * Definition for a binary tree node.
3 * public class TreeNode {
4 *     int val;
5 *     TreeNode left;
6 *     TreeNode right;
7 *     TreeNode() {}
8 *     TreeNode(int val) { this.val = val; }
9 *     TreeNode(int val, TreeNode left, TreeNode right) {
10 *         this.val = val;
11 *         this.left = left;
12 *         this.right = right;
13 *     }
14 * }
15 */
16class Solution {
17    public boolean isBalanced(TreeNode root) {
18        return dfs(root) != -1;
19    }
20    // Returns the height of the tree if balanced, or -1 if unbalanced
21    private int dfs(TreeNode node){
22        if (node == null){
23            return 0;
24        }
25        // Check left subtree
26        int leftHeight = dfs(node.left);
27        if (leftHeight == -1) return -1;
28
29        // Check right subtree
30        int rightHeight = dfs(node.right);
31        if (rightHeight == -1) return -1;
32
33        // Check for imbalance
34        if (Math.abs(leftHeight - rightHeight) > 1){
35            return -1;
36        }
37        //Return height
38        return Math.max(leftHeight, rightHeight) + 1;
39    }
40}