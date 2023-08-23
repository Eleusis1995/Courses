class DNABase:
    valid_bases = {"a":"adenine", 
                   "c":"cytosine", 
                   "g":"guanine", 
                   "t":"thymine"}
    def __init__(self, nucleotide) -> None:
        self.base = nucleotide

    def get_nucleotide(self):
        return self._nucleotide
    
    def set_nucleotide(self,new_nucleotide):
        if new_nucleotide.lower().strip() not in self.valid_bases and new_nucleotide.lower().strip() not in self.valid_bases.values():
            raise ValueError("Not valid name")
        self._nucleotide = self.valid_bases.get(new_nucleotide[0].lower().strip())

    def __repr__(self) -> str:
        return f"DNABase({self._nucleotide})"
    base = property(fget=get_nucleotide,fset=set_nucleotide)

Object = DNABase("a")
print(Object.base)
Object.base = "Guanine"
print(Object.base)
Object.base = "t"
print(Object)
Object.base = "cyTosIne             "
print(Object)
