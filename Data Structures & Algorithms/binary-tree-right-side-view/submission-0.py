# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS left ot right
        # Fetch the last elem

        def level(root,lev,res):
            if root is None:
                return
            
            if len(res)<=lev:
                res.append([])
            
            res[lev].append(root.val)

            level(root.left,lev+1,res)
            level(root.right,lev+1,res)
        
        res = []
        level(root,0,res)
        print(res)
        final_res = []
        for i in res:
            final_res.append(i[-1])
        print(final_res)
        return final_res


        