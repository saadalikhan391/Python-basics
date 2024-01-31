from OopsTest import Engine

class DriveCar(Engine):

    def car_model(self):
        print("Honda Model")

    def Drive_car(self):
        Engine.start_engine(self)
        Engine.stop_engine()

drive = DriveCar()
drive.car_model()
drive.Drive_car()
