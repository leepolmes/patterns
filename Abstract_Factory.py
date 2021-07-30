from abc import ABCMeta, abstractmethod

class InterfaceType():
    @staticmethod
    @abstractmethod

    def create_object():
        pass
 

class Object1(InterfaceType):

    def __init__(self):
        self.name = 'Object1'
    
    def create_object(self):
        return self

class Object2(InterfaceType):

    def __init__(self):
        self.name = 'Object2'
    
    def create_object(self):
        return self

class Object3(InterfaceType):

    def __init__(self):
        self.name = 'Object3'

    def create_object(self):
        return self

class NotObject1(InterfaceType):

    def __init__(self):
        self.name = 'NotObject1'
    
    def create_object(self):
        return self

class NotObject2(InterfaceType):

    def __init__(self):
        self.name = 'NotObject2'
    
    def create_object(self):
        return self

class NotObject3(InterfaceType):

    def __init__(self):
        self.name = 'NotObject3'

    def create_object(self):
        return self

class Factory1:
   @staticmethod
   @abstractmethod
   def create_object(some_property):
        

        if some_property == 'a':
            return Object1()
        if some_property == 'b':
            return Object2()
        if some_property == 'c':
            return Object3()
        return None


class Factory2:
    @staticmethod
    @abstractmethod
    def create_object(some_property):

        if some_property == 'a':
            return NotObject1()
        if some_property == 'b':
            return NotObject2()
        if some_property == 'c':
            return NotObject3()
        return None


class AbstractFactory(InterfaceType):
    

    @staticmethod
    def create_object(some_property):
      if some_property in ['aa', 'ab', 'ac']:
                return Factory1().create_object(some_property[1])
      if some_property in ['ba', 'bb', 'bc']:
                return Factory2().create_object(some_property[1])

hren = AbstractFactory.create_object('aa')
hren2 = AbstractFactory.create_object('bb')
print(hren.name)
print(hren2.name)