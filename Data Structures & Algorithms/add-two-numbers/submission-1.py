# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or carry != 0:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            sum = l1_val+l2_val+carry

            digit = sum%10
            carry = sum//10
            
            new_node = ListNode(digit)

            current.next = new_node

            current = current.next
            
            
        
        return dummy.next



        