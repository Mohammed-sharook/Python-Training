# In OOPS, polymorphism refers to functions which has same name but different functionalities

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def sounds_like(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def sounds_like(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.sounds_like()
    animal.about()
    print()