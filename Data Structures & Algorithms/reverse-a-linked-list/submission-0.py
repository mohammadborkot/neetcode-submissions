# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next


        new_list = ListNode()
        begin = new_list
        for i in range(len(nodes)-1, -1, -1):
            new_list.val = nodes[i].val
            if i != 0:
                new_list.next = ListNode()
            new_list = new_list.next

        return begin

        
        