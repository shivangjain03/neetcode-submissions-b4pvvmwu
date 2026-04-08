# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Do inorder traversal left->current->right
        #BST has no repeated val
        def helper(root,res):
            if root:
                helper(root.left,res)
                res.append(root.val)
                helper(root.right,res)
        res = []
        helper(root,res)
        current_max = -1000
        for i in res:
            if i>current_max:
                current_max = i
            else:
                return False
        return True
                