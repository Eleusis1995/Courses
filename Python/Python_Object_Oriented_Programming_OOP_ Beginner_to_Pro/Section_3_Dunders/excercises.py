#Lets Add A __repr__
# We could customize our objects's representation by implementing __repr__ in the objects class definition
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str:
        return f" The {self.title} was written for {self.author}, it has {self.pages} and is considered a {self.book_type} book"

b = Book("Harry potter", "La autora de harry poter", "Fantasy", 12000)
print(b)

#Lets Add A __repr__ vs __str__
# 1.- Both, str and repr dunders are used to define custom string representation for given object
# 2.- Both str and repr dunders are used to define cutom representation for a given object
# 3.- repr ideally should return a valid python code wich, if evaluated, rebuilts the instance
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str: # default representation of the object, how the intsnace can be replicated
        #We can create a instance
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
        #return f" The {self.title} was written for {self.author}, it has {self.pages} and is considered a {self.book_type} book"
    def __str__(self) -> str:# Informal for end user
        return f"{self.title} by {self.author} in {self.book_type}"

b = Book("Harry potter", "La autora de harry poter", "Fantasy", 12000)
print(b)
print(str(b))
c = eval(repr(b))
print(c)

#__format__
print(f"{100:.3f}")
print(format(100,'.3f'))
print("{:.3f}".format(100))
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __str__(self) -> str:# Informal for end user
        return f"{self.title} by {self.author} in {self.book_type}"
    def __format__(self, __format_spec: str) -> str:
        if __format_spec == "short":
            return f"{self.title} - {self.author}"
        elif __format_spec == "stealth":
            return f"A book containing exactly {self.pages}. Guess?"
        return str(self)
    
a = Book("Lord of rings", "sabe quien", "Fantasy", 12000)
print(f"{a}")
print(f"{a:stealth}")

#Object Equality
# 1.- by default, instances of the same class in pyhton are not equal
# 2.- we customize object equality by defininf __eq__
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str: # default representation of the object, how the intsnace can be replicated
        #We can create a instance
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Book): #verify first if other is an instance of the class
            return False
        return self.title == other.title  and self.author == other.author
    def __ne__(self, other: object) -> bool:
        print("Comparing non-equality")
        if not isinstance(other, Book):
            return False
        return self.title != other.title  and self.author != other.autho
        
a = Book("Lord of rings", "sabe quien", "Fantasy", 12000)  
b = Book("Lord of rings", "sabe quien", "Fantasy", 12000)      
from collections import namedtuple
essay = namedtuple("essay",["title", "author"])
e = essay("Antifragile", "Nassim telab")
print(type(e))    
print(e == a)
print(b != a)
#Non-equal

#hasing and mutability
# 1.- a hash is juts a fixed-length integer that identifies an object
# 2.- an object is hashable if it:
#   - has a hash value that never changes over its life
#   - is comparable to other objects, and
#   - shares the same hash value with objects it compares to as equal
# 3.- Immutable data types in python (eg int, float, str, tuples to as equal)
# 4.- Hashes are extremely useful in facilitaing fast lookup in
# dictionries and membership checks in sets; as a result,
#dictionary keys and set memebers need to be hashble

# 1.- by default, user-defined class are hasheble
# 2.- when we define dunder eq, python (v3+) makes them un hashable mostly to protect us from unpleasant side effects
# 3.- we make a class hashable again by definign dunder hash which should always return an integer
# 4.- as it its closely related to equality, it is good idea for dunder hash to consider the same atributtes that dunder eq in determinign equality
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str: # default representation of the object, how the intsnace can be replicated
        #We can create a instance
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Book): #verify first if other is an instance of the class
            return False
        return self.title == other.title  and self.author == other.author
    def __hash__(self) -> int:
        return hash((self.title, self.author))
    
a = Book("Lord of rings", "sabe quien", "Fantasy", 12000)  
b = Book("Lord of rings", "sabe quien", "Fantasy", 12000) 
c = Book("Harry potter", "la autora de harry potter", "Fantasy", 5200)
print(hash(a) == hash(b))
print(hash(a) == hash(c))

#hash gotcha

#other Rich comparision
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str: # default representation of the object, how the intsnace can be replicated
        #We can create a instance
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Book): #verify first if other is an instance of the class
            return False
        return self.title == other.title  and self.author == other.author
    def __hash__(self) -> int:
        return hash((self.title, self.author))
    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages
    def __lt__(self, other):
        return NotImplemented
    
    def __le__(self, other):
        return self.pages <= other.pages
    
a = Book("Lord of rings", "sabe quien", "Fantasy", 11000)  
b = Book("Lord of rings", "sabe quien", "Fantasy", 12000) 
print(a<=b)


#The total_ordering higher-order function from the functools module adds
#support for all comparision oprator as long
# as we drfine dunder es, and one of gt.lt.ge,le, etc
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str: # default representation of the object, how the intsnace can be replicated
        #We can create a instance
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Book): #verify first if other is an instance of the class
            return False
        return self.title == other.title  and self.author == other.author
    def __hash__(self) -> int:
        return hash((self.title, self.author))
    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages
from functools import total_ordering
Book = total_ordering(Book) #it implement all the verification of greater than, less than, etc
a = Book("Lord of rings", "sabe quien", "Fantasy", 110000)  
b = Book("Lord of rings", "sabe quien", "Fantasy", 12000) 
print("=======================================")
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)

#Truthiness : cossas basias o con valor 'nulo' son falsas
#bool(0)
#bool([])
#Objects, including instances of user-defined classes, by default, are truthy
# to customize this behavior, we define special logic within dunder bool
class Book:
    def __init__(self, title, author, book_type, pages) -> None:
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages
    def __repr__(self) -> str: # default representation of the object, how the intsnace can be replicated
        #We can create a instance
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', '{self.pages}')"
    def __bool__(self):
        return bool(self.pages) and not (self.pages < 1)
    def __len__(self):
        return self.pages
a = Book("Lord of rings", "sabe quien", "Fantasy", 10)
print("========BOOL============")
print(bool(a))
print(len(a))

class BookShelf:
    def __init__(self, capcity) -> None:
        self.book = []
        self.capacity = capcity
    def add_book(self,book):
        if not isinstance(book, Book):
            raise TypeError("Only 'Book' objects can be added")
        if not self.capacity > len(self.book):
            raise OverflowError("Bookshelf is full")
        self.book.append(book)
    def __repr__(self) -> str:
        return f"{str(self.book)}"
    def __add__(self,other):
        if not isinstance(other, Book):
            raise TypeError("Only 'Book' objects can be added")
        new_shelf = BookShelf(self.capacity)

        for book in self.book:
            new_shelf.add_book(book)

        new_shelf.add_book(other)
        return new_shelf
    def __radd__(self,other):
        if not isinstance(other, Book):
            raise TypeError("Only 'Book' objects can be added")
        return self + other
print("=======================Book shelf======================")
a = Book("Lord of rings", "sabe quien", "Fantasy", 10)
b = Book("Harry", "sabe quien", "Fantasy", 10)
c = Book("El Libro de la selva", "sabe quien", "Fantasy", 10)
d = Book("Lord of rings", "sabe quien", "Fantasy", 10)
e = Book("Lord of rings", "sabe quien", "Fantasy", 10)
f = Book("Power ranger", "sabe quien", "Fantasy", 100000)

shelf = BookShelf(capcity=10)

for i in [a,b,c,d,e]:
    shelf.add_book(i)

print(f"============Previo a add {str(shelf)}")
shelf = shelf + f
print(f"============Poseterior a add {str(shelf)}")
shelf = f + shelf
print(f"============Poseterior a add por la derecha {str(shelf)}")

#getitem
#1.- We could add support for squeare brackes key lookup to out classes by implementing __getitem__
# we are dree to customize the functionality supported by
# adding further logic beyond the customary one based
#on integers and slice objects
#3 implemeting __getitem__ also makes out class iterable

class BookShelf:
    def __init__(self, capcity) -> None:
        self.book = []
        self.capacity = capcity
    def add_book(self,book):
        if not isinstance(book, Book):
            raise TypeError("Only 'Book' objects can be added")
        if not self.capacity > len(self.book):
            raise OverflowError("Bookshelf is full")
        self.book.append(book)
    def __repr__(self) -> str:
        return f"{str(self.book)}"
    def __add__(self,other):
        if not isinstance(other, Book):
            raise TypeError("Only 'Book' objects can be added")
        new_shelf = BookShelf(self.capacity)

        for book in self.book:
            new_shelf.add_book(book)

        new_shelf.add_book(other)
        return new_shelf
    def __radd__(self,other):
        if not isinstance(other, Book):
            raise TypeError("Only 'Book' objects can be added")
        return self + other
    
    def __getitem__(self,item):
        if isinstance(item, str):
            return [b for b in self.book if item.lower() in b.title.lower()] #Look for base in book title
        return self.book[item]
    
a = Book("1-Lord of rings", "sabe quien", "Fantasy", 250)
b = Book("2-Harry", "sabe quien", "Fantasy", 10)
c = Book("3-El Libro de la selva", "sabe quien", "Fantasy", 10)
d = Book("4-Lord of rings", "sabe quien", "Fantasy", 150)
e = Book("5-Lord of rings", "sabe quien", "Fantasy", 10)
f = Book("6-Power ranger", "sabe quien", "Fantasy", 100000)

shelf = BookShelf(capcity=10)

for i in [a,b,c,d,e,f]:
    shelf.add_book(i)

print("----implementing slicing----")
print(f"item: {shelf['LORD']}")
print(f"Derecho: {shelf[:]}")
print(f"Reves: {shelf[::-1]}")

#Definig our own magics

