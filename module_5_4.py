
class House:
    houses_history = {}
    houses_history_name = houses_history.keys()

    def __new__(cls, houses_name, name):
        cls.houses_history[houses_name] = name
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
         self.name = name
         self.number_of_floors = number_of_floors


    # def __del__(self):
    #    print(f'{self.name} снесён, но он останется в истории')


obj_1 = House('ЖК Эльбрус', 10)
print(list(House.houses_history_name))

obj_2 = House('ЖК Акация', 20)
print(list(House.houses_history_name))

obj_3= House('ЖК Матрёшки', 20)
print(list(House.houses_history_name))

# obj_1.__del__()
# print(list(House.houses_history_name))






