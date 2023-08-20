class Vehicle:
    #default constructor
    def __init__(self, started = False, speed=0):
        self.started = started 
        self.speed = speed
        
    def start(self):
        self.started = True
        print("Car is started. Let us ride this...")
        
    def stop(self):
        self.speed = 0
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroom....")
        else:
            print("Please start the car first")
            
            
            
            
class Car(Vehicle):
    trunk_open = False
    
    def open_trunk(self):
        self.trunk_open = True 
        
    def close_trunk(self):
        self.trunk_open = False
        
        
        
class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
        
    def start(self, speed):
        if speed > 50:
            print("Vroom hahahah..")
        else:
            print("lets go bit slow")
        
       
            
            
            
            
M = Motorcycle()
M.center_stand_out = False
speed = 70
M.start(speed)

        
   
   
   
               
        
        
        