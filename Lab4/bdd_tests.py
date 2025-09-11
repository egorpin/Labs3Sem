import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from state import Car, OnRoadState, AtGasStationState, InSerivceState

scenarios('features/car_behavior.feature')

@pytest.fixture
def car():
    return Car(OnRoadState())

@pytest.fixture
def context():
    return {'output': ''}

@given("автомобиль находится на дороге")
def car_on_road(car):
    car.change_state(OnRoadState())
    return car

@given("автомобиль находится на заправке")
def car_at_gas_station(car):
    car.change_state(AtGasStationState())
    return car

@given("автомобиль находится в сервисе")
def car_in_service(car):
    car.change_state(InSerivceState())
    return car

@when("я пытаюсь вести автомобиль")
def try_to_drive(car, context, capsys):
    car.drive()
    captured = capsys.readouterr()
    context['output'] = captured.out.strip()

@when("я пытаюсь припарковать автомобиль")
def try_to_park(car, context, capsys):
    car.park()
    captured = capsys.readouterr()
    context['output'] = captured.out.strip()

@when("я пытаюсь заправить автомобиль")
def try_to_refuel(car, context, capsys):
    car.refuel()
    captured = capsys.readouterr()
    context['output'] = captured.out.strip()

@when("я меняю состояние на заправку")
def change_to_gas_station(car):
    car.change_state(AtGasStationState())

@when("я меняю состояние на сервис")
def change_to_in_service(car):
    car.change_state(InSerivceState())

@then(parsers.parse("вывод должен содержать '{expected_text}'"))
def output_contains_expected_text(context, expected_text):
    assert expected_text in context['output'], f"Expected '{expected_text}' in output, but got: {context['output']}"
