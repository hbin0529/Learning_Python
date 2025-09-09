# 생성자 개념

class Employee:
    def __init__(self, name, salary):
        print("initialization of constructor")
        self.name = name
        self.salary = salary

e1 = Employee("John", 2500)
print(e1)
print(e1.name, e1.salary)

e2 = Employee("Tom", 3100)
print(e2)
print(e2.name, e2.salary)

