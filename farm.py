class Animal(object):
    def __init__(self, name):
        self.name = name
        self.truth = 1
    def __eq__(self, other):
        if (isinstance(other, Animal)):
            return True
        else:
            return False

class Pig(Animal):
    def __init__(self, name):
        self.name = name
        self.truth = 10
    def __eq__(self, other):
        if (isinstance(other, Animal)):
            return other.truth
        else:
            return False
class Sheep(Animal):
    def __init__(self, name):
        self.name = name
        self.truth = 2
    def __eq__(self, other):
        if (isinstance(other, Animal)):
            return other.truth
        else:
            return False 
class Horse(Animal):
    def __init__(self, name):
        self.name = name
        self.truth = 3
    def __eq__(self, other):
        if (isinstance(other, Animal)):
            return other.truth
        else:
            return False
#Main
snowball = Pig("snowball")
one = Sheep("one")
two = Sheep("two")
q = Animal("q")