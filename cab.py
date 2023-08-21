class Cab():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):       
        if not self.open_seats():
            return False 
        self.passengers.append(name)
        return True        
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    
    
    

cab1 = Cab(4)

people = ["Somu", "Raju", "Sudheer", "Ankit", "Ramesan"] 

for person in people:
    success = cab1.add_passenger(person)
    if success:
        print(f"Added {person} successfully")
    else:
        print(f"Seat not available for {person}")   
        
    