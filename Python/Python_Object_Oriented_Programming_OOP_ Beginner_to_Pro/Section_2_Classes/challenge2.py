from enum import Enum
import random
class StrenghtPasswordLevel(Enum):
    LOW = "low"
    MID = "mid"
    HIGH = "high"
strength_dict = {
        StrenghtPasswordLevel.LOW: 8,
        StrenghtPasswordLevel.MID: 12,
        StrenghtPasswordLevel.HIGH: 16
    }
class Password:
    
    lowcase_charachter = [chr(i) for i in range(ord("a"), ord("z")+1)]
    uppercase_character = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    simbols_character = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(92,97)] + [chr(i) for i in range(123, 127)]
    numbers = [str(i) for i in range(10)]

    def __init__(self, strength = StrenghtPasswordLevel.MID, length = None):
        self.strength = strength
        if not length:
            self.length = strength_dict[self.strength]
        else:
            self.length = length
        self.password = self.create_password(self.strength,self.length)

    def create_password(self,strength,passlen):
        password = ""
        if strength == StrenghtPasswordLevel.LOW:
            for char in range(passlen):
                password+=random.choice(self.lowcase_charachter + self.uppercase_character)
        elif strength == StrenghtPasswordLevel.MID:
            for char in range(passlen):
                password+=random.choice(self.lowcase_charachter + self.uppercase_character + self.numbers)
        elif strength == StrenghtPasswordLevel.HIGH:
            for char in range(passlen):
                password+=random.choice(self.lowcase_charachter + self.uppercase_character + self.numbers + self.simbols_character)
        else:
            ValueError("No such option set")
        return password

    @classmethod
    def show_input_universe(cls):
        return {
            "Lower cases":cls.lowcase_charachter,
            "Upper casses":cls.uppercase_character,
            "Numbers": cls.numbers,
            "Simbols":cls.simbols_character
        }

P1 = Password()
print(P1.password)
P2 = Password(StrenghtPasswordLevel.HIGH)
print(P2.password)
P3 = Password(StrenghtPasswordLevel.HIGH, 20)
print(P3.password)
P4 = Password()
print(P4.password)

print(Password.show_input_universe())

    