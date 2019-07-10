class FreqStack(object):

    def __init__(self):
        self.frequency = collections.defaultdict(int)
        self.group = collections.defaultdict(list)
        self.max_frequency = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        feq = self.frequency[x] + 1
        self.frequency[x] += 1
        if feq > self.max_frequency:
            self.max_frequency = feq
        self.group[feq].append(x)
        
        
        

    def pop(self):
        """/
        :rtype: int
        """
        val = self.group[self.max_frequency].pop()
        self.frequency[val] -= 1
        if not self.group[self.max_frequency]:
            self.max_frequency -= 1
            
        return val
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()