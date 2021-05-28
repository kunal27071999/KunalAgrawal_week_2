"""

6. Using composition: 
	1. Create class c1 with variable v1=2 and method m1. Method m1 prints the method name and class name. Inside the consuructer initialize the self with new variable v2=4
	2. Create class c2 with variable v3=6 and method m2. Method m1 prints the method name and class name. Inside the consuructer initialize the self with new variable v4=8
	3. Define method m3 in the class c2 , create the instance of class c2 and print the v1 and v2. Call m2 method using c1. Print v3 and v4 using self and c2. Call m2 using self.

"""

class c1:
    v1 = 2 

    def __init__(self,v2 = 4):
        self.v2 = v2

    def m1():
        print("Inside m1")
        print("inside c1")

class c2(c1):
    v3 = 6

    def __init__(self,v4 = 8):
        self.v4 = v4
        c1.__init__(self)

    def getv4(self):
        return self.v4

    def m2():

        print("Inside m2")
        print("inside c2")





obj=c2()
print("v1 = ",obj.v1)
print("v2 = ",obj.v2)
print("v3 = ",c2.v3)
print("v4 = ",obj.v4)
