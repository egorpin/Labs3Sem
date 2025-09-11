# features/car_behavior.feature
Feature: Car Behavior in Different States
  As a car owner
  I want my car to behave differently in different states
  So that I can manage car operations appropriately

  Scenario: Driving behavior when car is on road
    Given автомобиль находится на дороге
    When я пытаюсь вести автомобиль
    Then вывод должен содержать 'едет по дороге'

  Scenario: Driving behavior when car is at gas station
    Given автомобиль находится на заправке
    When я пытаюсь вести автомобиль
    Then вывод должен содержать 'едет по заправке'

  Scenario: Driving behavior when car is in service
    Given автомобиль находится в сервисе
    When я пытаюсь вести автомобиль
    Then вывод должен содержать 'не может ездить в сервисе'

  Scenario: Parking behavior when car is on road
    Given автомобиль находится на дороге
    When я пытаюсь припарковать автомобиль
    Then вывод должен содержать 'припарковалась'

  Scenario: Parking behavior when car is at gas station
    Given автомобиль находится на заправке
    When я пытаюсь припарковать автомобиль
    Then вывод должен содержать 'припарковалась на заправке'

  Scenario: Parking behavior when car is in service
    Given автомобиль находится в сервисе
    When я пытаюсь припарковать автомобиль
    Then вывод должен содержать 'припарковалась в сервис'

  Scenario: Refueling behavior when car is on road
    Given автомобиль находится на дороге
    When я пытаюсь заправить автомобиль
    Then вывод должен содержать 'не может заправляться в дороге'

  Scenario: Refueling behavior when car is at gas station
    Given автомобиль находится на заправке
    When я пытаюсь заправить автомобиль
    Then вывод должен содержать 'заправляется'

  Scenario: Refueling behavior when car is in service
    Given автомобиль находится в сервисе
    When я пытаюсь заправить автомобиль
    Then вывод должен содержать 'не может заправляться в сервисе'

  Scenario: State transition from road to gas station
    Given автомобиль находится на дороге
    When я меняю состояние на заправку
    And я пытаюсь заправить автомобиль
    Then вывод должен содержать 'заправляется'

  Scenario: State transition from gas station to service
    Given автомобиль находится на заправке
    When я меняю состояние на сервис
    And я пытаюсь вести автомобиль
    Then вывод должен содержать 'не может ездить в сервисе'
