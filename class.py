#functions in python
def add(a,b):
    return a+b
print(add(10,20))

#class in python
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    def start(self):
        return "Car is starting"
    def stop(self):
        return "Car is stopping"

maruti=Car("Maruti","Swift",2020)
print(maruti.get_info())
print(maruti.start())
print(maruti.stop())
bmw=Car("BMW","X5",2021)
print(bmw.get_info())

