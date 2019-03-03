# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        faster = head.next
        
        while head and faster and faster.next:
            
            if head == faster:
                return True
            
            head = head.next
            faster = faster.next.next
        
        return False
        