"""
5. Using composition: Use below details and write a program to print the User details along with its Car details
	1. Create two classes User and Car. 
	2. Create "display" method in both classes.

"""

class car:
    def __init__(self,company,color,price):
        self.company = company
        self.color = color
        self.price = price

    def display(self):
        print("Car company :",self.company)
        print("Car color :",self.color)
        print("Car price :",self.price)


class user:

    def __init__(self,name,age,company,color,price):
        self.name = name 
        self.age = age
        self.obj1 = car(company,color,price)

    def display(self):
        print("User name :", self.name)
        print("User age :", self.age)
        self.obj1.display()


u = user("kunal",18,"audi","black",1000000)
u.display()
        