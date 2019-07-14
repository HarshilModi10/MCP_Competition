# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
                return None
            
        runner_A, runner_B = headA, headB
        runner_A_end, runner_B_end = False, False
        
        while True:
            if not runner_A and not runner_A_end:
                runner_A = headB
                runner_A_end = True
            if not runner_B and not runner_B_end:
                runner_B = headA
                runner_B_end = True
                
            if not runner_A or not runner_B:
                return None
            
            if runner_A == runner_B:
                return runner_A
            
            runner_A = runner_A.next
            runner_B = runner_B.next
            