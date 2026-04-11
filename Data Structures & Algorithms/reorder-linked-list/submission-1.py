# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #Find the mid length of the linkedlist 
        # split and then reverse

        #Mid length
        count = 0
        current = head
        while current:
            count+=1
            current = current.next
        print(count)
        mid = math.ceil(count / 2)
        print(mid)

        #Splitting
        first_half = head
        for i in range(mid-1):
            first_half = first_half.next
        second_half = first_half.next
        first_half.next = None

        #Reverse Second half
        prev = None
        reverse_second_half = second_half
        while reverse_second_half:
            nxt = reverse_second_half.next
            reverse_second_half.next = prev
            prev = reverse_second_half
            reverse_second_half = nxt
        
        reverse_second_half = prev


        #Zipping the first_half and reverse_second_half together
        p1 = head
        p2 = reverse_second_half
        while p2:
            first_next = p1.next
            second_next = p2.next
            p1.next = p2
            p1.next.next = first_next
            p1 = first_next
            p2 = second_next
        




        