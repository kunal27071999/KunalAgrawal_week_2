"""
14. WAP to declare the static variable as school name in above Student class 
	1. Declare within class and outside the method body
	2. inside constructor using class name
	3. inside method using class name
	4. inside class method using class name or cls variable5.  insite static methos using class name 
"""

class student:
    schoolName = "DPS"
    def __init__(self,name,roll,schoolName):
        self.name = name            
        self.roll = roll
        student.schoolName = schoolName

    def student(self,school):
        self.school = school


s = student("kunal",17,"DPS")

