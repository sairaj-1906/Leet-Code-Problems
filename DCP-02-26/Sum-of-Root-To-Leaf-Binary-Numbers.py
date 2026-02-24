1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9        self.total = 0
10
11        def dfs(node: TreeNode, cur: int) -> None:
12            if not node:
13                return
14            cur = (cur << 1) | node.val
15            if not node.left and not node.right:
16                self.total += cur
17                return
18            dfs(node.left, cur)
19            dfs(node.right, cur)
20        
21        dfs(root, 0)
22        return self.total