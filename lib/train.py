class Train():
    def __init__(self, colour):
        self.wheels = 8
        self.colour = colour
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)