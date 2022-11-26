class ElectronicDevice:

    def __init__(self, weight, colour):
        self.weight = weight
        self.colour = colour


class Computer(ElectronicDevice):
    def __init__(self, wireless, weight, colour):
        self.wireless = wireless
        ElectronicDevice.__init__(self, weight, colour)

        


class TV(ElectronicDevice):
    def __init__(self, smart, weight, colour):
        ElectronicDevice.__init__(self, weight, colour)
        self.smart = smart


class Desktop(Computer):
    def __init__(self, weight, colour, wireless=False):
        Computer.__init__(self, weight, colour)


class Laptop(Computer):
    def __init__(self, weight, colour, wireless=False):
        Computer.__init__(self, weight, colour)