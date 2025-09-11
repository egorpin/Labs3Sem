from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass

class Wolkswagen(Car):
    def drive(self):
        print('Wolkswagen едет на бензине')

class Tesla(Car):
    def drive(self):
        print('Tesla едет на электричестве')

class CarDealer(metaclass=ABCMeta):
    @abstractmethod
    def buyCar(self):
        pass

class PetrolCarDealer(CarDealer):
    def buyCar(self):
        return Wolkswagen()

class ElectricCarDealer(CarDealer):
    def buyCar(self):
        return Tesla()

if __name__ == '__main__':
    pcd = PetrolCarDealer()
    ecd = ElectricCarDealer()
    pcd.buyCar().drive()
    ecd.buyCar().drive()
