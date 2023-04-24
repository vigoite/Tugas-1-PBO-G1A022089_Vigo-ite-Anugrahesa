class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def get_make(self):
    return self.make

  def get_model(self):
    return self.model

  def get_year(self):
    return self.year

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_make()) # "Toyota"
print(my_car.get_model()) # "Corolla"
print(my_car.get_year()) # 2020
