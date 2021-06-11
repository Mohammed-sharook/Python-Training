# inheritance is the procedure of which one class inherits the attributes and methods of another class
# Main thing is along with the inherit properties from parent class the child class has its own methods and properties


class McLaren:    # parent class
    def __init__(self, type, millage, speed ):
        self.type = type
        self.millage = millage
        self.speed = speed

    def about(self):
        return f' This is a "{self.type}" it gives millage of "{self.millage}" and it goes speed upto "{self.speed}"'


class BMW(McLaren):   # child class
    pass              # with same properties and methods of parent class


class RangeRover(McLaren):  # child class

    def specification(self, name):  # Has its own methods
        return f" {name} is a type of both racing and trucking "


obj = BMW("Racing car", "12km/lr", "250km/hr")
print(obj.about())

print()

obj1 = RangeRover("racecar", "10km/lr", "220kkm/hr")
print(obj1.specification("RangeRover"))
print(obj1.about())