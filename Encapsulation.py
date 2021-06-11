# Encapsulation is a way of hiding data ,it puts restriction on accessing the variables and methods

# protect attributes and methods using (_) before their names such as ---> self._name
# It cannot be accessed outside the class.

class Employee:
    def __init__(self):
        self._password = "123456"


class Details(Employee):
    def __init__(self):
        Employee.__init__(self)
        print("The Employee password is",self._password)


obj = Employee()
print(obj._password) # direct access the protected attribute
print(obj.password)  # It gives attribute error i we try to access it --->/
# ( but we can still access this by calling as usual how they are defined )


obj1 = Details()  # This will give the protected attribute because it is called inside the sub_class

# Actual way to protect the data or methods and attribute is using (__) before the fun name or attributes
# 'Private member" it cannot be accessed outside the class and also inside the sub_class


class Employee:
    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def access(self):
        return f"The password can only access through inside the scope of class {self.__password}"


obj3 = Employee("sha@gmail",12345)
print(obj3.access())
print(obj3.email)
print(obj3.__password)  # This will gives an attribute error

