# test_abstract_factory.py
import pytest
from abstract_factory import (
    Car,
    Wolkswagen,
    Tesla,
    CarDealer,
    PetrolCarDealer,
    ElectricCarDealer
)

class TestWolkswagen:
    def test_wolkswagen_drive_method(self, capsys):
        car = Wolkswagen()
        car.drive()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Wolkswagen едет на бензине"

class TestTesla:
    def test_tesla_drive_method(self, capsys):
        car = Tesla()
        car.drive()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Tesla едет на электричестве"

class TestPetrolCarDealer:
    def test_petrol_car_dealer_buy_car_returns_wolkswagen(self):
        dealer = PetrolCarDealer()
        car = dealer.buyCar()
        assert isinstance(car, Wolkswagen)
        assert isinstance(car, Car)

    def test_petrol_car_dealer_buy_car_returns_new_instance_each_time(self):
        dealer = PetrolCarDealer()
        car1 = dealer.buyCar()
        car2 = dealer.buyCar()
        assert car1 is not car2
        assert isinstance(car1, Wolkswagen)
        assert isinstance(car2, Wolkswagen)

class TestElectricCarDealer:
    def test_electric_car_dealer_buy_car_returns_tesla(self):
        dealer = ElectricCarDealer()
        car = dealer.buyCar()
        assert isinstance(car, Tesla)
        assert isinstance(car, Car)

    def test_electric_car_dealer_buy_car_returns_new_instance_each_time(self):
        dealer = ElectricCarDealer()
        car1 = dealer.buyCar()
        car2 = dealer.buyCar()
        assert car1 is not car2
        assert isinstance(car1, Tesla)
        assert isinstance(car2, Tesla)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
