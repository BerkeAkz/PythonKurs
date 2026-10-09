# Aggregation (toplulaştırma) 

class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id

class Department:
    def __init__(self,name_dp,):
        self.name_dp=name_dp
        self.employees=[] #aggregation

    def add_employees(self,emp):
        self.employees.append(emp)

    def printEmpoyees(self):

        for item in self.employees:
            print(f"Employee:{item.name} İD:{item.emp_id}")



e1=Employee("Berke Akgöz",10)
e2=Employee("Alper Akgöz", 7)

dep=Department("Computer")

dep.add_employees(e1)
dep.add_employees(e2)

dep.printEmpoyees()
