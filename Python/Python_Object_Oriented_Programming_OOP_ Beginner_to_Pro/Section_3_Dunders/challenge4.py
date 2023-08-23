""""
Requirements
> Define a new type called Vector that stores 3 instance attributes: x, y, z
> Users should be able to create new instances as Vector(x=1, y=2, z=3), where the
coordinates are positional args with no defaults
andybek.com> Instances of this new Vector type should have a representation that would help the
user reconstruct the instance
> The magnitude of the vector should be accessible through a method, ideally a built-in
- hint: the magnitude is calculated as sqrt of sum of squared coordinates
- hint2: as far as built-ins are concerned, __len__ will not work; try to target abs()?
> Users should be able to add two vectors to get a third, e.g. Vector(1, 2, 3) + Vector(4, 5,
6) -> Vector(5, 7, 9)
> Users should be able to numerically scale a vector, e.g. Vector(1, 2, 3) * 2 = Vector(2, 4,
6)
> The scalar multiplication operation should work the same regardless of the order of
operands, e.g. Vector(1, 2, 3) * 2 = 2 * Vector(1, 2,3)

> All comparison operators should be supported between two instances of Vector
> Vector should be hashable
andybek.com> A Vector instance should evaluate to False if and only if its magnitude is zero
> Lastly, the Vector class should let the user select coordinates using square brackets too,
e.g. if v1 = Vector(1, 2, 3) then both v1['y'] and v1['Y'] should return 2
"""
import math
from functools import total_ordering
class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __sizeof__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError(f"{other_vector} is not type Vector")
        return Vector(self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z)
    
    def __radd__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError(f"{other_vector} is not type Vector")
        return self + other_vector
    
    def __sub__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError(f"{other_vector} is not type Vector")
        return Vector(self.x - other_vector.x, self.y - other_vector.y, self.z - other_vector.z)
    
    def __mul__(self, magnitud):
        return Vector(self.x * magnitud, self.y * magnitud, self.z * magnitud)
    
    def __rmul__(self, magnitud):
        return self * magnitud
    
    def __eq__(self, other_vector: object) -> bool:
        if not isinstance(other_vector, Vector):
            raise TypeError(f"{other_vector} is not type Vector")
        return self.__sizeof__() == other_vector.__sizeof__()
    
    def __gt__(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError(f"{other_vector} is not type Vector")
        return self.__sizeof__() > other_vector.__sizeof__()
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z)) #Se manda un set
    
    def __bool__(self):
        if self.__sizeof__() == 0:
            return False
        return True
    def __getitem__(self, item):
        # if isinstance(item,str):
        #     if item.upper() == "X":
        #         return self.x
        #     elif item.upper() == "Y":
        #         return self.y
        #     elif item.upper() == "Z":
        #         return self.z
        #     else:
        #         raise TypeError("No existe esa opcion")
        # if item == 0: return self.x
        # elif item == 1: return self.y
        # elif item == 2: return self.z
        # else: raise TypeError("No existe esa opcion")
        local= {
            0: "x",
            1: "y",
            2: "z"
        }
        if type(item) == str and item.lower() in ["x","y", "z"]:
            return eval(f"self.{item.lower()}")
        elif type(item) == int and item in [0,1,2]:
            return eval(f"self.{local[item]}")

Vector = total_ordering(Vector)
v1 = Vector(3,5,5)
v2 = Vector(3,4,5)
print(f"La sumatorio de  vecotores es {v1 + v2}")
print(f"La sumatorio de  vecotores es {v2 + v1}")
print(f"La resta de v1 - v2 de  vecotores es {v1 - v2}")
print(f"La resta de v2 - v1 de  vecotores es {v2 - v1}")
print(f"multiplica por 4 el vector 1 {v1*2}")
print(f"multiplica por 4 el vector 1 {2*v1}")
print(f"Comparacion de vectores {v1 == v2}")
print(f"Comparacion de vectores {v1 != v2}")
print(f"Comparacion de vectores {v1 > v2}")
print(f"Comparacion de vectores {v2 > v1}")
print(f"Hashable {hash(v1)}")
print(f"Bool {bool(v1)}")
print(f"Coordinates X = {v1['x']},Y = {v1['y']},Z = {v1['z']}")
print(f"Coordinates X = {v1[0]},Y = {v1[1]},Z = {v1[2]}")
