import re
import os
from datetime import datetime
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials


class HotelBillCalculator:
    def __init__(self):
        self.customer_name = ""
        self.customer_address = ""
        self.check_in_date = None
        self.check_out_date = None
        self.room_number = 101  # Example room number assignment
        self.room_rent = 0
        self.restaurant_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        


        SCOPE = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        self.sheet = GSPREAD_CLIENT.open('Hotelio').worksheet("Total Expenditure")
        
        
        

    def exit_or_input(self, prompt):
        user_input = input(prompt).strip()
        if user_input.lower() == "exit":
            print("Exiting the program. Thank you!")
            sys.exit()
        return user_input

    def get_valid_date(self, prompt):
        while True:
            date_input = self.exit_or_input(prompt)
            try:
                return datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Error: Please enter a valid date in YYYY-MM-DD format. Type 'exit' to quit.")

    def get_valid_number(self, prompt, min_value=None, max_value=None):
        while True:
            user_input = self.exit_or_input(prompt)
            try:
                value = int(user_input)
                if min_value is not None and value < min_value:
                    print(f"Error: Value must be at least {min_value}. Type 'exit' to quit.")
                elif max_value is not None and value > max_value:
                    print(f"Error: Value must not exceed {max_value}. Type 'exit' to quit.")
                else:
                    return value
            except ValueError:
                print("Error: Please enter a valid numeric value. Type 'exit' to quit.")

    def input_data(self):
        while True:
            self.customer_name = self.exit_or_input("\nEnter your name: ")
            if not self.customer_name:
                print("Error: Name cannot be empty. Type 'exit' to quit.")
            elif not re.match(r"^[a-zA-Z\s]+$", self.customer_name):
                print("Error: Name can only contain alphabets and spaces. Type 'exit' to quit.")
            else:
                break

        while True:
            self.customer_address = self.exit_or_input("\nEnter your address: ")
            if not self.customer_address:
                print("Error: Address cannot be empty. Type 'exit' to quit.")
            else:
                break

        self.check_in_date = self.get_valid_date("\nEnter your check-in date (YYYY-MM-DD): ")
        self.check_out_date = self.get_valid_date("\nEnter your check-out date (YYYY-MM-DD): ")
        while self.check_out_date <= self.check_in_date:
            print("Error: Check-out date must be after the check-in date. Type 'exit' to quit.")
            self.check_out_date = self.get_valid_date("\nEnter your check-out date (YYYY-MM-DD): ")

        print("Your room number:", self.room_number, "\n")

    def calculate_room_rent(self):
        print("\nChoose room type:")
        print("1. Standard (1000 per day)")
        print("2. Deluxe (2000 per day)")
        print("3. Suite (3000 per day)")
        room_type = self.get_valid_number("Enter your choice (1-3): ", 1, 3)

        days = self.get_valid_number("Enter number of days for the stay: ", 1)
        rates = {1: 1000, 2: 2000, 3: 3000}
        self.room_rent = days * rates[room_type]

    def calculate_restaurant_bill(self):
        print("\nEnter total restaurant bill amount:")
        self.restaurant_bill = self.get_valid_number("Enter amount: ", 0)

    def calculate_laundry_bill(self):
        print("\nEnter total laundry bill amount:")
        self.laundry_bill = self.get_valid_number("Enter amount: ", 0)

    def calculate_game_bill(self):
        print("\nEnter total game bill amount:")
        self.game_bill = self.get_valid_number("Enter amount: ", 0)

    def display_bill(self):
        total_bill = self.room_rent + self.restaurant_bill + self.laundry_bill + self.game_bill
        print("\n" + "=" * 30)
        print("Hotel Bill Summary")
        print("=" * 30)
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer Address: {self.customer_address}")
        print(f"Check-in Date: {self.check_in_date.strftime('%Y-%m-%d')}")
        print(f"Check-out Date: {self.check_out_date.strftime('%Y-%m-%d')}")
        print(f"Room Rent: {self.room_rent}")
        print(f"Restaurant Bill: {self.restaurant_bill}")
        print(f"Laundry Bill: {self.laundry_bill}")
        print(f"Game Bill: {self.game_bill}")
        print(f"Total Bill: {total_bill}")
        print("=" * 30)
        
        # Save to spreadsheet
        self.save_to_spreadsheet(total_bill)

    def save_to_spreadsheet(self, total_bill):
        self.sheet.append_row([
            self.customer_name,
            self.customer_address,
            self.check_in_date.strftime('%Y-%m-%d'),
            self.check_out_date.strftime('%Y-%m-%d'),
            self.room_rent,
            self.restaurant_bill,
            self.laundry_bill,
            self.game_bill,
            total_bill
        ])
        print("Data has been saved to the spreadsheet.")

    def edit_spreadsheet_entry(self):
        print("\nEditing an existing entry.")
        row_number = self.get_valid_number("Enter the row number to edit (excluding headers): ", 2)
        try:
            row = self.sheet.row_values(row_number)
            print(f"Current row data: {row}")
            
            self.customer_name = self.exit_or_input("Enter new name (leave blank to keep current): ") or row[0]
            self.customer_address = self.exit_or_input("Enter new address (leave blank to keep current): ") or row[1]
            self.check_in_date = self.get_valid_date("Enter new check-in date (YYYY-MM-DD, or rewrite the current date you have): ") or datetime.strptime(row[2], "%Y-%m-%d")
            self.check_out_date = self.get_valid_date("Enter new check-out date (YYYY-MM-DD, or rewrite the current date you have): ") or datetime.strptime(row[3], "%Y-%m-%d")
            self.room_rent = self.get_valid_number("Enter new room rent (or enter the current): ", 0) or int(row[4])
            self.restaurant_bill = self.get_valid_number("Enter new restaurant bill (leave blank to keep current): ", 0) or int(row[5])
            self.laundry_bill = self.get_valid_number("Enter new laundry bill (leave blank to keep current): ", 0) or int(row[6])
            self.game_bill = self.get_valid_number("Enter new game bill (leave blank to keep current): ", 0) or int(row[7])
            total_bill = self.room_rent + self.restaurant_bill + self.laundry_bill + self.game_bill

            self.sheet.update(f"A{row_number}", [[
                self.customer_name,
                self.customer_address,
                self.check_in_date.strftime('%Y-%m-%d'),
                self.check_out_date.strftime('%Y-%m-%d'),
                self.room_rent,
                self.restaurant_bill,
                self.laundry_bill,
                self.game_bill,
                total_bill
            ]])

            print("Row updated successfully.")
        except gspread.exceptions.APIError as e:
            print(f"Error editing the row: {e}")

def main():
    hotel_calculator = HotelBillCalculator()

    while True:
        print("\n1. Enter Customer Data")
        print("2. Calculate Room Rent")
        print("3. Calculate Restaurant Bill")
        print("4. Calculate Laundry Bill")
        print("5. Calculate Game Bill")
        print("6. Show Total Cost")
        print("7. Edit Spreadsheet Entry")
        print("8. EXIT")

        choice = hotel_calculator.get_valid_number("\nEnter your choice (1-8): ", 1, 8)

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
            hotel_calculator.edit_spreadsheet_entry()
        elif choice == 8:
            print("Exiting the program. Thank you!")
            break

if __name__ == "__main__":
    main()
