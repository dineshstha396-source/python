#class and object example
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} Dog is sitting.")
    def roll(self):
        print(f"{self.name} Dog is rolling.")


dog1=Dog("Dinesh",19)
print(dog1.name)
dog1.sit()
dog1.roll()


class Car():
    def __init__(self,brand,year,model):
        self.brand=brand
        self.year=year
        self.model=model

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.brand+' '+self.model
        return long_name.title()
car1=Car("tesla",2007,"electric")
print(car1.get_descriptive_name())
        
    