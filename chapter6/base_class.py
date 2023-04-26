# 繼承 inherit: parent, superclass, base class & child, subclass, derived class
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_car = Car()
give_me_yugo = Yugo()

give_me_car.exclaim()
give_me_yugo.exclaim()

#copy(duplicate) method
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_yugo = Yugo()
yugo = give_me_yugo.exclaim()

#add(extra) method
class Yugo(Car):
    def need_a_push(self):
        print("A little help here?")

give_me_yugo = Yugo()
give_me_yugo.need_a_push()

#self
car = Car()
car.exclaim()
Car.exclaim(car)
'''
class Car():
    def exclaim(self):
        print("I am a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

give_me_car = Car()

give_me_yugo = Yugo()

give_me_car.exclaim()
give_me_yugo.need_a_push()

#give_me_car.need_a_push()  AttributeError

'''