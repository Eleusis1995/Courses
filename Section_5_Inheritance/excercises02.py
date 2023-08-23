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
    
    @property
    def name(self):
        return self._name
    
    infect = property(fset=infect)

class DNAVirus(Virus): #RNAVirus is a subclass that inheritances from Virus
    geno = "ribonucleic"

    def reproduce(self):
        #success, status = Virus.reproduce(self)
        success, status = super().reproduce()
        if success:
            return f"{self._name} just replicated in the cytoplasm of {self._host} cells"
        
class CoronaVirus(DNAVirus):
    # def infect(self): #Override the original functionality of the father's method
    #     return f" A {self.__class__.__name__} specific methos with a different signare from the parameters"
    pass

class SARSCov2(CoronaVirus):
    known_variants = ["alpha", "beta", "gama", "epsilon"]
    def __init__(self,variant):
        super().__init__("SARSCov2", 2.49,1.3)
        self._variant = variant

    def mutate(self):
        print(f"The {self.name} virus just mutated its spike prteine")

    @property
    def variant(self):
        return self._variant
    
    @variant.setter
    def variant(self, value):
        if value.lower() not in self.known_variants:
            raise ValueError("Error")
        self._variant = value.lower()


class DoubleMutant(SARSCov2):
    @property
    def variant(self):
        print("Getter from the subclass")
        return self._variant
    #@SARSCov2.variant.setter #we are indicating the class where this methos is define as property
    @variant.setter
    def variant(self, value):
        self._variant = value.lower()

cv = SARSCov2("ALPHA")
dv = DoubleMutant("NEW variant")
print(dv.variant)
"""""
1
properties defined in the parent could be extended/modified in the
subclass
2
because properties live in the namespace of the class in which they
'
re
defined, referring to the them from the subclass requires the use of a
fully qualified name in the subclass, i.e. one that specifies the parent
class name
3
when inheriting properties, we reserve the flexibility to only
extend/modify the methods we care about, e.g. any combination of
get, set, de
"""