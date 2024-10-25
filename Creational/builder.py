class House:
    def __init__(self):
        self.rooms = None
        self.windows = None
        self.roof = None

    def __str__(self):
        return f"House with {self.rooms} rooms, {self.windows} windows, and a {self.roof} roof."


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self 

    def set_windows(self, windows):
        self.house.windows = windows
        return self

    def set_roof(self, roof_type):
        self.house.roof = roof_type
        return self

    def build(self):
        return self.house



class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_simple_house(self):
        self.builder.set_rooms(1).set_windows(2).set_roof("simple")
        return self.builder.build()

    def construct_luxury_house(self):
        self.builder.set_rooms(5).set_windows(10).set_roof("luxury")
        return self.builder.build()



builder = HouseBuilder()
director = HouseDirector(builder)

simple_house = director.construct_simple_house()
print(simple_house)  

luxury_house = director.construct_luxury_house()
print(luxury_house)  
