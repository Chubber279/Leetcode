from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.isMirror(root.left, root.right)
        
        
    def isMirror(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        queue = [root, root]

        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            print(left.val, right.val)
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True