#Multiple inherit
class Brand:
    def model(self):
        print("Volvo V2E")

class Car:
    def model(self):
        print("Tesla")

class Launch(Brand, Car):
    def model(self):
        print("Out of Models")

obj = Launch()
obj.model()

#Multilevel
class Brand:
 def model(self):
        print("Volvo V2E")

class Car(Brand):
    def model(self):
        print("Tesla")

class Launch(Car):
    def model(self):
        print("Out of Models")

obj = Launch()
obj.model()
