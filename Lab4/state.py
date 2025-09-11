from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class InSerivceState(State):
    def drive(self):
        return 'не может ездить в сервисе!'

    def park(self):
        return 'припарковалась в сервис'

    def refuel(self):
        return 'не может заправляться в сервисе!'

class OnRoadState(State):
    def drive(self):
        return 'едет по дороге'

    def park(self):
        return 'припарковалась'

    def refuel(self):
        return 'не может заправляться в дороге!'

class AtGasStationState(State):
    def drive(self):
        return 'едет по заправке'

    def park(self):
        return 'припарковалась на заправке'

    def refuel(self):
        return 'заправляется...'


class Car:
    def __init__(self, state):
        self._state = state

    def change_state(self, state):
        self._state = state

    def drive(self):
        self._execute('drive')

    def park(self):
        self._execute('park')

    def refuel(self):
        self._execute('refuel')

    def _execute(self, operation: str) -> None:
        func = getattr(self._state, operation)
        print('Машина {}.'.format(func()))

if __name__ == '__main__':
    car = Car(OnRoadState())
    car.drive()
    car.change_state(AtGasStationState())
    car.park()
    car.refuel()
    car.change_state(OnRoadState())
    car.drive()
    car.change_state(InSerivceState())
    car.park()
