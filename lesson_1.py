class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    number_of_wheels = 4
    counter = 0

    # contructor
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # object attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    number_of_wheels = 10
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}')
        else:
            print(f'Cargo of {type} was successfully loaded '
                  f'to {self.model} with weigth {weight}')


print(f'We need {Car.number_of_wheels * 10 * 5000} soms for winter lastics')
print(f"Was created {Car.counter} cars")

bmw_car = Car('BMW X7', 2020, 'Black')
print(bmw_car)
print(f'Model: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color} '
      f'penalties: {bmw_car.penalties}')
nissan_car = Car(the_color='Green', the_model='Nissan GTR',
                 the_year=2004, penalties=2500)
print(nissan_car)
print(f'Model: {nissan_car.model} year: {nissan_car.year} color: {nissan_car.color} '
      f'penalties: {nissan_car.penalties}')
# nissan_car.color = 'White'
nissan_car.change_color('White')
print(f'Model: {nissan_car.model} year: {nissan_car.year} '
      f'new color: {nissan_car.color} '
      f'penalties: {nissan_car.penalties}')
bmw_car.drive('Osh')
nissan_car.drive('Tokmok')

print(f"Was created {Car.counter} cars")

boeing_plane = Plane('Boeng 347', 2023, 'Blue')
print(f'Model: {boeing_plane.model} year: {boeing_plane.year} '
      f'new color: {boeing_plane.color}')

man_truck = Truck('Man 56', 1999, 'Red', 2400, 25000)
print(f'Model: {man_truck.model} year: {man_truck.year} '
      f'color: {man_truck.color} '
      f'penalties: {man_truck.penalties} '
      f'load capacity: {man_truck.load_capacity}')
man_truck.load_cargo('Potatos', 30000)
man_truck.load_cargo('Apples', 20000)
man_truck.drive('LA')

print(f'We need {Truck.number_of_wheels * 1 * 5000} soms for winter lastics for TRUCKS')