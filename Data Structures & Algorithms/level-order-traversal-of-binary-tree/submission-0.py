# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def level(root,lev,res):
            if root is None:
                return
                        
            if len(res)<=lev:
                res.append([])

            res[lev].append(root.val)

            #Recurse left and right ith same level
            level(root.left,lev+1,res)
            level(root.right,lev+1,res)
        
        res = []
        level(root,0,res)
        return res


        