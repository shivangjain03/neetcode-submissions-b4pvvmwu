# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Using DFS and storing the max_value and updating if find a greater value
        # if node.val>max add to list
        def prep(root,res,current_max):
            if root:
                if root.val>=current_max:
                    res.append(root.val)
                    current_max = root.val
                prep(root.left, res,current_max )
                prep(root.right, res, current_max)
        
        res = []
        max_value = -100
        prep(root,res, max_value)
        return len(res)
                

        
        