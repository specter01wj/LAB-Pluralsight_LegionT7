class Employee:
    """Base class representing an employee."""
    def __init__(self, fname, lname):
        self.fname = fname.strip().title()
        self.lname = lname.strip().title()

    def __str__(self):
        return f"{self.fname} {self.lname}"

class SalaryEmployee(Employee):
    """Represents a salaried employee with fixed annual salary."""
    WEEKS_PER_YEAR = 52  # Defined as a class constant

    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = max(0, salary)  # Ensures salary is non-negative
    
    def calculate_paycheck(self):
        """Calculate weekly paycheck based on salary."""
        return self.salary / self.WEEKS_PER_YEAR
    
    def __str__(self):
        return f"{super().__str__()} - Salary: ${self.salary:.2f}"

class HourlyEmployee(Employee):
    """Represents an hourly employee with a wage and weekly hours."""
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = max(0, weekly_hours)  # Prevents negative hours
        self.hourly_rate = max(0, hourly_rate)  # Prevents negative rate

    def calculate_paycheck(self):
        """Calculate weekly paycheck based on hours worked."""
        return self.weekly_hours * self.hourly_rate
    
    def __str__(self):
        return f"{super().__str__()} - Hourly: ${self.hourly_rate:.2f}/hr, Weekly Hours: {self.weekly_hours}"

class CommissionEmployee(SalaryEmployee):
    """Represents a salaried employee who also earns commission."""
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = max(0, sales_num)
        self.com_rate = max(0, com_rate)

    def calculate_paycheck(self):
        """Calculate weekly paycheck with base salary + commission earnings."""
        base_pay = super().calculate_paycheck()
        commission = self.sales_num * self.com_rate
        return base_pay + commission

    def __str__(self):
        return f"{super().__str__()} - Sales: {self.sales_num}, Commission Rate: ${self.com_rate:.2f}/sale"

