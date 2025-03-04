class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)


class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")


class Developer(Employee):
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000)

print(isinstance(employee1, Tester))
print(isinstance(employee1, Employee))

print(issubclass(Developer, Employee))
print(issubclass(Employee, object))
print(issubclass(Developer, object))

try:
    # something that raises the FloatingPointError or the ZeroDivisionError
    raise FloatingPointError("Watch out, a floating point error!")
except ArithmeticError as e:
    # handle this error
    print(e)
