"""
2. Write note on composition

"""


"""
It is one of the fundamental concepts of Object-Oriented Programming.
In this concept, we will describe a class that references to one or 
more objects of other classes as an Instance variable. Here, by using
the class name or by creating the object we can access the members of
one class inside another class. It enables creating complex types by 
combining objects of different classes. It means that a class Composite
can contain an object of another class Component. This type of relationship 
is known as Has-A Relation.


composition – diagrammatic representation

 In the above figure Classes are represented as boxes with the class name
  Composite and Component representing Has-A relation between both of them.   

class A :

    
    # variables of class A
    # methods of class A
    ...
    ...

class B : 
    # by using "obj" we can access member's of class A.
    obj = A()

    # variables of class B
    # methods of class B
    
    ...
    ...

"""