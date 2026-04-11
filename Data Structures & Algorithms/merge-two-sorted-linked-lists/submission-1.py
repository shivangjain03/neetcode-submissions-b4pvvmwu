# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val>=l2.val:
                res.next = l2
                l2 = l2.next
            elif l2.val>l1.val:
                res.next = l1
                l1 = l1.next
            res = res.next
        if l1:
            res.next = l1
        elif l2:
            res.next  = l2
        return head.next
            

        