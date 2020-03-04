class Employee:
    # raise_amount is a class variable
    raise_amount = 1.04

    num_of_emps = 0

    # self is called instance argument, the other three are attribute argument
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@emory.edu'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # you can't only type raise_amount, a class variable can only be accessed from a class
        # or from a class instance. Now if a instance has a attribute called raise_amount, this function
        # would use it, if not then it will use the class variable raise_amount
        # if we change it to Employee.raise_amount, then it always uses the class variable
        self.pay = int(self.pay * self.raise_amount)

    # the function created after this decorator will be a class function and automatically takes
    # a class (cls) argument as the first argument
    @classmethod
    def set_raise_amout(cls, amount):
        cls.raise_amount = amount

    @classmethod
    # use classmethod as alternative constructor that take in hyphen seperated values
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    # if the method has some logical connection with the class but does not access instances or
    # the class anywhere within the method, then it should be a staticmethod
    # instance methods take self as first argument by default, class methods take cls as first argument
    # by default, static methods take nothing by default
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# we can manually set instance attributes without being explicit in the class blueprint
# emp_1.first = 'Evan'
# emp_1.last = 'Zhao'
# emp_1.email = 'nzhao9@emory.edu'
# emp_1.pay = 50000
print('The num_of_emps now is:')
print(Employee.num_of_emps)
print()

emp_1 = Employee('Evan','Zhao',50000)
emp_2 = Employee('Clara','Liu',400)

print('The num_of_emps now is:')
print(Employee.num_of_emps)
print()

print('access class attributes')
print(emp_1.email)
print(emp_2.email)
print()

print("Two ways to call a class function")
# since fullname is a function instead of a attribute, we need to put () after it
# 虽然emp_1不在fullname的括号里 但是emp_1其实是被作为一个instance argument passed in to fullname function
print(emp_1.fullname())
# this does the exact same thing as the line above, here we call the full name function from its class
# and pass emp_1 as the instance argument
print(Employee.fullname(emp_1))
print()


print("access class variable from class and from class instance have the same effect")
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# to understand this with further detail: when we are trying to access an attribute on an instance,
# python will first check if that instance contains that attribute, if the instance doesn't, then
# python will check if the class or any class that it inherits from contains that attribute

#to get a better idea of what's going on, we can see that emp_1 instance doesn't contain the
# raise amount attribute. It is the class that it belongs to, Employee, that contains it.
print('emp_1 instance namespace:')
print(emp_1.__dict__)

print('Employee class namespace:')
print(Employee.__dict__)
print()

# this would change the class variable raise_amount from 1.04 to 1.05
Employee.raise_amount=1.05

# this will not affect the value of the class variable raise_amount, instead it will create a instance
# attribute called raise_amount for emp_1
emp_1.raise_amount=1.06

# these two have the same effect
Employee.set_raise_amout(1.07)
emp_1.set_raise_amout(1.07)

# calling class method as alternative constructor method
emp_str_1 = 'Evan-Zhao-50000'
new_emp_1 = Employee.from_string(emp_str_1)

# calling static method is_workday
print('calling static method is_workday')
import datetime
my_date = datetime.date(2020,2,21)
print(Employee.is_workday(my_date))
print()


# Class inheritance

class Developer(Employee):
    # changing the raise_amount attribute explicitly will overwrite the raise_amount inherited
    # of course, the raise_amount for the Employee class will not change by this
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # we don't have to copy and paste the every from the Employee class constructor
        # this one line is equivalent to copy paste all of it and its more maintainable
        # Employee.__init__(self,first,last,pay) also works but a bit less maintainable
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


    pass

# Developer class inherits everything from the Employee class
dev_1 = Developer('Evan','Zhao',50000, 'Python')
dev_2 = Developer('Clara','Liu',400,'Java')

# As we can see from below, Developer class contains nothing itself
# the reason why dev_1.email works is that python follows the method resolution order and find
# the constructor, instance attributes and everything from the Employee class that the Developer
# class inherits from
print(dev_1.email)
print(dev_2.email)
print()

print('Developer class namespace:')
print(Developer.__dict__)
print()
print('help(Developer):')
help(Developer)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # you never want to pass mutable data types, like lists or dicts as default arguments
        if employees is None:
            self.employees= []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


mgr_1 = Manager('Sue','Smith',90000,[dev_1])
print(mgr_1.email)
print(dev_2.fullname())
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# mgr_1 is of course an instance of the Manager class
print(isinstance(mgr_1,Manager))

# it is also an instance of the Employee class since the Manager class inherits from it
print(isinstance(mgr_1,Employee))

# however, it's not an instance of the Developer class
print(isinstance(mgr_1,Developer))

# Manager is a subclass of Employee
print(issubclass(Manager,Employee))
