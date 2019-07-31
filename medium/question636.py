class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        output = [0 for _ in range(n)]
        last_time = 0
        last_id = []
        
        for log in logs:
            e_id, execution, time  = log.split(":")
            
            if execution == "start" and last_id:
                l_id = last_id.pop()
                output[l_id] += int(time) - last_time
                last_time = int(time)
                last_id.append(l_id)
                last_id.append(int(e_id))
            
            elif execution == "end":
                output[last_id.pop()] += int(time) - last_time + 1
                last_time = int(time) + 1
            else:
                last_time = int(time)
                last_id.append(int(e_id))
                
        return output
            
        