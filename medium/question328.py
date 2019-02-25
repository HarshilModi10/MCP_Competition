# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        odd = head
        head1 = even = head.next
        
        while True:
            if even.next:
                odd.next = even.next
            
            else:
                odd.next = head1
                even.next = None
                return head
            
            if even.next.next:
                even.next = even.next.next
            
            else:
                odd.next = even.next
                odd = odd.next
                odd.next = head1
                even.next = None
                return head
            
            odd = odd.next
            even = even.next
        
       