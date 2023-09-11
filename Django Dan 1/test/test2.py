
"""
Klasa za opisivanje auta.
"""

class Car():

    def __init__(self,fuel,brand,power):
        self.fuel = fuel
        self.brand = brand
        self.power = power
        
    def refuel(self,fuel):
        self.fuel += fuel
    
    def __str__(self):
        return 'Fuel:' + self.fuel + ' Brand: ' + self.brand + ' Power: ' + str(self.power)

volvo = Car('benzin','volvo',200)
print(volvo)