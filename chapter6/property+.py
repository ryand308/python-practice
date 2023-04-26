class Duck():
    def __init__(self, input_name):
        self.hidden_name=input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.hidden_name=input_name

fowl = Duck('Howard')
print(fowl.name)

fowl.name= "Donald"
print(fowl.name)
#-----------------------------------------

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2*self.radius
    @diameter.setter
    def diameter(self, radius):
        print("The radius: ")
        self.radius = radius/2
c= Circle(5)
print(c.radius)
print(c.diameter)

c.diameter=10
print(c.radius)
print(c.diameter)