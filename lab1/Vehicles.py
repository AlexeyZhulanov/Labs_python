from abc import ABC, abstractmethod


class Vehicles(ABC):
    average_load_capacity: int

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.model = model
        self.weight = weight
        self.consumption = consumption
        self.tank_capacity = tank_capacity

    @abstractmethod
    def PowerReserve(self):
        return f' запас хода {self.model}: {self.tank_capacity / self.consumption * 100} километров'

    @abstractmethod
    def CityDriving(self):
        if self.weight < 2000:
            return f'{self.model} может ездить по городу'
        else:
            return f'{self.model} не может ездить по городу'

    @abstractmethod
    def Print(self):
        pass


class Car(Vehicles):
    average_load_capacity: int = 450

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Car"
        super().__init__(model, weight, consumption, tank_capacity)

    def PowerReserve(self):
        return super().PowerReserve()

    def CityDriving(self):
        return super().CityDriving()

    def Print(self):
        return f"Printing Car with model: {self.model}, weight: {self.weight}, consumption: {self.consumption} and tank_capacity: {self.tank_capacity}"


class Gazelle(Vehicles):
    average_load_capacity: int = 2140

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Gazelle"
        super().__init__(model, weight, consumption, tank_capacity)

    def PowerReserve(self):
        return super().PowerReserve()

    def CityDriving(self):
        return super().CityDriving()

    def Print(self):
        return f"Printing Gazelle with model: {self.model}, weight: {self.weight}, consumption: {self.consumption} and tank_capacity: {self.tank_capacity}"


class Kamaz(Vehicles):
    average_load_capacity: int = 8000

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Kamaz"
        super().__init__(model, weight, consumption, tank_capacity)

    def PowerReserve(self):
        return super().PowerReserve()

    def CityDriving(self):
        return super().CityDriving()

    def Print(self):
        return f"Printing Kamaz with model: {self.model}, weight: {self.weight}, consumption: {self.consumption} and tank_capacity: {self.tank_capacity}"


class Truck(Vehicles):
    average_load_capacity: int = 20000

    def __init__(self, model: str, weight: int, consumption: int, tank_capacity: int):
        self.name = "Truck"
        super().__init__(model, weight, consumption, tank_capacity)

    def PowerReserve(self):
        return super().PowerReserve()

    def CityDriving(self):
        return super().CityDriving()

    def Print(self):
        return f"Printing Truck with model: {self.model}, weight: {self.weight}, consumption: {self.consumption} and tank_capacity: {self.tank_capacity}"


class Belaz(Vehicles):
    average_load_capacity: int = 300000

    def __init__(self, model: str, weight: int, height: int, consumption: int, tank_capacity: int):
        self.name = "Belaz"
        super().__init__(model, weight, consumption, tank_capacity)
        self.height = height

    def PowerReserve(self):
        return super().PowerReserve()

    def CityDriving(self):
        return super().CityDriving()

    def Print(self):
        return f"Printing Belaz with model: {self.model}, weight: {self.weight}, height: {self.height}, consumption: {self.consumption} and tank_capacity: {self.tank_capacity}"