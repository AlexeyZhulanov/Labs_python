from abc import ABC, abstractmethod


class Vehicles(ABC):
    average_load_capacity: int

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.model = model
        self.weight = weight
        self.consumption = consumption
        self.tank_capacity = tank_capacity

    def __repr__(self) -> str:
        return f'Printing <\'{self.__class__.__name__}\' model: {self.model}, weight: {self.weight}, consumption: {self.consumption}, tank_capacity: {self.tank_capacity}>'

    @abstractmethod
    def power_reserve(self):
        return f' запас хода {self.model}: {self.tank_capacity / self.consumption * 100} километров'

    @abstractmethod
    def city_driving(self):
        if self.weight < 2000:
            return f'{self.model} может ездить по городу'
        else:
            return f'{self.model} не может ездить по городу'


class Car(Vehicles):
    average_load_capacity: int = 450

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Car"
        super().__init__(model, weight, consumption, tank_capacity)

    def power_reserve(self):
        return super().power_reserve()

    def city_driving(self):
        return super().city_driving()


class Gazelle(Vehicles):
    average_load_capacity: int = 2140

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Gazelle"
        super().__init__(model, weight, consumption, tank_capacity)

    def power_reserve(self):
        return super().power_reserve()

    def city_driving(self):
        return super().city_driving()


class Kamaz(Vehicles):
    average_load_capacity: int = 8000

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Kamaz"
        super().__init__(model, weight, consumption, tank_capacity)

    def power_reserve(self):
        return super().power_reserve()

    def city_driving(self):
        return super().city_driving()


class Truck(Vehicles):
    average_load_capacity: int = 20000

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Truck"
        super().__init__(model, weight, consumption, tank_capacity)

    def power_reserve(self):
        return super().power_reserve()

    def city_driving(self):
        return super().city_driving()


class Belaz(Vehicles):
    average_load_capacity: int = 300000

    def __init__(self, model: str, weight: int, height: int, consumption: int, tank_capacity: int):
        self.name = "Belaz"
        super().__init__(model, weight, consumption, tank_capacity)
        self.height = height

    def power_reserve(self):
        return super().power_reserve()

    def city_driving(self):
        return super().city_driving()

    def __repr__(self) -> str:
        return f'Printing <\'{self.__class__.__name__}\' model: {self.model}, weight: {self.weight}, height: {self.height},consumption: {self.consumption}, tank_capacity: {self.tank_capacity}>'
