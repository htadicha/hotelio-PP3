# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
class HotelBillCalculator:
   """
   A class to calculate hotel bills for room rent, restaurant, laundry, and game services.
   """


   def __init__(self, room_type='', food_bill=0, game_bill=0, laundry_bill=0, total_bill=0, additional_charges=1, customer_name='', customer_address='', check_in_date='', check_out_date='', room_number=101):
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