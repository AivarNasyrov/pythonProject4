def init(self, cpu, memory):
    self.__cpu = cpu
    self.__memory = memory


@property
def cpu(self):
    return self.__cpu


@cpu.setter
def cpu(self, value):
    self.__cpu = value


@property
def memory(self):
    return self.__memory


@memory.setter
def memory(self, value):
    self.__memory = value


def make_computations(self):
    print(self.__memory * self.__cpu)


def __str(self):
    return f'memory : {self.memory}, cpu: {self.cpu}'


def gt(self, other):
    return self.memory > other.memory


def ge(self, other):
    return self.memory >= other.memory


def lt(self, other):
    return self.memory < other.memory


def le(self, other):
    return self.memory <= other.memory


def eq(self, other):
    return self.memory == other.memory


def ne(self, other):
    return self.memory != other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'“Идет звонок на номер {call_to_number}” с сим-карты-{sim_card_number} - '
              f'{self.__sim_cards_list[sim_card_number - 1]}')

    def __str(self):
        return f'Список сим-кард: {self.sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        print(f'Маршрут до {location} построен')