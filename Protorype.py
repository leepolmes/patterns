# pylint: disable=too-few-public-methods
"Prototype Concept Sample Code"
from abc import ABCMeta, abstractmethod


class InterfacePrototype(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def clone():
       pass


class MyClass(InterfacePrototype):
    

    def __init__(self, something):
        self.something = something
    def clone(self):
        
        return type(self)(
            self.something)

    def __str__(self):
        return f"something={self.something}"



OBJECT1 = MyClass([1, 2, 3, 4])  
print(f"OBJECT1 {OBJECT1}")
print(id(OBJECT1))

OBJECT2 = OBJECT1.clone()  
OBJECT2.something[1] = 500


print(f"OBJECT2 {OBJECT2}")
print(id(OBJECT2))
print(f"OBJECT1 {OBJECT1}")
print(id(OBJECT1))
