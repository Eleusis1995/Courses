from collections import UserDict
from random import choice
from typing import Any

class FunnyDict(dict):#option 1
    not_found = ["404","Wait, what", "Try again, or not?"]

    def __getitem__(self, __key: Any) -> Any:
        if not __key in self:
            return choice(self.not_found)
        return super().__getitem__(__key)
    def get(self,value):
        return self.__getitem__(value)
    

class FunnyDict2(UserDict):#option 2 : UserDict is a wrapper from dict
    not_found = ["404","Wait, what", "Try again, or not?"]

    def __getitem__(self, __key: Any) -> Any:
        if not __key in self:
            return choice(self.not_found)
        return super().__getitem__(__key)
    
population = FunnyDict({
    "CAN": 38,
    "USA": 329,
    "IND": 1380
})
print(population["CAN"])
print(population["CANADA"])
print(population.get("CANADA"))
print(population.get("CAN"))
population2 = FunnyDict2({
    "CAN": 38,
    "USA": 329,
    "IND": 1380
})
print(population2["CAN"])
print(population2["CANADA"])
print(population2.get("CANADA"))
print(population2.get("CAN"))