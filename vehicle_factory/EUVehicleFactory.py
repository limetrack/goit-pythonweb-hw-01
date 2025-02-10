from VehicleFactory import VehicleFactory
from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} {model}", "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} {model}", "EU Spec")
