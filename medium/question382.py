# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.array = []
        node = head
        while node:
            self.array.append(node.val)
            node = node.next
            
            
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        
        return self.array[random.randint(0,len(self.array)-1)]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()