import Employee

class EmployeeList:
    def __init__(self, employee_list=None):
        self.head = None
        self.tail = None
        if employee_list is not None:
            self.addMultipleEmployees(employee_list)
    
    def __str__(self):
        return '\n -> '.join([str(node) for node in self])
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_employee
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_employee
        return count
    
    def getHead(self):
        return self.head

    def addEmployee(self, name, salary, totalHour, totalSalary, meal, payment):
        if self.head is None:
            self.tail = self.head = Employee.Employee(name, salary, totalHour, totalSalary, meal, payment)
        else:
            self.tail.next_employee = Employee.Employee(name, salary, totalHour, totalSalary, meal, payment)
            self.tail = self.tail.next_employee
            return self.tail
        
    def addMultipleEmployees(self,employeelist):
        for each in employeelist:
            each = employeelist[each]
            self.addEmployee(each['name'],each['salary'],each['totalHour'],each['totalSalary'], each['meal'], each['payment'])
