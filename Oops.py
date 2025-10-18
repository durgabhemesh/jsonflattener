
from abc import ABC, abstractmethod

class Human():

    def __init__(self,amount):
        self.amount=amount
        self.__balance=amount
        self._bal=amount

    def get_balance(self):
        print(self.__balance)
        return self.__balance

    def set_balance(self,amount):
        self.__balance+=amount


class Parent(Human):

    def __init__(self,balance):
        super().__init__(balance)




obj2=Parent(5000)

obj2.set_balance(500)
obj2.get_balance()

#Multiple Inhertence

class Human():
    def show(self):
        print("In Human")

class Father():
    def show(self):
        print("In Father")

class Child(Father,Human):
    pass

obj=Child()

obj.show()


#Abstraction

class Bike(ABC):

    @abstractmethod
    def RE(self):
        pass

class Imple(Bike):

    def RE(self):
        pass




pp=Imple()

pp.RE()


#class methods

class Class():
    name="Some"

    def __init__(self):
        print(Class.name)

    @classmethod
    def changename(cls):
        cls.name="Hey"


cl=Class()

cl.changename()
print(cl.name)

cl2=Class()


