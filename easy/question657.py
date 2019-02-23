class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        start = [0,0]
        
        for move in moves:
            if move == "U":
                start[1] += 1
            elif move == "D":
                start[1] -= 1
            elif move == "L":
                start[0] -= 1
            elif move == "R":
                start[0] += 1
            
        return start == [0,0]
        