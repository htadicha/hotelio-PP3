import datetime
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
        print(
            "\n\nWelcome to Moyale Hotel: please enter your choice below to view total bill,\n\n\nselect Exit options to move to the next item or to stop the app.\n"
        )
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
        later in the code we will ensure the information provided for the above customer data are valid inputs for each

        """
        self.customer_name = input("\nEnter your name: ").strip()
        while not self.customer_name:
            print("Name cannot be empty.")
            self.customer_name = input("\nEnter your name: ").strip()

        self.customer_address = input("\nEnter your address: ").strip()
        while not self.customer_address:
            print("Address cannot be empty.")
            self.customer_address = input("\nEnter your address: ").strip()

        self.check_in_date = self.get_valid_date(
            "\nEnter your check-in date (YYYY-MM-DD): "
        )
        self.check_out_date = self.get_valid_date(
            "\nEnter your check-out date (YYYY-MM-DD): "
        )

        print("Your room number: ", self.room_number, "\n")

    def get_valid_date(self, prompt):
        """
        Validate the input date format and ensure it is later than 2020-01-01.
        """
        while True:
            date_str = input(prompt).strip()
            try:
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                if date_obj.year <= 2020:
                    print("Date must be later than 2020-01-01.")
                else:
                    return date_str
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")

    # at each stage runninng the code to ensure we don't have majore typo or indentation error

    def calculate_room_rent(self):
        """- Method to:
        1. Calculates the room rent based on the room type selected and the number of nights stayed.
        2. Presents a menu of room types with corresponding charges per night.
        """
        print("We have the following rooms for you:-")
        print("1. Suite: = euros 60 per night")
        print("2. Junior Suite: = euros 50 per night")
        print("3. Double: = euros 40 per night")
        print("4. Single: = euros 30 per night")

        #    use while true to validate whether the type selected btween 1-4 is a valid number
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
        we will have 1- 6 options and validate the numbers and have 6 break the loop as it will be used as exit
        1. Calculates the restaurant bill based on the items ordered and their quantities.
        2. Presents a menu of food items with corresponding charges.
        """
        print("RESTAURANT MENU")
        print("1. Water = euros 2")
        print("2. Tea = euros 3")
        print("3. Breakfast Combo = euros 20")
        print("4. Lunch = euros 30")
        print("5. Dinner = euros 50")
        print("6. Exit")
        # exception handling for invalid number input
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
        print("LAUNDRY MENU")
        print("1. Shorts = euros 3")
        print("2. Trousers = euros 4")
        print("3. Shirt = euros 5")
        print("4. Jeans = euros 6")
        print("5. Girl Suit = euros 8")
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
            # setting the choices for 1-6 and multiplying by quantity
            if choice == 1:
                self.laundry_bill += 3 * quantity
            elif choice == 2:
                self.laundry_bill += 4 * quantity
            elif choice == 3:
                self.laundry_bill += 5 * quantity
            elif choice == 4:
                self.laundry_bill += 6 * quantity
            elif choice == 5:
                self.laundry_bill += 8 * quantity

        print("Total laundry cost: Rs", self.laundry_bill, "\n")

    # calculating game bill next
    def calculate_game_bill(self):
        """
        1. Calculates the game bill based on the games played and hours spent.
        2. Presents a menu of games with corresponding charges per hour.
        """
        print("GAME MENU")
        print("1. Table Tennis = euros 15 per hour")
        print("2. Bowling = euros 20 per hour")
        print("3. Snooker = euros 25 per hour")
        print("4. Video Games = euros 35 per hour")
        print("5. Pool = euros 50 per hour")
        print("6. Exit")
        #  will set up the game  bill to have similar condition as the rest of the bills
        # 1. must be an integer
        # The game choices should be 1-6
        # Number of hours must also be > 0
        while True:
            try:
                choice = int(input("Enter your choice: ").strip())
                if choice == 6:
                    break
                if choice not in [1, 2, 3, 4, 5, 6]:
                    print("Invalid choice. Please choose a valid game.")
                    continue

                # Adding conditons for hour value to always be greater than 0
                hours = int(input("Enter the number of hours: ").strip())
                if hours <= 0:
                    print("Number of hours must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
            # add the choices to be selected for hourly rate multiplication
            if choice == 1:
                self.game_bill += 15 * hours
            elif choice == 2:
                self.game_bill += 20 * hours
            elif choice == 3:
                self.game_bill += 25 * hours
            elif choice == 4:
                self.game_bill += 35 * hours
            elif choice == 5:
                self.game_bill += 50 * hours

        print("Total game cost: Euro", self.game_bill, "\n")

    # adding the calculator for hotel bills including charges
    def display_bill(self):
        """
        Display the total hotel bill including all charges.
        """
        print("HOTEL BILL")
        print("Customer Details:")
        print("Customer Name:", self.customer_name)
        print("Customer Address:", self.customer_address)
        print("Check-in Date:", self.check_in_date)
        print("Check-out Date:", self.check_out_date)
        print("Room Number:", self.room_number)
        print("Room Rent:", self.room_rent)
        print("Food Bill:", self.food_bill)
        print("Laundry Bill:", self.laundry_bill)
        print("Game Bill:", self.game_bill)
        #  total bill added at the end of the  to ensure charges for all the bills in the hotel is included.

        self.total_bill = (
            self.room_rent + self.food_bill + self.laundry_bill + self.game_bill
        )

        print("Sub Total Bill:", self.total_bill)
        print("Additional Service Charges:", self.additional_charges)
        print("Grand Total Bill:", self.total_bill + self.additional_charges, "\n")
        self.room_number += 1


# main function to run the calculator to be added to print customer details, room bill, restaurant bill, game bull and total cost
def main():
    """
    Main function to run the hotel bill calculator.
    """
    hotel_calculator = HotelBillCalculator()

    while True:
        print("1. Enter Customer Data")
        print("2. Calculate Room Rent")
        print("3. Calculate Restaurant Bill")
        print("4. Calculate Laundry Bill")
        print("5. Calculate Game Bill")
        print("6. Show Total Cost")
        print("7. EXIT")
        # next validation has to be added to ensure the added inputs are valid inputs and should always be integer
        try:
            choice = int(input("\nEnter your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
        # validate the choices to print out the bill calculator based on choices made.`

        if choice == 1:
            hotel_calculator.input_data()
        elif choice == 2:
            hotel_calculator.calculate_room_rent()
        elif choice == 3:
            hotel_calculator.calculate_restaurant_bill()
        elif choice == 4:
            hotel_calculator.calculate_laundry_bill()
        elif choice == 5:
            hotel_calculator.calculate_game_bill()
        elif choice == 6:
            hotel_calculator.display_bill()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
