# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        li = ListNode()
        dummy_list = li

        while list1!= None and list2!=None:
            if list1.val<list2.val:
                dummy_list.next = list1
                #remove the val node from list1
                list1 = list1.next
            else:
                #remove the val node from list2
                dummy_list.next = list2
                list2 = list2.next
            dummy_list = dummy_list.next
        
        dummy_list.next = list1 if list1 else list2

        return li.next
        

            
        