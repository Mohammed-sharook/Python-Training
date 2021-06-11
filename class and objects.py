class HumanBeing:
    Nationality = "Indian"
    Nature_behaviour = "Eating" # universal/ class attributes.

    def __init__(self, color, language):    # constructor method
        self.color = color     # instance attributes
        self.language = language

    def charecter(self,color):      # class / instance method
        return f"The common thing between {color} and {self.color} people is {self.Nature_behaviour}"

    def speak(self,num_language):   # class method
        return f"people from {self.Nationality} counties can speak multiple languages more than  {num_language}"


obj = HumanBeing("black", "English")     # we can create multiple objects for same class
print(obj.charecter("white"))
print(obj.speak(3))