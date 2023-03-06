from abc import ABC, abstractmethod
from enum import Enum


class AnimalType(Enum):
    animal = 0
    bird = 1


class FoodType(Enum):
    hay = 0
    corn = 1


class Food:
    def __init__(self, type_: FoodType, quantity: int):
        self.type = type_
        self.quantity = quantity


class ProfitType(Enum):
    milk = 0
    meat = 1
    eggs = 2
    wool = 3
    feather = 4


class Profit:
    def __init__(self, type_: ProfitType, quantity: int):
        self.type = type_
        self.quantity = quantity


class Farm:

    def __init__(self):
        self.all_animals = []

    @property
    def animals(self):
        return [animal for animal in self.all_animals if animal.animal_type == AnimalType.animal]

    @property
    def birds(self):
        return [animal for animal in self.all_animals if animal.animal_type == AnimalType.bird]

    @property
    def animals_number(self):
        return len(self.animals)

    @property
    def birds_number(self):
        return len(self.birds)

    @property
    def food(self):
        return {FoodType.hay: sum([animal.food.quantity for animal in self.all_animals if animal.food.type == FoodType.hay]),
                FoodType.corn: sum([animal.food.quantity for animal in self.all_animals if animal.food.type == FoodType.corn])}

    @property
    def profit(self):
        return {ProfitType.milk: sum([animal.profit.quantity for animal in self.all_animals if animal.profit.type == ProfitType.milk]),
                ProfitType.meat: sum([animal.profit.quantity for animal in self.all_animals if animal.profit.type == ProfitType.meat]),
                ProfitType.eggs: sum([animal.profit.quantity for animal in self.all_animals if animal.profit.type == ProfitType.eggs]),
                ProfitType.wool: sum([animal.profit.quantity for animal in self.all_animals if animal.profit.type == ProfitType.wool]),
                ProfitType.feather: sum([animal.profit.quantity for animal in self.all_animals if animal.profit.type == ProfitType.feather]),
                }

    def print_statistics(self):
        print("==== RESULTS ====")
        print(f"Number of animals: {self.animals_number}")
        print(f"Number of birds: {self.birds_number}")
        print()
        print("Need food:")
        print(f"Hay: {self.food[FoodType.hay]}")
        print(f"Corn: {self.food[FoodType.corn]}")
        print()
        print("RECEIVE:")
        print(f"Milk: {self.profit[ProfitType.milk]}")
        print(f"Meat: {self.profit[ProfitType.meat]}")
        print(f"Eggs: {self.profit[ProfitType.eggs]}")
        print(f"Wool: {self.profit[ProfitType.wool]}")
        print(f"Feather: {self.profit[ProfitType.feather]}")


class Animal(ABC):
    def __init__(self, farm: Farm, name, animal_type: AnimalType, food: Food, profit: Profit):
        self.farm = farm
        self.name = name
        self.animal_type = animal_type
        self.food = food
        self.profit = profit
        self.farm.all_animals.append(self)


class Cow(Animal):
    def __init__(self, farm, name, hay, milk):
        super().__init__(farm, name, AnimalType.animal, Food(FoodType.hay, hay), Profit(ProfitType.milk, milk))


class Sheep(Animal):
    def __init__(self, farm, name, hay, wool):
        super().__init__(farm, name, AnimalType.animal, Food(FoodType.hay, hay), Profit(ProfitType.wool, wool))


class Pig(Animal):
    def __init__(self, farm, name, corn, meat):
        super().__init__(farm, name, AnimalType.animal, Food(FoodType.corn, corn), Profit(ProfitType.meat, meat))


class Chicken(Animal):
    def __init__(self, farm, name, corn, eggs):
        super().__init__(farm, name, AnimalType.bird, Food(FoodType.corn, corn), Profit(ProfitType.eggs, eggs))


class Duck(Animal):
    def __init__(self, farm, name, corn, feather):
        super().__init__(farm, name, AnimalType.bird, Food(FoodType.corn, corn), Profit(ProfitType.feather, feather))


if __name__ == '__main__':
    farm = Farm()
    cow1 = Cow(farm, 'cow1', 12, 54)
    cow2 = Cow(farm, 'cow2', 22, 24)

    sheep1 = Sheep(farm, 'sheep1', 23, 7)

    pig1 = Pig(farm, 'pig1', 12, 65)

    farm.print_statistics()
