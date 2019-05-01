#reverse a linklist iteratively
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        previous = None
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            
        return previous

#reverse a linkedlist using recursion 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        return self.reverse(head)
    
    def reverse(self,root,prev = None):
        if not root:
            return prev
        
        n = root.next
        root.next = prev
        return self.reverse(n,root)
        


        
        
        