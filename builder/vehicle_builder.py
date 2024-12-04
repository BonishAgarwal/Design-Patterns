from base import Vehicle


class VehicleBuilder:
    def __init__(self):
        self.color = "White"
        self.wheels = "4"
        self.seats = "5"
        self.gears = "5"
    
    def set_color(self, color):
        self.color = color
        return self # Return the builder object to allow method chaining
    
    def set_wheels(self, wheels):
        self.wheels = wheels
        return self
    
    def set_seats(self, seats):
        self.seats = seats
        return self
    
    def set_gears(self, gears):
        self.gears = gears
        return self
    
    def build(self):
        return Vehicle(
            self.color,
            self.wheels,
            self.seats,
            self.gears
        )