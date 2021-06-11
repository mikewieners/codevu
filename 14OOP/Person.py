import datetime

class Person:
    last_name = None
    first_name = None
    date_of_birth = None

    def age(self):
        return (datetime.date.today() - self.date_of_birth).days/365.25 if self.date_of_birth else None

new_person = Person()
type(new_person)

class Employee(Person):
    hire_date = None
    hourly_pay_rate = None

    def calculate_paycheck(self, hours_this_pay_period):
        return hours_this_pay_period * self.hourly_pay_rate

new_employee = Employee()
type(new_employee)

class Person2:
    def __init__(self, last_name, first_name, date_of_birth):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth

new_person2 = Person2('Person', 'Kelly', '2021-06-10', '111-11-1111')
type(new_person2)