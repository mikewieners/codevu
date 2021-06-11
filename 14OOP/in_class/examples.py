# object - an instance of a class; everything is an object; 
# class - template (cookie cutter) used to construct objects and includes all attributes and methods
# attribute - variables associated with a class or object
# method - function within a class and any objects of that class' type

# inheritance - create a new class (child) by extending an existing class (parent); the child
# has all the attributes and methods of the parent class plus additional attributes and methods
# defined by the child class

from datetime import date

today = date.today()
print(type(today))