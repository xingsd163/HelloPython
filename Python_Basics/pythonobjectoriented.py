# Python Object Oriented Programming

class Employee:
    empCount=0

# constructor, self, attributes
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Nathan",1500)
emp2 = Employee("Joey", 2000)

emp1.displayCount()
emp1.displayEmployee()

emp2.displayCount()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)

emp1.age=20
print(emp1.age)

age=getattr(emp1,'age')
print(age)


# exception handling, try except else finally

try:
    age2=getattr(emp2,'age')
    print(age2)
except AttributeError:
    print("No this attribute")
finally:
    print("exit..")


# internal class attributes,
# __dict__
# __name__, __module__

print("====CLass Metadata===")

print("The name of this class: ", Employee.__name__)
print("The doc of this class: ", Employee.__doc__)
print("The attributes of this class: ", Employee.__dict__)