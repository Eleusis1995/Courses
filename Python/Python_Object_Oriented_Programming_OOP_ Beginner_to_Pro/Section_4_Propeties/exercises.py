#loyal customers

class Customer:
    loyalty_levels = {"Brozen","Golden","platinum"}
    def __init__(self, loyalty) -> None:
        self.loyalty = loyalty

    def set_loyolty(self,level):
        if level not in self.loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified")

# c1 = Customer("Brozen")
# c2 = Customer("Golden")
# c3 = Customer("platinum")
# c4 = Customer("Platinu")

# def get_discount(discount_level):
#     return  {
#         "Brozen":0.1,
#         "Golden":0.2,
#         "platinum":0.3
#     }.setdefault(discount_level, "There is no that option") #Figoure out how to use a raise error
    
# for customer in [c1,c2,c3,c4]:
#     print(f"The discount for {customer.loyalty} is {get_discount(customer.loyalty)}")

#Always start plain
# c4.set_loyolty("Golden")

class Customer:
    loyalty_levels = {"Brozen","Golden","platinum"}
    def __init__(self, loyalty) -> None:
        self._loyalty = loyalty

    def set_loyolty(self,level):
        if level not in self.loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified")
        self._loyalty = level
#Provated and mabled atributs
# 1 remember, attributes and methods defined on a pyrthon clñass are public
# 2 There are no provate or protect attributes per se
# 3 as programmers we communucated our intent by relying on naming conventions, of which two important ones are
# one _ meand private
# two __ means attribute are name mangled with the class
def get_discount(discount_level):
    return  {
        "Brozen":0.1,
        "Golden":0.2,
        "platinum":0.3
    }.setdefault(discount_level, "There is no that option") #Figoure out how to use a raise error
    

class Customer:
    loyalty_levels = {"Brozen","Golden","platinum"}
    def __init__(self, loyalty) -> None:
        self._loyalty = loyalty

    def set_loyolty(self,level):
        if level not in self.loyalty_levels:
            raise ValueError(f"Invalid loyalty {level} specified")
        self._loyalty = level
    
    def get_loyalty(self):
        return self._loyalty
    
    loyalty = property(fget=get_loyalty,fset=set_loyolty) #Throuh variable loyalty we acces to self._loyalty
    
    

c1 = Customer("Brozen")
c2 = Customer("Golden")
c3 = Customer("platinum")
c4 = Customer("Platinu")

for customer in [c1,c2,c3,c4]:
    print(f"The discount for {customer.loyalty} is {get_discount(customer.loyalty)}")

#Breaking changes

#DEcoretaro refresh
#A de corator is a funcrtion that takes another function as argument, adds
# some functionality, then returns it, and does all of this without
#otherwise changing the function
def ten_times(x):
    return x*10

tenx = ten_times #this like a ponter to function
print(tenx(5))

#a func can be passed as args to other function
def pass_three_to(func):
    what = 3
    return func(what)
print(pass_three_to(tenx))
print(pass_three_to(ten_times))

@pass_three_to
def squer(x):
    return x**2

print(squer)

# definign a func within another one
def outer():
    def inner():
        return "Inner func"
    s = inner()
    return s
print(outer())


#we can also return functioin from functions
def give_me_a_function():
    def new_func():
        return "The new function is returning"
    return new_func()
re = give_me_a_function()
print(re)

# Closures
def greet(who):
    how = "Goog morning"
    def create_greeting():
        return f"{how}. {who}!"
    return create_greeting # return addres in memory

a = greet("Andy")
print(a) #Prints just the address in memory
print(a())

#decorator are desing pattern built on the shoulders on these two gigants: first-class functions + closures
from random import randint
def odd_or_even(func):
    def inner():
        num = func()
        print(f"The number {num} is {'even' if num %2 == 0 else 'odd'}")
        return num
    return inner # remeber always return inner function
    
@odd_or_even
def bingo():
    return randint(1,50)



b = bingo()
print(b)