"""
1.- We traditionally define class state in class body
2.- class state is stored in a mappingproxy object and retrived using __dict__
3.- class state is shared and accessible by all instance of that class
"""

class MercedezBenz: #class example
    doors = 2
    wheels = 4

print(MercedezBenz)
print(type(MercedezBenz)) #type of 'MercedezBenz'
print(MercedezBenz.__base__)
print(MercedezBenz.__name__) #class name
print(MercedezBenz.__dict__) #gives back atribute from class in dictionary format
MercedezBenz.doors = 4 #changing doors
print(MercedezBenz.__dict__)
MercedezBenz.Model = 'G' #adding atribute
print(MercedezBenz.Model)#printing new atribute 'G'

M1 = MercedezBenz() #ceating two instrances
M2 = MercedezBenz()
print(M1 == M2) #they are not the same

#_____________________________
#redifinding class
"""
1.- We add behavior to our class by defining functions
2.- These functions are special in theh they always have at leats one parameter
3.-That parameter is by convenction called self
4.- when functions are defined within the body of a class, they become bound (or attahced)
to instances of the class

"""
class MercedezBenz: #class example
    doors = 2
    wheels = 4
    model = 'G'

    def drive(self):
        return self

M3 = MercedezBenz() #creating other 2 instances
M4 = MercedezBenz()
print(M3.drive()) #printing objects in memory
print(M4.drive()) 
print(M3 == M3.drive())#True, becase methods return onject itself

print(type(MercedezBenz.drive)) #it's a function
print(M3.drive) #Method bound to a specific object
print(M4.drive)
print(type(M3.drive))#it is a method

#_____________________
"""
1.- Attributes are simply variables associated with objects
2.- Instances attributes could be set before or after the instances objecrs is returned
3.-That´s said, it is best prectice to set them in __init__, a special method
which existes specialy for this purpose
"""
class MercedezBenz: #class example
    doors = 2
    wheels = 4
    model = 'G'
    def __init__(self, color="black"):
        """
        After instance creation, but before it is returned
        """
        self.color = color

    def drive(self):
        return self

M1 = MercedezBenz("red")
print(M1)
M2 = MercedezBenz()
print(M2)

#__________________+
"""
1.- In addition to the traditional dot access syntax, attributes could also be read
and set ussing getattr and setattr built-in
2.- Thse methods are most useful ifn we're manipulating object programmatically
and specually if we're doing to at scale
"""
class MercedezBenz: #class example
    doors = 2
    wheels = 4
    model = 'G'
    def __init__(self, color="black"):
        """
        After instance creation, but before it is returned
        """
        self.color = color

    def drive(self):
        return self

M1 = MercedezBenz()
M2 = MercedezBenz()
print(getattr(M1, "color"))
setattr(M1, 'otracosa', 18)
print(getattr(M1, "otracosa"))

objs = [M1, M2]
atributes = ['doors','color']
values = [5, 'navy']
for ob in objs:
    for atri, val in zip(atributes,values):
        setattr(ob, atri, val)



print(getattr(M1, "doors"))
print(getattr(M1, "color"))

try:
    print(M1.wings)
except AttributeError as e:
    print(e)

#instead we can used getter
print(getattr(M1, "wings", "No atributte wings"))

"""
1.- self is always the first argument passed to instance methods
2.- It represents the instances object bound to the method
3.- It is called self by (bood) convention only
"""


"""
Class ans staic Methods
1.- In addition to instance methods, python has static and class methods
2.- In class methods, the class is implicitly passed as the firts argument, 
whereas in static methods, neither the instance object not the class is passed
3.- Static mwthods are like regular functions that are grouped with the class namespace because they're
somehoce conpectually related to the class
"""
class MercedezBenz: #class example
    doors = 2
    wheels = 4
    model = 'G'
    def __init__(self, color="black"):
        """
        After instance creation, but before it is returned
        """
        self.color = color

    def drive(self):
        return self
    
    @staticmethod
    def driver_statci():
        return "static methods"

    @classmethod
    def driver_clas(cls):
        return f"class method for {cls}"

M1 = MercedezBenz()
print(M1.driver_statci)
print(M1.driver_clas)

print(MercedezBenz.driver_statci)
print(MercedezBenz.driver_clas)

"""
alternavit:

"""
class MercedezBenz: #class example
    """
    Class to test
    """
    doors = 2
    wheels = 4
    model = 'G'
    def __init__(self, color="black"):
        """
        After instance creation, but before it is returned
        """
        self.color = color

    def drive(self):
        return self
    
    #@staticmethod
    def driver_statci():
        return "static methods"

    #@classmethod
    def driver_clas(cls):
        return f"class method for {cls}"

    driver_statci = staticmethod(driver_statci)
    driver_clas = classmethod(driver_clas)

"""
__dict__ method return the atributs from an object as dictionary
1.- All instances attibutes are stored in an instance-specific mapping object
2.- For instances, that objects is plain in python dictionary
3.- It is accessed using instances.__dict__ syntax

1.- Unlike instances, however, the class __dict__ is a mappingproxy, which is more restricted type of read-only where all the keys are strings
"""

M1 = MercedezBenz()
M2 = MercedezBenz("RED")
setattr(M2,"Engine", "V6")
M1.__dict__["ModelYear"] = 1990
for obj in [M1,M2]:
    print(obj.__dict__)

for key, value in MercedezBenz.__dict__.items():
    print(f"{key} : {value}")


"""
Immutables: boolenas, ints, floats, string, tuple
Mutable: lists

It is not good idea to use mutable variables as atributes ina a class, these becase the instamces share
the same varibles
"""
class Tires:
    def __init__(self, kind, diatnces_covered):
        self.kind = kind
        self.diatnces_covered = diatnces_covered
class MercedezBenz: #class example
    """
    Class to test
    """
    doors = 2
    wheels = 4
    model = 'G'
    tires = [Tires("operational", 10) for i in range(4)]
    def __init__(self, color="black"):
        """
        After instance creation, but before it is returned
        """
        self.color = color

    def drive(self):
        return self
    
    #@staticmethod
    def driver_statci():
        return "static methods"

    #@classmethod
    def driver_clas(cls):
        return f"class method for {cls}"

    driver_statci = staticmethod(driver_statci)
    driver_clas = classmethod(driver_clas)

M1 = MercedezBenz("RED")
print(M1.tires)
M2 = MercedezBenz("BLUE")
M1.tires.append(Tires("Classic", 21))
print(M2.tires)