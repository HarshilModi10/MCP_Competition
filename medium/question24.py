# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        new_head = curr = head.next
        prev = head
        last = None
        
        while curr and prev:
            temp = curr.next
            if temp and temp.next:
                prev.next = temp.next
            else:
                prev.next = temp
            
            curr.next = prev
            prev = temp
            if prev:
                curr = prev.next
        
        return new_head