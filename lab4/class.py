'''class cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name 
        self.afe = age
        self.isHappy = isHappy


cat1 = cat()
cat1.set_data("mamu",13,True)
print(cat1.name)'''

#конструктор 
class Building:
    year = None
    city = None

    def __init__(self,year,city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:",self.year,"City: ",self.city)


class School(Building):
    puple = 0
    def __init__(self,puples, year, city):
        super(School,self).__init__(year,city)
        self.puple = puples




school = School(100,2000,"Atu")
school.get_info()
house = Building(2000,"Atu")
shop = Building(2000,"Atu")