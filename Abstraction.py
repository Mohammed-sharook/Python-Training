# from abc import ABC, abstractmethod  # import ABS class from abs module
#
#
# class Abstract(ABC):  # Cannot able to create objects for abstract class
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def age(self,number):
#         print("His age is",number)
#
#
# obj = Abstract("sharook") # can't create obj for abs class
# obj.age(23)


# we can achieve abstraction using inheritance.

from  abc import ABC,abstractmethod


class Dog(ABC):
    def __init__(self, bread):
        self.bread = bread

    def about_bread(self):
        print("The dogs which from",self.bread,"are very powerful")

    @abstractmethod
    def price(self,amount):
        pass


class New_Dog(Dog):
    def price(self,amount):
        print("The", self.bread, "price is", amount, "thousand")


obj1 = New_Dog("Dollmansion")
obj1.price(30)