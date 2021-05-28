"""
11. WAP to demonstrate where can we declare the instance variables
	1. inside constructer
	2. insite instance method 
	3. ouside class ny using object reference variable

"""

class student:

    def __init__(self, name, rollno):

        self.name = name
        self.rollno = rollno

    def display(self):

        print("hello my name is:", self.name)
        print("my roll number is:", self.rollno)

s = student('HARRY', 1001)
s.display()
print(s.name)

class emp: 
    name='Harsh'
    salary='25000'

    def setAge(self,age):
        self.age = age

    def show(self): 
        print(self.name)
        print(self.salary)
        print(self.age)

# Driver Code
e1 = emp() 
e1.setAge(23)
e1.show()
print(getattr(e1,'name'))
setattr(e1,'height',152) 
print(getattr(e1,'height'))
delattr(emp,'salary') 