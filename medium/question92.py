# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        
        dummy = dummyNode = ListNode(0)
        dummy.next = head
        
        for i in range(m-1):
            dummy = dummy.next
        prev = None
        current = dummy.next
                
        for i in range(n-m + 1):
            n = current.next
            current.next = prev
            prev = current
            current = n
        if m !=0:
            dummy.next.next = current
            dummy.next = prev
        else:
            dummy.next = current
        
        return dummyNode.next
        
            
        
            
        