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

class Creator:

  def create_object(some_property):

        if some_property == 'a':
            return Object1()
        if some_property == 'b':
            return Object2()
        if some_property == 'c':
            return Object3()
        return None


hren = Creator.create_object('a')
print(hren.name)

