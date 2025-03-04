from employee import Employee
from project import Project


p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)
