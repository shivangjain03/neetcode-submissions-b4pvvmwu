# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        curr = head
        dummy = ListNode(0, head)
        while curr:
            len+=1
            curr = curr.next
        print(len)

        index_to_remove = len-n

        sec = dummy

        for i in range(index_to_remove):
            sec = sec.next
        
        if sec.next:
            sec.next = sec.next.next


        return dummy.next