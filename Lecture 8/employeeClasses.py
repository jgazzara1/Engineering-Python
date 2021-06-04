class Employee:

    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

    def printSalary(self):
        print self.salary

    def raiseSalary(self, bonus):
        self.salary = self.salary + bonus

E1 = Employee('Bob', 8000)
E2 = Employee('Mary', 9000)
E3 = Employee('Joe', 4000)

List = [E1, E2, E3]

for emp in List:
    emp.printSalary()

for item in List:
    item.raiseSalary(1000)

for item in List:
    item.printSalary()
