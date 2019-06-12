"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employ = {}
        #create a hashmap of id as key and importance and subordinates as values
        for employee in employees:
            employ[employee.id] = [employee.importance, employee.subordinates]
        #track of at the subordinates
        queue = []
        queue.append(id)
        total = 0
        
        while queue:
            importance, sub = employ[queue.pop()]
            total += importance
            for employee in sub:
                queue.append(employee)
                
        return total
            
        
        