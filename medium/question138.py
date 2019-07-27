"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        bijection_list = {}
        
        current = head
        prev = dummy = Node(0,None,None)
        
        while current:
            node = Node(current.val, None, None)
            prev.next = node
            bijection_list[current] = node
            
            current = current.next
            prev = prev.next
        
        current, new = head, dummy.next
        
        while current:
            if current.random:
                new.random = bijection_list[current.random]
            current = current.next
            new = new.next
        
        return dummy.next
            
        
        
        