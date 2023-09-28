from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Inorder Traversal - Left node, Root node, Right node

    Recursive Solution:
    Check if root node is not null
    If there is left node, add to list
    Add root node to list
    If there is right node, add to list
    return list
    '''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            output.extend(self.inorderTraversal(root.left))
            output.append(root.val)
            output.extend(self.inorderTraversal(root.right))
        return output
    
    '''
    Iterative Soltion

    Initialize stack and output list
    Create a pointer to traverse the tree
    While both the pointer is not null and stack is not empty
        Check if pointer is not null:
            Add the node to the stack
            point pointer to left node
        If pointer is null:
            Pop from the stack then point the pointer to that node
            Add the value of the node to the output list
            point pointer to the right node
    '''
    
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

