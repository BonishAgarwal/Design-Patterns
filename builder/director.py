from vehicle_builder import VehicleBuilder


class CarDirector:
    
    def __init__(self, builder: VehicleBuilder):
        self.builder = builder
    
    def build_car(self):
        custom_car = self.builder.set_color("Red").set_gears("2")
        return custom_car