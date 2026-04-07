# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        first_half = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        #Reverse second_half

        prev = None
        reverse_second_half = second_half

        while reverse_second_half:
            nxt = reverse_second_half.next
            reverse_second_half.next = prev
            prev = reverse_second_half
            reverse_second_half = nxt
        #Prev is the head of reverse second_half
        #Merge the first and second half alternatingly

        first = head
        second = prev

        while second:
            first_p = first.next
            second_p = second.next
            first.next = second
            second.next = first_p
            first = first_p
            second = second_p

            



        