""""
Amelia Cortez
ClassVehicle.py
This program will ask the user to input details about their car.
It will then display the details
""" 

class Vehicle:
    def __init__(self,vehicle):
        #Initialize attributes to Vehicle
        self.vehicle = vehicle
        

class Automobile(Vehicle):
    # Represents aspects of a vehicle, speficially car/automobile
    def __init__(self,year, make, model, doors, roof):
        # Initialize attributes to automobile
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        super().__init__('car') #Select type of vehicle
    
    @classmethod   
    def car_details(cls):
        # User input and validation
        print("Please enter car details:")
        
        while True:
            print('What year is your car')
            year = input()
            try:
                year = int(year)
            except:
                print('Please enter a valid year(YYYY)')
                continue
            if year < 1920 or year > 2024:
                print('Please enter a valid year in format YYYY')
                continue
            break
    
        make = input('What make is your car: ')    
        model = input('What model is your car: ')
            
        while True:
            doors = input("Doe your car have 2 or 4 doors: ")
            if doors in ('2', '4'):
                doors = int(doors)
                break
            else:
                print("Please enter if your car has 2 or 4 doors. Please enter '2' or '4'")
            
        while True:
            roof = input("Is your car roof solid or does it have a sunroof: ").lower()
            if roof in ('solid', 'sunroof'):
                break
            else:
                print("Does your car have a sunroof or is it a solid roof(No window on roof). Please enter 'sunroof' or 'solid'")
            
        return cls(year, make, model, doors, roof)
    
def main():
 # Print/display user input  
    car = Automobile.car_details()
          
    print(f'Vehicle type: {car.vehicle}')
    print(f'Year: {car.year}')
    print(f'Make: {car.make}')
    print(f'Model: {car.model}')
    print(f'Number of doors: {car.doors}')
    print(f'Type of roof: {car.roof}')
        
if __name__ == "__main__":
    main()
        
        
                
            
        
        
        
        
    
        
