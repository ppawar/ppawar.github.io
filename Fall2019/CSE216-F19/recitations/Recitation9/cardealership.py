class Car:
    def __init__(self, id, brand, price, attributes):
        self.id = id
        self.brand = brand
        self.price = price
        self.attributes = attributes

    def __repr__(self):
        attr = self.attributes
        return '\tCar: [ <' + str(self.id) + '> ' + str(self.brand) + \
                         ' - ' + str(self.price) + str(attr) + ' ]'

    def __eq__(self, other):
        return self.id == other.id and self.brand == other.brand and \
               self.price == other.price and \
               self.attributes.paint == other.attributes.paint and \
               self.attributes.tires == other.attributes.tires and \
               self.attributes.trim == other.attributes.trim

    def __lt__(self, other):
        return self.id < other.id


class CarAttributes:
    def __init__(self, paint, tires, trim):
        self.paint = paint
        self.tires = tires
        self.trim = trim

    def __repr__(self):
        return ' - Attributes: [' + str(self.paint) + ' - ' + \
               str(self.tires) + ' - ' + str(self.trim) + ']'


class Dealership:
    def __init__(self, car_list, name):
        self.car_list = car_list
        self.name = name

    def __repr__(self):
        string = self.name + ': \n'
        for i in self.car_list:
            string += str(i) + '\n'
        return string

    def add_cars(self, cars):
        for car in cars:
            newcar = Car(car[0], car[1], car[2], CarAttributes(car[3], car[4], car[5]))
            self.car_list.append(newcar)
        return None

    def update_car(self, id, new_value):
        for car in self.car_list:
            if id == car.id:
                print("There is a car")
                carFound = True
                # Change param value
                detail = new_value[0]
                if detail == 'brand':
                    car.brand = new_value[1]
                elif detail == 'price':
                    car.price = new_value[1]
                elif detail == 'paint':
                    car.attributes.paint = new_value[1]
                elif detail == 'tires':
                    car.attributes.tires = new_value[1]
                elif detail == 'trim':
                    car.attributes.trim = new_value[1]
                return "Updated"
        return "Car not found"


# You do not need to modify this function, but see what it does though.
def reset_cars():
    global car1, car2, car3, car4, car5, car6, car7, car8, car9, dealership1, dealership2, dealership3
    car1 = Car(1, 'Ford', 23000, CarAttributes('Red', 'Rain', 'Level-1'))
    car2 = Car(2, 'BMW', 46000, CarAttributes('Blue', 'Regular', 'Regular'))
    car3 = Car(3, 'Ferrari', 150000, CarAttributes('Violet', 'Regular', 'Level-2'))
    car4 = Car(4, 'Toyota', 26000, CarAttributes('Black', 'Snow', 'Regular'))
    car5 = Car(5, 'BMW', 50000, CarAttributes('Red', 'Sport', 'Level-3'))
    car6 = Car(6, 'Lotus', 50000, CarAttributes('Grey', 'Sport', 'Regular'))
    car7 = Car(7, 'Audi', 40000, CarAttributes('Blue', 'Regular', 'Level-2'))
    car8 = Car(8, 'Audi', 45000, CarAttributes('Blue', 'Rain', 'Regular'))
    car9 = Car(9, 'Ford', 30000, CarAttributes('Violet', 'Sport', 'Level-1'))

    dealership1 = Dealership([car1, car2, car3], 'KMac')
    dealership2 = Dealership([car4, car5, car6, car7], 'JRM')
    dealership3 = Dealership([car8, car9], 'ALee')


# global variables
car1 = car2 = car3 = car4 = car5 = car6 = car7 = car8 = car9 = dealership1 = dealership2 = dealership3 = None



# Testing...
#
def main():
    # Reset the values to start with the known starting point.
    reset_cars()

    # Testing Part 2.
    p1List = [[11, 'Mercedes', 40000, 'Grey', 'Snow', 'Regular'],
              [12, 'Ford', 20000, 'Red', 'Rain', 'Level-1']
              ]
    p2List = []
    p3List = [
        [13, 'Mercedes', 40000, 'Grey', 'Snow', 'Regular'],
        [14, 'Mercedes', 40000, 'Blue', 'Snow', 'Regular'],
        [15, 'Mercedes', 40000, 'Orange', 'Snow', 'Regular']
    ]
    dealership1.add_cars(p1List)
    print('Testing add_cars() for cars = p1List: \n' + str(dealership1))


    #Testing Task 1.
    reset_cars()
    dealership2.add_cars(p2List)
    print('Testing add_cars() for cars = p2List: \n' + str(dealership2))
    reset_cars()
    dealership3.add_cars(p3List)
    print('Testing add_cars() for cars = p3List: \n' + str(dealership3))
    reset_cars()
    print()

    # Testing Task 2.
    print('Testing update_car() for id = 1, newValue = ("brand", "Hyundai") : ' + str(
        dealership1.update_car(1, ('brand', 'Hyundai'))))
    print(dealership1)
    print()
    reset_cars()
    print('Testing update_car() for id = 100, newValue = ("paint","Red"): ' + str(
        dealership2.update_car(100, ('paint', 'Red'))))
    print(dealership2)
    print()
    reset_cars()
    print('Testing update_car() for id = 8, newValue = ("trim", "Level-1"): ' + str(
        dealership3.update_car(8, ("trim", "Level-1"))))
    print(dealership3)
    print()
    reset_cars()
    print()


if __name__ == '__main__':
    main()
