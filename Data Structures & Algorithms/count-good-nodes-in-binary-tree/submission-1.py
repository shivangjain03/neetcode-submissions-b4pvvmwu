# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def check(root,res,maxi):
            if not root:
                return
            if root.val>=maxi:
                res.append(root.val)
                maxi = root.val
            check(root.left,res,maxi)
            check(root.right,res,maxi)
        
        res = []
        maxi = -100
        check(root,res,maxi)
        print(res)
        return len(res)
        

        