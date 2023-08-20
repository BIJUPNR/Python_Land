class Car:
    #default constructor
    def __init__(self, started = False, speed=0):
        self.started = started 
        self.speed = speed
        
    def start(self):
        self.started = True
        print("Car is started. Let us ride this...")
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroom....")
        else:
            print("Please start the car first")
            
    def stop(self):
        self.speed = 0
        print("Halting the car")
        
        
        
        
car = Car()
car.increase_speed(40)
car.start()
car.increase_speed(50)

        
   
   
    