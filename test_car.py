from Car import Car

def test_car_attributes():
    car = Car("Toyota", "Innova", 2022, 2500000)
    assert car.brand == "Toyota"
    assert car.model == "Innova"
    assert car.year == 2022
    assert car.price == 2500000
