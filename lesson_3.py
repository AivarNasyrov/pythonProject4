import enum

class Color(enum.Enum):
    WHITE = 1
    BLACK = 2
    DARK_YELLOW = 3
    RED = 4

class MusicPlayable:

    def play_music(self, song):
        print(f'Now is playing {song} song')

    def stop_music(self):
        print('Music stopped')


class Drawable:
    def draw(self, emoji):
        print(emoji)


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'{self.__model} is driving')

    def __str__(self):
        return f'Model: {self.__model} year: {self.__year} ' \
               f'color: {self.__color.name}'

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year < other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year


class FuelCar(Car):
    __total_fuel = 1000

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    @staticmethod
    def get_fuel_type():
        return 'AI - 95'

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'{self.model} is driving by using fuel')

    def __str__(self):
        return super().__str__() + f' fuel bank: {self.fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'{self.model} is driving by using electricity')

    def __str__(self):
        return super().__str__() + f' battery: {self.battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


my_car = Car('Nissan Pathfinder', 2000, Color.WHITE)
print(my_car)

bmw_car = FuelCar('MBW x6', 2009, Color.BLACK, 80)
print(bmw_car)

tesla_car = ElectricCar('Tesla Model S', 2023, Color.RED, 65000)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2022, Color.DARK_YELLOW, 50, 40000)
print(toyota_car)
toyota_car.drive()
print(HybridCar.mro())

num_1 = 9
num_2 = 7
print(f'Is number one bigger than number two? {num_1 > num_2}')
print(f'Is bmw car fresher than toyota car? {bmw_car > toyota_car}')
print(f'Is bmw car same year with toyota car? {bmw_car == toyota_car}')
print(bmw_car + toyota_car)
print(str(FuelCar.get_total_fuel()) + ' ' + FuelCar.get_fuel_type())
toyota_car.play_music('Yesterday')

samsung_phone = SmartPhone()
samsung_phone.play_music('Any')
samsung_phone.stop_music()
samsung_phone.draw('📱')
toyota_car.draw('🚗')

if toyota_car.color == Color.DARK_YELLOW:
    print('The car is beautiful')