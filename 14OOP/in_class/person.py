from datetime import date

class Person:
    last_name = None
    first_name = None
    height_in_inches = None
    date_of_birth = None
    address = None

    def calculate_age(self):
        return (date.today() - self.date_of_birth).days/365.25 if self.date_of_birth else None

    def get_formatted_name(self):
        return self.first_name + ' ' + self.last_name

my_person = Person()
type(my_person)

class Employee(Person):
    social_security_number = None
    department = None
    employee_id = None
    title = None
    manager = None
    hourly_pay_rate = None

    def calculate_paycheck(self, hours):
        return self.hourly_pay_rate * hours

print()