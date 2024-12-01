class Plant:
    edible = False

    def __init__(self, name_plant):
        self.name_plant = name_plant

class Flower(Plant):
    def __init__(self, name_plant):
         super().__init__(name_plant)

class Fruit(Plant):
    def __init__(self, name_plant):
         super().__init__(name_plant)
    edible = True


class Animal:
    alive = True
    fed = False

    def __init__(self, name_animal):
        self.name_animal = name_animal

class Mammal(Animal):
    def __init__(self, name_animal):
        super().__init__(name_animal)

class Predator(Animal):
    def __init__(self, name_animal):
        super().__init__(name_animal)

    def eat(self, food):
        self.food = Plant()

        if food.edible == True:
             print(f'{self.name_animal} не стал есть {self.food.name_plant}')
             self.alive = False

        else:
            print(f'{self.name_animal} съел {self.food.name_plant}')
            self.fed = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name_animal)
print(p1.name_plant)

print(a1.alive)
print(a1.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)



