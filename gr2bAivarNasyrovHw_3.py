class Computer:
    def __init__(self, cpu, memory):
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
        return(self.__memory * self.__cpu)


    def __str__(self):
        return f'memory : {self.memory}, cpu: {self.cpu}'


    def __gt__(self, other):
        return self.memory > other.memory


    def __ge__(self, other):
        return self.memory >= other.memory


    def __lt__(self, other):
        return self.memory < other.memory


    def __le__(self, other):
        return self.memory <= other.memory


    def __eq__(self, other):
        return self.memory == other.memory


    def __ne__(self, other):
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
        return(f'“Идет звонок на номер {call_to_number}” с сим-карты-{sim_card_number} - '
              f'{self.__sim_cards_list[sim_card_number - 1]}')

    def __str__(self):
        return f'Список сим-кард: {self.sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        return(f'Маршрут до {location} построен')

computer = Computer("Intel", 256)
phone = Phone(['O', "Mega"])
smartphone_1 = SmartPhone(16, 128, ['O', "Mega"])
smartphone_2 = SmartPhone(16, 64, ['O', "Mega"])
print(smartphone_1.use_gps("TCUM"))
list_1 = [smartphone_1, smartphone_2, phone, computer]
for i in list_1:
    print(i)
    

