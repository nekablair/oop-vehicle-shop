# os.system('cls' if os.name == 'nt' else 'clear')  #clearing the terminal no matter your os
#remember to use ---if isinstance
class CarManager:
    total_cars = 0
    all_cars = []

    def __init__(self, make, model, year, mileage, services = None): #<---constructor function that happens everytime we update cars
        #update total_cars and create id for this car
        self._id = CarManager.total_cars
        CarManager.total_cars += 1
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []
        
        #update all_cars
        CarManager.all_cars.append(self)

    def __str__(self):
        return f"ID {self._id} | Make {self._make} | Model {self._model} | Year {self._year} | Mileage {self._mileage} | Services {self._services}"
    
    def __repr__(self):
        return str(self)

    # def __init__(self, id, make, model, year, mileage, services): #<-- don't do this because we want to be able to control the id and not have the user change it
    #     self._id = id
    #     self._make = make
    #     self._model = model
    #     self._year = year
    #     self._mileage = mileage
    #     self._services = services

    def terminal():
        print("---- WELCOME ----")
        print("1. Add Car")
        print("2. View all cars")
        print("3. View total number of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit")
        CarManager.user_input()


    def user_input():
        run = True
        while run == True:
            option = input("Enter choice: ")
            if option == "1":
                make = input("Add Make: ")
                model = input("Add Model: ")
                year = input("Add Year: ")
                mileage = input("Add Mileage: ")
                new_car = CarManager(make, model, year, mileage)
                print(new_car)
                print(CarManager.all_cars)
                CarManager.terminal()
            elif option == "2":
                print(CarManager.all_cars)
                CarManager.terminal()
            elif option == "3":
                print(f" Total Cars: {CarManager.total_cars}")
                CarManager.terminal()
                #some logic isn't right, when picking anything other then 0, it errors out, thinking, it isn't inputting it as an actual list
            elif option == "4":
                user_id_choice = int(input("Enter car id please : "))
                for car in CarManager.all_cars:
                    if user_id_choice == car._id :
                        print(type(user_id_choice)
                        print(f"ID: {car._id}, MAKE: {car._make}, MODEL: {car._model}, YEAR: {car._year}, MILEAGE: {car._mileage}, SERVICES: {car._services}")
                        CarManager.terminal()
                    else:
                        print("That car id is not in the inventory, choose another id.")
                        CarManager.terminal()
            elif option == "5":
                print(car._id)
                user_id_choice = int(input("Enter car id please : "))
                for car in CarManager.all_cars:
                    if user_id_choice == car._id :
                        car_services_from_user = input("Add the services you want: ")
                        print(car_services_from_user) #<built-in function id> error in terminal
                        car._services.append(car_services_from_user)
                        print(f"Car services you've requested : {car._services}")
                    else:
                        print("That's not the right car id")
                CarManager.terminal()
            if option == "6":
                CarManager.update_mileage_car()
            if option == "7":
                print("Quitting... thank you for using Car Manager!")
                run = False
                
    #attempting to do getter and setter so I can update mileage
    # @property
    # def get._update_mileage_car():
    #     print("updated mileage")
        



# CarManager.terminal_application()
print(CarManager.terminal())
# print(CarManager.all_cars)
# print("total cars: " + str(CarManager.total_cars)) #AttributeError: type object "CarManager" has no attribut "total_cars"
# print("car1")
# print(CarManager.user_inputs)
# car1 = CarManager( "Toyota", "Camry", 1998, 120345, ["oil change", "filter check"])
# print(car1._id)
# print(CarManager.all_cars)
# print("total cars: " + str(CarManager.total_cars))
# print("car2")
# car2 = CarManager("Honday", "Odyssey", 2015, 98345, ["tire rotation", "transmission fluid flush" ])
# print(car2._id)
# print(CarManager.all_cars)