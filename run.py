# prerequisites:
# 1. ensure you have all the required information e.g currency
# 2. understand OOP elements of python from CI modules
# 3. understand python maths concepts like +, * and addition to add all the required grand totals
#  after project is complete go back and make sure you have correct spelling for your docustrings and comments
#  make sure you follow the grading criteria for proper grading and submission
# Github pages doesn't support python for deployment, so ensure you have good understand of how to deploy on Heroku in the module.


class HotelBillCalculator:
    """
    A class to calculate hotel bills for room rent, restaurant, laundry, and game services.
    """

    def __init__(
        self,
        room_type="",
        food_bill=0,
        game_bill=0,
        laundry_bill=0,
        total_bill=0,
        additional_charges=1,
        customer_name="",
        customer_address="",
        check_in_date="",
        check_out_date="",
        room_number=101,
    ):
        """
        Initialise the HotelBillCalculator with default or provided values.
        """
        print("\n\n*****WELCOME TO HEWING HOTEL*****\n")
        self.room_type = room_type
        self.food_bill = food_bill
        self.game_bill = game_bill
        self.laundry_bill = laundry_bill
        self.total_bill = total_bill
        self.additional_charges = additional_charges
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_number = room_number

    #    build input data for collecting customer data
    def input_data(self):
        """
        input method for collection of customer data such as name, address, check-in date, and check-out date.
        later in the code we will ensure the information provided for the above customer data are valide inputs for each

        """
        self.customer_name = input("\nEnter your name: ").strip()
        while not self.customer_name:
            print("Name cannot be empty.")
            self.customer_name = input("\nEnter your name: ").strip()

        self.customer_address = input("\nEnter your address: ").strip()
        while not self.customer_address:
            print("Address cannot be empty.")
            self.customer_address = input("\nEnter your address: ").strip()

        self.check_in_date = input("\nEnter your check-in date: ").strip()
        while not self.check_in_date:
            print("Check-in date cannot be empty.")
            self.check_in_date = input("\nEnter your check-in date: ").strip()

        self.check_out_date = input("\nEnter your check-out date: ").strip()
        while not self.check_out_date:
            print("Check-out date cannot be empty.")
            self.check_out_date = input("\nEnter your check-out date: ").strip()

        print("Your room number: ", self.room_number, "\n")

    # at each stage runninng the code to ensure we don't have majore typo or indentation error

    def calculate_room_rent(self):
        """- Method to:
        1. Calculates the room rent based on the room type selected and the number of nights stayed.
        2. Presents a menu of room types with corresponding charges per night.
        """
        print("We have the following rooms for you:-")
        print("1. Type A ----> euro 60 per night")
        print("2. Type B ----> euro 50 per night")
        print("3. Type C ----> euro 40 per night")
        print("4. Type D ----> euro 30 per night")

        #    use while true to validate whether the type selected btween 1-4 is a valide number
        while True:
            try:
                choice = int(input("Enter your choice: ").strip())
                if choice not in [1, 2, 3, 4]:
                    print("Invalid choice. Please choose a valid room type.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        #    set the valid number of nights to be always greater than 0
        while True:
            try:
                nights = int(input("For how many nights did you stay: ").strip())
                if nights <= 0:
                    print("Number of nights must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of nights.")

        # set the control flow for choices taken by user if choices are from 1-4
        if choice == 1:
            print("You have opted for room type A")
            self.room_rent = 60 * nights
        elif choice == 2:
            print("You have opted for room type B")
            self.room_rent = 50 * nights
        elif choice == 3:
            print("You have opted for room type C")
            self.room_rent = 40 * nights
        elif choice == 4:
            print("You have opted for room type D")
            self.room_rent = 30 * nights

        print("Your room rent is: euro", self.room_rent, "\n")

    # next we will calculate the restaurant bill e.g food, water
    def calculate_restaurant_bill(self):
        """
        The restaurant bill will help us understand the cost of food and water at different mill time
        we will have 1-6 options and validate the numbers and have 6 break the loop as it will be used as exit
        1. Calculates the restaurant bill based on the items ordered and their quantities.
        2. Presents a menu of food items with corresponding charges.
        """
        print("*****RESTAURANT MENU*****")
        print("1. Water -----> euro 2")
        print("2. Tea ----->  euro 3")
        print("3. Breakfast Combo -----> euro 20")
        print("4. Lunch -----> euro 30")
        print("5. Dinner -----> euro 50")
        print("6. Exit")
        # exception handling for invalide number input
        # number has to be between 1-6, 6 breaks and restart the choices
        # ensure that quantity is always greater than 0
        # ensure input is integer
        while True:
            try:
                choice = int(input("Enter your choice: ").strip())
                if choice == 6:
                    break
                if choice not in [1, 2, 3, 4, 5, 6]:
                    print("Invalid choice. Please choose a valid menu item.")
                    continue
                quantity = int(input("Enter the quantity: ").strip())
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            # build flow for choices to be calculated for restaurant food and water bills during different meal time.
            if choice == 1:
                self.food_bill += 2 * quantity
            elif choice == 2:
                self.food_bill += 3 * quantity
            elif choice == 3:
                self.food_bill += 20 * quantity
            elif choice == 4:
                self.food_bill += 30 * quantity
            elif choice == 5:
                self.food_bill += 50 * quantity
        print("Total food cost: Rs", self.food_bill, "\n")

    # we will calculate laundary bill in the next lines
    def calculate_laundry_bill(self):
        """
        1. Calculates the laundry bill based on the items laundered and their quantities
        2.Presents a menu of laundry items with corresponding charges.
        """
        print("******LAUNDRY MENU*******")
        print("1. Shorts -----> euro 3")
        print("2. Trousers -----> euro 4")
        print("3. Shirt -----> euro 5")
        print("4. Jeans -----> euro 6")
        print("5. Girl Suit -----> euro 8")
        print("6. Exit")
# set the input to be integers and add value error using the while true statement.
# make sure the input is only integer and takes numbers from 1-6,  ensure quantity is always greater than 0
# set 6 to be an exit, hence breaks
        while True:
             try:
                choice = int(input("Enter your choice: ").strip())
                if choice == 6:
                   break
                if choice not in [1, 2, 3, 4, 5, 6]:
                   print("Invalid choice. Please choose a valid laundry item.")
                   continue
# add conditions for the input to always be greater than 0 for quantity
                quantity = int(input("Enter the quantity: ").strip())
                if quantity <= 0:
                   print("Quantity must be greater than 0.")
                   continue

                
             except ValueError:
                  print("Invalid input. Please enter valid numbers.")
              