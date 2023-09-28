from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            output.extend(self.inorderTraversal(root.left))
            output.append(root.val)
            output.extend(self.inorderTraversal(root.right))
        return output
    
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        current_node = root
        while current_node or stack:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                output.append(current_node.val)
                current_node = current_node.right
        return output

solution = Solution()
answer = solution.inorderTraversal(root = [1,null,2,3])
print(answer)