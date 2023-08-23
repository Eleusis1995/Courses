""""
recap
1
built-in types could be extended both to add functionality as
well customize existing behavior
3 some commonly extended built-ins are: list, set, dict, and str
2
this includes subclass overrides of specific dunders or the definition
of new methods and attributes
4
int and float are also often inherited in creating numeric
abstractions with custom behavior
"""

class AvgList(list):
    def __init__(self, *args):
        if args and type(args[0]) != list:
            super().__init__(args)
        else:
             super().__init__(args[0])

    def average(self):
        return sum(self) / len(self)
    
l1 = AvgList(1,2,3,4,5,3,42323,8)
print(l1.average())
l2 = AvgList([1,2,3,4,5,3,42323,8])
print(l2.average())