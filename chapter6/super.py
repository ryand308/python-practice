# cuper()

class Person():
    def __init__(self,name):
        self.name = name+"-is my best friend"
        
class EmailPerson(Person):
    def __init__(self, name, email):

        super().__init__(name)

        self.email = email
        
bob = EmailPerson("Bob Frapples","bob@frapples.com")

print(bob.name)
print(bob.email)

