## Hotel Bill 
### Overview
The Hotel Bill Calculator is a Python-based application designed to help hotels manage and calculate customer bills. The application collects customer data, calculates various charges including room rent, restaurant bills, laundry bills, and game bills, and then displays the total bill to the customer.

### Features
1. __Customer Data Collection:__
Collects customer's name, address, check-in date, and check-out date.
2. __Room Rent Calculation:__ 
Calculates the room rent based on the type of room and the number of nights stayed.
3. __Restaurant Bill Calculation:__ 
Calculates the total cost of food items ordered by the customer.
4. __Laundry Bill Calculation:__ 
Calculates the total cost of laundry services used by the customer.
5. __Game Bill Calculation:__ 
Calculates the total cost of games played by the customer.
6. __Total Bill Display:__ 
Displays a detailed bill including all charges and the grand total. 

## Class and Methods
#### HotelBillCalculator
This is the main class responsible for managing the hotel billing process.

`__init__(self, room_type='', food_bill=0, game_bill=0, laundry_bill=0, total_bill=0, additional_charges=1, customer_name='', customer_address='', check_in_date='', check_out_date='', room_number=101)`
The constructor initializes the class with default or provided values and prints a welcome message.

`input_data(self)`
Collects and validates customer data:

- __customer_name:__ Must not be empty; __NOTE__ didn't validate it to be only letters because in some culture names have numbers to indicate the position the child is born in.
- __customer_address:__ Must not be empty.
- __check_in_date:__ Must be a valid date in the format YYYY-MM-DD and later than 2020-01-01.
- __check_out_date:__ Must be a valid date in the format YYYY-MM-DD and later than 2020-01-01.

1. `get_valid_date(self, prompt)`
Helper method to validate date inputs ensuring they are in the correct format and within the specified range.

2. `calculate_room_rent(self)`
Calculates the room rent based on the type of room selected and the number of nights stayed:

- Suite: €60 per night
- Junior Suite: €50 per night
- Double: €40 per night
- Single: €30 per night
3. `calculate_restaurant_bill(self)`
Calculates the restaurant bill based on the menu items ordered and their quantities:

- Water: €2
- Tea: €3
- Breakfast Combo: €20
- Lunch: €30
- Dinner: €50
4. `calculate_laundry_bill(self)`
Calculates the laundry bill based on the items and their quantities:
- Shorts: €3
- Trousers: €4
- Shirt: €5
- Jeans: €6
- Girl Suit: €8

5. `calculate_game_bill(self)`
Calculates the game bill based on the games played and the number of hours spent:

- Table Tennis: €15 per hour
- Bowling: €20 per hour
- Snooker: €25 per hour
- Video Games: €35 per hour
- Pool: €50 per hour
- display_bill(self)
- Displays the total bill, including all charges and the grand total, along with customer details.

### `main()`
The main function that runs the Hotel Bill Calculator. It provides a menu-driven interface to:

1. Enter customer data
2. Calculate room rent
3. Calculate restaurant bill
4. Calculate laundry bill
5. Calculate game bill
6. Show total cost
7. Exit the application



## Menu Options:

1. Enter Customer Data: Collects and validates customer details.
2. Calculate Room Rent: Calculates the room rent based on user input.
3. Calculate Restaurant Bill: Adds items to the restaurant bill based on user input.
4. Calculate Laundry Bill: Adds items to the laundry bill based on user input.
5. Calculate Game Bill: Adds items to the game bill based on user input.
6. Show Total Cost: Displays the detailed bill including all charges.
7. EXIT: Exits the application.
 
 ## Testing
 ### Validator testing
 

 ### Manual testiing

 #### Browser Compatibility
1. __Google Chrome:__ No issues with appearance, responsiveness, or functionality.
2. __Safari:__ No issues with appearance, responsiveness, or functionality.
3. __Mozilla Firefox:__ No issues with appearance, responsiveness, or functionality.
4. __Microsoft Edge:__ No issues with appearance, responsiveness, or functionality.

 #### Device compatibility
1. __MacBook Pro 13:__ No issues with appearance, responsiveness, or functionality.
2. __iPhone 13 Mini:__ No issues with appearance, responsiveness, or functionality.
3. __iPad 9th Generation:__ No issues with appearance, responsiveness, or functionality.
4. __Iphone 14:__ No issues with appearance, responsiveness, or functionality.
4. __Iphone 15 pro and pro max:__ No issues with appearance, responsiveness, or functionality.
### The Lighthouse Test