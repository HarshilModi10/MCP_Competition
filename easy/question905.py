class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        
        for num in A:
            if num %2 == 0:
                res.insert(0,num)
            else:
                res.append(num)
        
        return res

#better Solution
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        front = 0
        end = len(A)-1
        
        while front < end:
            if A[front] %2 == 0:
                front += 1
            elif A[end] %2 == 1:
                end -= 1
            elif A[front] %2 == 1 and A[end] %2 == 0:
                A[front], A[end] = A[end], A[front]
                front += 1
                end -= 1
        
        return A
        