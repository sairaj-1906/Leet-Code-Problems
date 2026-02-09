1import java.util.ArrayList;
2import java.util.List;
3
4// Definition for a binary tree node.
5class TreeNode {
6    int val;
7    TreeNode left;
8    TreeNode right;
9    
10    TreeNode() {}
11    TreeNode(int val) { this.val = val; }
12    TreeNode(int val, TreeNode left, TreeNode right) {
13        this.val = val;
14        this.left = left;
15        this.right = right;
16    }
17}
18
19class Solution {
20    // List to store nodes in sorted order
21    private List<TreeNode> sortedNodes = new ArrayList<>();
22
23    public TreeNode balanceBST(TreeNode root) {
24        // Step 1: Traverse the tree to get nodes in sorted order
25        inOrderTraversal(root);
26        
27        // Step 2: Reconstruct the tree from the sorted list
28        return createBalancedBST(0, sortedNodes.size() - 1);
29    }
30
31    // Helper method for In-Order Traversal (Left -> Root -> Right)
32    private void inOrderTraversal(TreeNode node) {
33        if (node == null) return;
34        
35        inOrderTraversal(node.left);
36        sortedNodes.add(node);
37        inOrderTraversal(node.right);
38    }
39
40    // Helper method to build a balanced BST from a sorted list
41    private TreeNode createBalancedBST(int start, int end) {
42        // Base case: if start index exceeds end index, sub-list is empty
43        if (start > end) return null;
44
45        // Find the middle element to be the root
46        int mid = start + (end - start) / 2;
47        TreeNode root = sortedNodes.get(mid);
48
49        // Recursively build the left subtree using the left half of the list
50        root.left = createBalancedBST(start, mid - 1);
51
52        // Recursively build the right subtree using the right half of the list
53        root.right = createBalancedBST(mid + 1, end);
54
55        return root;
56    }
57}