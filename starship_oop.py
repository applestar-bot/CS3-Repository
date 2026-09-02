Class Starship:

    def__init__(self, base_weight, cargo_weight, final_fuel):
        self.base_weight = base_weight
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel

    def calculate_fuel(self):
        base_weight = 50000
        cargo_weight = 1000
    self.final_fuel =(self.base_weight + self.cargo_weight)* 3

    return self.final_fuel

starship = Starship(50000)
starship.load_cargo(1000)
starship.load_cargo(1000)
starship.load_cargo(1000)

starship.calculate_fuel()

