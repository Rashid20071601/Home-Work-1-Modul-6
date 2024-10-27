# Родительский класс для животных
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        # Проверяем, съедобно ли растение
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Родительский класс для растений
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

# Наследуемый класс млекопитающих
class Mammal(Animal):
    pass

# Наследуемый класс хищников
class Predator(Animal):
    pass

# Класс цветов, наследуется от Plant
class Flower(Plant):
    pass

# Класс фруктов, наследуется от Plant, меняем edible
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Создаем объекты и выполняем действия
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)   # Волк с Уолл-Стрит
print(p1.name)   # Цветик семицветик
print(a1.alive)  # True
print(a2.fed)    # False

# Хищник пробует съесть цветок
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
# Млекопитающее пробует съесть фрукт
a2.eat(p2)       # Хатико съел Заводной апельсин

print(a1.alive)  # False
print(a2.fed)    # True