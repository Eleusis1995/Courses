from typing import Any


class Contact:
    def __init__(self, name, last_name, phone = None, email = None, displaye_mode = "masked") -> None:
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.displaye_mode = displaye_mode
    @staticmethod
    def masking(string_to_mask):
        return string_to_mask.replace(string_to_mask[len(string_to_mask)//2:], len(string_to_mask)//2 * '*')
    def __repr__(self) -> str:
        return f"Contact({self.masking(self.name)}, {self.masking(self.last_name)})"
    def __str__(self) -> str:
        return f"{self.name[0:1]}{self.last_name[0:1]}"
    def __format__(self, __format_spec: str) -> str:
        if __format_spec == "unmasked":
            return f"Contact({self.name}, {self.last_name}, {self.phone}, {self.email})"
        return repr(self)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Contact): #verify first if other is an instance of the class
            return False
        return (self.name == other.name  and self.last_name == other.last_name) or (self.phone == other.phone and self.email == other.email)
    def __hash__(self) -> int:
        return hash(self.name, self.last_name, self.email, self.phone)
    
c1 = Contact("Juan", "Camaney")
print(f"{c1}")
print(f"{c1:unmasked}")
print(str(c1))