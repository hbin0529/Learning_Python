class Employee:

    def __init__(self, name, age, salary):
        print(id(self))

e = Employee("John", 30, 2800)
a = Employee("Tom", 29, 2900)
print('e =', id(e))
print('a =', id(a))