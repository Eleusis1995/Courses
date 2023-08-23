""""
recap
1 in python, we could extend the behavior of built-in data structures
just like we do with regular user-defined ones
2 to do that, we simply define a subclass that inherits from the respective
built-in, and modify or enhance only the behaviour we care about
"""


from random import choice
from typing import Any

class FunnyDict(dict):
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