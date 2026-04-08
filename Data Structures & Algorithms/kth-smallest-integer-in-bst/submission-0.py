# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Do inorder DFS and save all the nodes val in the list then sort them and find using the using
        #Performe DFS
        def helper(root,res):
            if root:
                helper(root.left,res)
                res.append(root.val)

                
                helper(root.right,res)
            
        res = []
        helper(root,res)
        return res[k-1]
        