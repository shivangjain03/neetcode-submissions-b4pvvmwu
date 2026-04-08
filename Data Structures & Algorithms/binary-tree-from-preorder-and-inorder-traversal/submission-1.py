# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder = root->left->right 
        #Inorder =  left->root-.right
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root_index = inorder.index(root_val)
        inorder_left = inorder[:root_index]
        inorder_right = inorder[(root_index+1):]
        len_left = len(inorder_left)
        len_right = len(inorder_right)
        preorder_left = preorder[1:(1+len_left)]
        preorder_right = preorder[(1+len_left):]

        root = TreeNode(root_val)

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right,inorder_right)

        return root

