from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    """Represents a company that manages employees and payroll."""
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        """Adds an employee to the company."""
        if isinstance(new_employee, Employee):  # Ensure it's an Employee object
            self.employees.append(new_employee)
        else:
            print("Error: Invalid employee type. Must be an Employee instance.")

    def display_employees(self):
        """Displays the list of employees in the company."""
        print("\n📋 Current Employees:")
        if not self.employees:
            print("No employees added yet.")
        else:
            for employee in self.employees:
                print(employee)  # Uses __str__ from Employee class
        print("-" * 30)

    def pay_employees(self):
        """Calculates and displays payroll for all employees."""
        print("\n💰 Paying Employees:")
        if not self.employees:
            print("No employees to pay.")
        else:
            for employee in self.employees:
                print(f"📄 Paycheck for: {employee}")
                print(f"💵 Amount: ${employee.calculate_paycheck():,.2f}")
                print("-" * 30)

def main():
    """Main function to create a company and manage employees."""
    my_company = Company()

    # Create and add employees
    employees = [
        SalaryEmployee("Sarah", "Hess", 50000),
        HourlyEmployee("Lee", "Smith", 25, 50),
        CommissionEmployee("Bob", "Brown", 30000, 5, 200),
    ]

    for emp in employees:
        my_company.add_employee(emp)

    # Display and pay employees
    my_company.display_employees()
    my_company.pay_employees()

if __name__ == "__main__":
    main()
