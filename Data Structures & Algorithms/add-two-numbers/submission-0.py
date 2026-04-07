# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# curr.next = ListNode(digit): You take a new car and hook it to the post (or the car you are currently standing on).
#curr = curr.next: You walk onto that new car you just added. Now you are standing on the new car, ready to hook the next one to its back.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            sum = val1+val2+carry
            digit = sum%10
            carry = sum//10
            curr.next = ListNode(digit)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next        
        return dummy.next 