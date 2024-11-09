class House:
    def __init__(self, name, number_of_floors):
           self.name = name
           self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __iadd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors






obj_1 = House('ЖК Эльбрус', 10)
obj_2 = House('ЖК Акация', 20)
obj_1.__str__()
obj_2.__str__()
# print(len(obj_1))
# print(len(obj_2))
print(obj_1 == obj_2)
obj_1.__add__(10)
obj_1.__str__()
print(obj_1 == obj_2)
obj_1.__iadd__(10)
obj_2.__iadd__(10)
obj_1.__str__()
obj_2.__str__()
print(obj_1 < obj_2)
print(obj_1 <= obj_2)
print(obj_1 > obj_2)
print(obj_1 >= obj_2)
print(obj_1 != obj_2)
