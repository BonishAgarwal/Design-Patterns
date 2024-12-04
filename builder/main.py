from vehicle_builder import VehicleBuilder


def main():
    
    custom_car = VehicleBuilder().set_color("Black").set_gears("6").set_wheels("2")
    
    car = custom_car.build()
    
    print(car.wheels)
    
if __name__ == "__main__":
    main()