class car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.__year=year
        self.__color=color
    def get_year(self):
        return self.__year
    def get_color(self):
        return self.__color
car=car("Auto","sport",2026,"red")
print(car.make,car.model,car.get_year(),car.get_color())