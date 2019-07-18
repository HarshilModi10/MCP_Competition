# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current, prev = head, None
        
        while current:
            if current.val == val:
                if not prev:
                    current = current.next
                    head = head.next
                else:
                    prev.next = current.next
                    current = prev.next
            else:
                prev, current = current, current.next
        
        return head
                
        