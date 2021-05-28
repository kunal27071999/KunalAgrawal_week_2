"""
4. Using composition: Use below details and write a program to print the Laptop details along with its processor specification
	1. Create two classes Laptop and Processor. 
	2. Create "display" method in the Laptop class

"""

class Processor:

    def __init__(self,core,generation):
        self.core = core
        self.generation = generation

    

class laptop:

    def __init__(self,core,generation,comapny,price,):
        self.obj1 = Processor(core,generation) 
        self.company = comapny
        self.price = price
        


    def display(self):
        print("Laptop company :", self.company)
        print("Laptop price :", self.price)
        print("Laptop core :", self.obj1.core)
        print("Laptop generation :", self.obj1.generation)


l = laptop(4,"8GEN","DELL",90000)
l.display()