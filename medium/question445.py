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
        #reverse both linklist
        cur_l1, cur_l2 = l1, l2
        prev_l1, prev_l2 = None, None
        
        while cur_l1:
            cur_l1.next, prev_l1, cur_l1 = prev_l1, cur_l1, cur_l1.next
        
        while cur_l2:
            cur_l2.next, prev_l2, cur_l2 = prev_l2, cur_l2, cur_l2.next
        
        carry = 0
        dummy = head = ListNode(0)
        
        while prev_l2 or prev_l1 or carry:
            total = carry
            if prev_l2:
                total += prev_l2.val
                prev_l2 = prev_l2.next
            if prev_l1:
                total += prev_l1.val
                prev_l1 = prev_l1.next
            
            head.next = ListNode(total%10)
            carry = total /10
            head = head.next
        
        cur , prev = dummy.next, None
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            
        return prev