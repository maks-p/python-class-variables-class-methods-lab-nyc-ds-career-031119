class Driver:

    _all = []
    _count = 0

    def __init__(self, name, car_make, car_model):
        self.name = name
        self.car_make = car_make
        self.car_model = car_model
        Driver._all.append(self)
        Driver._count += 1

    def get_driver(self):
        return f"{self.name} drives a {self.car_make} {self.car_model}."

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        return [driver.name for driver in cls._all]

    @classmethod
    def car_makes(cls):
        return [driver.car_make for driver in cls._all]

    @classmethod
    def car_models(cls):
        return [driver.car_model for driver in cls._all]

    @classmethod
    def fleet_makes_count(cls):
        make_count_dict = {}
        for driver in cls._all:
            make_count_dict[driver.car_make] = make_count_dict.get(driver.car_make, 0) + 1
        return make_count_dict
    
    @classmethod
    def fleet_models_count(cls):
        model_count_dict = {}
        for driver in cls._all:
            model_count_dict[driver.car_model] = model_count_dict.get(driver.car_model, 0) + 1
        return model_count_dict

    @classmethod
    def percent_of_fleet(cls, car_make):
        percent = cls.fleet_makes_count()[car_make] / cls._count
        return f"{100 * percent}%"

helga = Driver("Helga Pataki", "Toyota", "Camry")
arnold = Driver("Arnold Shortman", "Toyota", "Highlander")
gerald = Driver("Gerald Johanssen", "Toyota", "Camry")
robert = Driver("Robert 'Big Bob' Pataki", "Honda", "Pilot")
grandpa = Driver("Grandpa Phil", "Jeep", "Grand Cherokee")
rhonda = Driver("Rhonda Wellington Lloyd", "Kia", "Sonata")
phoebe = Driver("Phoebe Heyerdahl", "Honda", "Civic")

print(Driver.fleet_size())
print(Driver.driver_names())
print(Driver.car_makes())
print(Driver.car_models())
print(Driver.fleet_makes_count())
print(Driver.fleet_models_count())
print(Driver.percent_of_fleet("Toyota"))
