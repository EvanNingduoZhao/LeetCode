"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""



# 很简单的一道dfs题 说实话应该属于是easy难度的 
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeeMap = {}
        target = employees[0]
        for employee in employees:
            employeeMap[employee.id] = employee
            if employee.id == id:
                target = employee
        totalValue = 0
        stack = [target]
        while stack:
            employee = stack.pop()
            totalValue += employee.importance
            for sub in employee.subordinates:
                stack.append(employeeMap[sub])
        return totalValue