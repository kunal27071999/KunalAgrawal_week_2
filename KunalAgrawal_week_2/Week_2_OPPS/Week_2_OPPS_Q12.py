"""
12. Using variables declared in Que 4, 
	1. Print using self
	2. delete using self 
	3. delete using object reference
	4. Update the value of RollNo and print the object
"""

class Stud:
    def __init__(self,Name,RollNo):
        
        self.Name = Name
        self.RollNo = RollNo

    def display(self):
        
        print("hello my name is:", self.Name)
        print("my roll number is:", self.RollNo)


s = Stud("Kunal", 17)

s.display()