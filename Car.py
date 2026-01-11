class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def show_details(self):
        print("Car Details")
        print("-----------")
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Year  :", self.year)
        print("Price : Rs.", self.price)


if __name__ == "__main__":
    car = Car("Toyota", "Innova", 2022, 2500000)
    car.show_details()