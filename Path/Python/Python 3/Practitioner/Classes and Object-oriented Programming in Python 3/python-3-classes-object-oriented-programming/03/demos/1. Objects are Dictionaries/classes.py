# class Employee:
#     pass

# e = Employee()
# print(e)
# print(e.__dict__)



# class Employee:
#     def __init__(self):
#         self.__dict__["name"] = "Ji-Soo"
#         self.__dict__["age"] = 38
#         self.__dict__["position"] = "developer"
#         self.__dict__["salary"] = 1200

# e = Employee()
# print(e.__dict__)


class Employee:
    def __init__(self):
        self.name = "Ji-Soo"
        self.age = 38
        self.position = "developer"
        self.salary = 1200


e = Employee()
# print(e.name)
print(e.__class__)
