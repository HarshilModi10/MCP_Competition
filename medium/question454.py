class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        first_set = {}
        second_set = {}
        
        for i in range(len(A)):
            for j in range(len(B)):
                first_sum = A[i] + B[j]
                second_sum = C[i] + D[j]
                
                if first_sum in first_set:
                    first_set[first_sum] += 1
                else:
                    first_set[first_sum] = 1
                
                if second_sum in second_set:
                    second_set[second_sum] += 1
                else:
                    second_set[second_sum] = 1
        
        total = 0
        
        for val, count in first_set.items():
            if -1* val in second_set:
                total = total + count * second_set[-1* val]
        return total
    
        
        