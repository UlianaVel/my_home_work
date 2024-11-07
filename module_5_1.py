class House:
    def __init__(self, name, number_of_floors):
           self.name = name
           self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
               print("Такого этажа не существует")
        else:
               i = 1
               while i < int(self.new_floor)+1:
                     print(i)
                     i +=1


obj = House('ЖК Горский', 18)
obj.go_to(int(input("введите номер этажа ",)))


