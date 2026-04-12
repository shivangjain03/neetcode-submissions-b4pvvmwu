# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root,level,res):
            if root is None:
                return
            if len(res)<=level:
                res.append([])
            res[level].append(root.val)

            bfs(root.left, level+1, res)
            bfs(root.right, level+1, res)
        
        res = []
        result = []
        bfs(root,0,res)
        print(res)
        for i in res:
            print(i)
            result.append(i[-1])
        return result
        