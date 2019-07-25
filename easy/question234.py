# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        #reverse second half
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #get only the less of the half
        if fast:
            slow = slow.next
        
        prev = None
        
        while slow:
            slow.next, slow, prev = prev, slow.next, slow
        
        #you have head and prev
        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        
        return True