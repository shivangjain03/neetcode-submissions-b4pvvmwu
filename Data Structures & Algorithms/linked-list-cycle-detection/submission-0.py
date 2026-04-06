# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Traverse the linkedlist
        # Create a hashmap add the node to the hashmap    
        visited = {}
        linked = head
        while linked not in visited and linked!= None:
            visited[linked] = True
            linked = linked.next
        if linked == None:
            return False
        else:
            return True


        