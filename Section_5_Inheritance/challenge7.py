""""
> Define a new type called BankAccount that takes a single instance attribute:
initial_balance (defaults to 0)
andybek.com> This type should support deposit() and withdraw() methods, which in turn should
only support transactions in positive amounts, i.e. an attempt to deposit or withdraw
-2$ should be ignored
> Define 3 more specialized types of BankAccount with the following characteristics:
1. Savings: has pay_interest() method which deposits directly into the account when
called; interest rate: 0.0035
2. HighInterest: like Savings, but higher interest and with a withdrawal fee. The fee is
specified at initialization and defaults to $5. It is taken from the account's balance on every
withdrawal. Interest rate: 0.007
3. LockedIn: like HighInterest, but higher interest without the ability to withdraw on
demand. Interest rate: 0.009
> The balance of any of the above accounts should be available by attribute access syntax,
e.g. account.balance
> The representation of any of the instances should simply indicate the type of account
and the amount contained within, e.g. "A SavingsBankAccount with $100 in it
"""
class BankAccount:
    interest_rate = {
        "Savings":0.0035,
        "HighInterest":0.007,
        "LockedIn":0.009
        }
    def __init__(self,initial_balance = 0) -> None:
        self._initial_balance = initial_balance
        self.from_class = ""
    
    @property
    def balance(self):
        return self._initial_balance

    def deposit(self, add_amount):
        if add_amount > 0:
            self._initial_balance+=add_amount
        else:
            raise ValueError(f"{add_amount} must be gretaer that 0")
    def withdraw(self, sub_ammout):
        if sub_ammout > 0:
             self._initial_balance-=sub_ammout
        else:
            raise ValueError(f"{sub_ammout} must be gretaer that 0")
        
    def pay_interest(self):
        if self.from_class != "":
            self._initial_balance+= self._initial_balance * self.interest_rate[self.from_class]
            print(f"Deposited ${self._initial_balance * self.interest_rate[self.from_class]}")
        else:
            raise KeyError("This method just can be called from a subclass")

    def __repr__(self) -> str:
        #instance_name = "".join([t.__name__ for t in type(self).__mro__[:-1]])
        return f"A {self.__class__.__name__} with ${self._initial_balance} in it"
        
    deposit = property(fset=deposit)
    withdraw = property(fset=withdraw)

class Savings(BankAccount):
    def pay_interest(self):
        self.from_class = self.__class__.__name__
        super().pay_interest()
    

class HighInterest(Savings):
    def __init__(self, initial_balance=0,withdrawal_fee = 5) -> None:
        super().__init__(initial_balance)
        self._withdrawal_fee = withdrawal_fee

    #@withdraw.setter
    def withdraw(self, sub_ammout):
        sub_ammout +=self._withdrawal_fee
        super(Savings, HighInterest).withdraw.__set__(self,sub_ammout)
        #Savings.withdraw.fset(self,sub_ammout)

    withdraw = property(fset=withdraw)
   

class LockedIn(HighInterest):
    def withdraw(self):
        print(f" Cannot make an aeraly withdrawal from a locked in saving accocunt")

    

s = Savings(140)
print(str(s))
s.pay_interest()
print(str(s))
s.withdraw = 100
print(str(s))


h = HighInterest(100)
print(str(h))
h.pay_interest()
print(str(h))
h.withdraw = 10
print(str(h))




    