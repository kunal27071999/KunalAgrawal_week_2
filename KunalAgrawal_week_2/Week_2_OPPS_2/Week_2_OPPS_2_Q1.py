"""
1. Write note on inheretance

"""

"""
Inheritance is the capability of one class to derive or inherit the properties from another class.
The benefits of inheritance are: 


It represents real-world relationships well.
It provides reusability of a code. We don’t have to write the same code again and again.
Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, 
then all the subclasses of B would automatically inherit from class A.
Below is a simple example of inheritance in Python 



# A Python program to demonstrate inheritance 

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"
class Person(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
Output: 
Geek1 False
Geek2 True



What is object class? 
Like Java Object class, in Python (from version 3.x), object is root of all classes. 
In Python 3.x, “class Test(object)” and “class Test” are same. 
In Python 2.x, “class Test(object)” creates a class with object as parent
(called new style class) and “class Test” creates old style class (without object parent).
Refer this for more details.

Subclassing (Calling constructor of parent class) 
A child class needs to identify which class is its parent class. 
This can be done by mentioning the parent class name in the definition of the child class. 
Eg: class subclass_name (superclass_name): 
_ _ _ 
_ _ _ 

"""