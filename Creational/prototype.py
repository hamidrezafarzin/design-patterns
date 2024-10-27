import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        return f"ConcretePrototype with attribute: {self.attribute}"

# Client code
prototype = ConcretePrototype("Initial State")
clone = prototype.clone()
clone.attribute = "Changed State"

print(prototype)  # Output: ConcretePrototype with attribute: Initial State
print(clone)      # Output: ConcretePrototype with attribute: Changed State