# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
