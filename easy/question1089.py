class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return arr
        length = 0
        count_zero = 0
        one = False
        
        for num in arr:
            if num == 0:
                count_zero += 1
                length += 1
            length += 1
            
            if length >= len(arr):
                if length > len(arr):
                    one = True
                    count_zero -= 1
                break
            
                
        
        write_index = len(arr) - 1
        read_index = write_index - count_zero
        
        while read_index >= 0:
            if arr[read_index] == 0:
                arr[write_index] = 0
                if write_index != 0 and not one:
                    arr[write_index - 1] = 0
                    write_index -= 1                    
                one = False
                
            else:
                arr[write_index] = arr[read_index]
            
            write_index -= 1
            read_index -= 1