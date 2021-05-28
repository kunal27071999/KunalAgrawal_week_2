"""
7. Uning Inheretance	
	1. Create parent class with variable as name 
	2. Initialize the instance with new variable v2=20 inside the constructer
	3. Create method m1 with self as parameter and print the method name 
	4. Create classmethod m2 and print the method name 
	5. Create staticmethod m3 and print the method name 
	6. Create chile class and inherit it wil parent 
	7. Create instance of the child class and call methods defined in parent class
	8. print variables declared in the parent class using instance of child 

"""

class parent:
    name = "kunal"

    def __init__(self,v2 = 20):
        self.v2 = v2

    def m1(self):
        print("inside m1")

    @classmethod
    def m2(cls):
        print("inside m2")

    @staticmethod
    def m3():
        print("inside m3")

class child(parent):
    def __init__(self):
        parent.__init__(self)

    print("inside child")

c1 = child()
c1.m1()
c1.m2()
c1.m3()
print(c1.name)
print(c1.v2)