#Inheritance
from random import getrandbits


class Virus: #Super Class
    def __init__(self, name, reproduction_rate,resistence) -> None:
        self._name = name
        self._reproduction_rate = reproduction_rate
        self._resistence = resistence
        self._load = 1
        self._host = None

    def infect(self, host):
        self._host = host

    def reproduce(self):
        if self._host is not None:
            self._load*= (1 + self._reproduction_rate)
            should_mutate = getrandbits(1)
            print(f"Should mutate: {should_mutate}")
            if should_mutate:
                try:
                    self.mutate()
                except AttributeError:
                    pass
           
            return True, f"Virus reproduction in {self._host}. Virus Load: {int(self._load)}"
        
       
        raise AttributeError("Virus needs to infect a host before being able to reproduce")
    infect = property(fset=infect)

class RNAVirus(Virus): #RNAVirus is a subclass that inheritances from Virus
    geno = "deoxyribonucleic"

    def reproduce(self):
        success, status = Virus.reproduce(self)
        if success:
            return f"{self._name} just replicated in the cytoplasm of {self._host} cells"
        
class DNAVirus(Virus): #RNAVirus is a subclass that inheritances from Virus
    geno = "ribonucleic"

    def reproduce(self):
        #success, status = Virus.reproduce(self)
        success, status = super().reproduce()
        if success:
            return f"{self._name} just replicated in the cytoplasm of {self._host} cells"

class CoronaVirus(RNAVirus):
    # def infect(self): #Override the original functionality of the father's method
    #     return f" A {self.__class__.__name__} specific methos with a different signare from the parameters"
    pass

class SARCov2(CoronaVirus):
    def __init__(self, name, reproduction_rate, resistence) -> None:
        super().__init__(name, reproduction_rate, resistence)
    def mutate(self):
        print(f"The {self._name} virus just mutated its spike protein")

print(issubclass(SARCov2,CoronaVirus)) # Check if the class is a subclass
print(issubclass(CoronaVirus,RNAVirus))
print(issubclass(SARCov2,Virus))
V1 = Virus("SIDA", 3,50)
V1.infect = "Animal"
print(V1.reproduce())

r = RNAVirus("HIV", 1.1,0.2)
r.infect = "Monkey"
print(r.reproduce())
# All classes inherite from object
# All python classes implicity inherit from 'object'

#Method Resolution order

class TempVirus:
    attr = "some_class_attributes"
    attr_other = "some_other_class_attributes"

    def __init__(self, attr) -> None:
        self.attr = attr

# get the supper class
print(CoronaVirus.__base__)
# get the whole string of inheritage of the class
print(CoronaVirus.__mro__)

c = CoronaVirus("Juan",1,2)

s = SARCov2("Original",1.2,8)
s.infect = "Tobi"
for _ in range(4):
    print(s.reproduce())

#Subclass __init__
