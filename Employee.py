class Employee:
    def __init__(self, name="hi", salary=0, totalHour=0.00, totalSalary=0, meal=0, payment=0, next_employee = None, pre_employee = None):
        self.name = name
        self.salary = salary
        self.totalHour = totalHour
        self.totalSalary = totalSalary
        self.meal = meal
        self.payment = payment
        self.next_employee = next_employee
        self.pre_employee = pre_employee
    
    def __str__(self):
        return self.name +'\t'+str(self.salary)+'\t'+str(self.totalHour)+'\t'+str(self.totalSalary)+'\t'+str(self.meal)+'\t'+str(self.payment)
    
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary
    
    def setSalary(self, newSalary):
        return newSalary
    
    def getWorkTime(self):
        return self.totalHour
    
    def setWorkTime(self, hour):
        self.totalHour = self.totalHour + float(hour)
        return self.totalHour
    
    def getMeal(self):
        return self.meal
    
    def setMeal(self,m):
        self.meal = self.meal + m
        return self.meal
    
    def getPayment(self):
        return self.payment
    

