import copy

class Singleton():
    
    value = []

    def __new__(cls):
        return cls

   

    @staticmethod
    def static_method():
        pass
       



        


print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT3)}")