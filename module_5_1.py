class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

        def go_to(new_floor):
            if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")

        go_to(new_floor)

new_floor = int(input("введите номер этажа ",))
House('ЖК Горский', 18)
