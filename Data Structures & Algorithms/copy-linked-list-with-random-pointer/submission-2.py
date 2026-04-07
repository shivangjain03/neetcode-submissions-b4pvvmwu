"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Clone and insert
        if not head:
            return None
        
        curr = head
        while curr:
            #Saving next nopde
            nxt = curr.next
            #Create a new node 
            copy = Node(curr.val)
            copy.next = nxt
            curr.next = copy
            curr = nxt

        curr = head
        #Point A'->Random of A.next(which is cloned node)
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        
        #Unzip
        curr = head
        copy_head = curr.next
        while curr:
            #Fixing A-B not A->A'
            clone = curr.next 
            curr.next = clone.next 

            #Fixing A'->B' not A'->B 
            if curr.next:
                clone.next = curr.next.next
            else:
                clone.next = None

            curr = curr.next
        return copy_head
        
        


        