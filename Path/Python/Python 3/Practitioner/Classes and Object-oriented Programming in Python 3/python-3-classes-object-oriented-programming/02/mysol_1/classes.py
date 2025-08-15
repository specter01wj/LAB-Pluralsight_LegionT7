# employee1_name = "Ji-Soo"
# employee1_age = 38
# employee1_position = "developer"
# employee1_salary = 1200

# employee2_name = "Lauren"
# employee2_age = 44
# employee2_position = "tester"
# employee2_salary = 1000


# employee1 = ["Ji-Soo", 38, "developer", 1200]
# employee2 = ["Lauren", 44, "tester", 1000]


employee1 = {
    "name": "Ji-Soo",
    "age": 38,
    "position": "developer",
    "salary": 1200
}
employee2 = {
    "name": "Lauren",
    "age": 44,
    "position": "tester",
    "salary": 1000
}


def init_employee(name, age, position, salary):
    return {
        "name": name,
        "age": age,
        "position": position,
        "salary": salary
    }


employee3 = init_employee("Mateo", 38, "developer", 200)


def increase_salary(employee, percent):
    employee['salary'] += employee['salary'] * (percent/100)


def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}")


employees = [employee1, employee2]
increase_salary(employee2, 20)
for e in employees:
    employee_info(e)
    # print(f"{e[0]}s' salary is ${e[3]}")
    # print(f"{e['name']} salary is ${e['salary']}")
