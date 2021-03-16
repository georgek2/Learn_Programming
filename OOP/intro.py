import random

class Employee:

    def __init__(self, first, last, department, salary):
        self.first = first
        self.last = last
        self.department = department
        self.salary = salary

    def fullname(self):

        return f"{self.first} {self.last} in {self.department} department"


    def userid(self):
        part1 = random.choice(self.first)
        part2 = random.choice(self.last)
        n_1 = random.randint(0, 11)
        n_2 = random.randint(0, 11) 

        result = f"User_ID: {part1}{n_1}{part2}{n_2}\nPay: {self.salary}"

        return result

    def info(self):

        # obj = {
        #     'fullname': self.fullname(),
        #     'id': self.userid()
        # }
        # items = [v for v in obj.values()]
        items = f"{self.fullname()}\n{self.userid()}"
        
        return items

emp_1 = Employee('George', 'Kamuruu', 'Production', 10000)
emp_2 = Employee('Luke', 'Hobbs', 'HR', 34000)

# print(emp_2.fullname())
# print(emp_2.userid())

print(emp_1.info())
