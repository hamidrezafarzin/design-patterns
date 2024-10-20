class Chair:
    def sit(self):
        pass

class Table:
    def use(self):
        pass

class HomeChair(Chair):
    def sit(self):
        print("sit on the home chair")

class HomeTable(Table):
    def use(self):
        print("Use Home table")

class OfficeChair(Chair):
    def sit(self):
        print("sit on the office chair")

class OfficeTable(Table):
    def use(self):
        print("Use office table")
        
class FurnitureFactory:
    def create_chair(self): pass
    def create_table(self): pass

class HomeFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return HomeChair()

    def create_table(self):
        return HomeTable()
    
class OfficeFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return OfficeChair()

    def create_table(self):
        return OfficeTable()


def create_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    chair.sit()
    table.use()



home_factory = HomeFurnitureFactory()
create_furniture(home_factory)

office_factory = OfficeFurnitureFactory()
create_furniture(office_factory)