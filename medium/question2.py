# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        temp = l1  
        prev = None
        
        
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total/10
            l1.val = total%10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
               
        if not prev.next and l2:
            prev.next = l2

        while carry:
            if prev.next:
                total = prev.next.val + carry
                prev.next.val = total %10
                carry = total/10
            else:
                prev.next = ListNode(carry)
                carry = 0
                
            prev = prev.next
        return temp
    
                
            
            