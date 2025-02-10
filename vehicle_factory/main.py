from VehicleFactory import VehicleFactory
from USVehicleFactory import USVehicleFactory
from EUVehicleFactory import EUVehicleFactory

if __name__ == "__main__":
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    # ТЗ для США
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # ТЗ для ЄС
    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale")

    eu_car.start_engine()
    eu_motorcycle.start_engine()
