class Quote():
    def __init__(self, person, words):
        self.perosn = person
        self.words = words
    def who(self):
        return self.perosn
    def says(self):
        return self.words + '.'
    
class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'
#--------------------------------------
hunter = Quote('Elmer Fudd',"I'm hunting wabbits")
hunted1 = QuestionQuote('Bugs Bunny',"what's up, doc")
hunted2 = ExclamationQuote('Daffy Duck',"It's rabbit season")
#--------------------------------------
print(hunter.who(), 'says:', hunter.says())
print(hunted1.who(), 'says:', hunted1.says())
print(hunted2.who(), 'says:', hunted2.says())
#--------------------------------------
class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())
    
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)