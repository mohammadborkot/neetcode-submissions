# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        n1 = None
        i = head

        while i:
            temp = i.next
            i.next = n1
            n1 = i
            i = temp
            
        return n1




        
        