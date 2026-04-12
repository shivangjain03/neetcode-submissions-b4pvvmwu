# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Preorder->Current->left->right
        #Inorder->Left->Current->Right
        if len(preorder) == 0 or len(inorder) ==  0:
            return None
        
        root = TreeNode(preorder[0])

        root_elem = preorder[0]
        root_index_inorder = inorder.index(root_elem)
        print(root_index_inorder)
        first_half_inorder = inorder[:root_index_inorder]
        second_half_inorder = inorder[root_index_inorder+1:]

        root.left = self.buildTree(preorder[1 : 1 + root_index_inorder], first_half_inorder)
        root.right = self.buildTree(preorder[1 + root_index_inorder : ], second_half_inorder)


        return root


        