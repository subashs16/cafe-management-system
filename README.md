Cafe Ordering System
Overview:
The Cafe Ordering System is a simple command-line application that allows users to place orders at a cafe. 
Users can select items from a predefined menu, and the system will calculate the total amount based on their selections.

Features:
Menu Display: Shows the available items and their prices.
Order Placement: Allows users to add items to their order.
Order Total: Calculates and displays the total amount of the order.

Menu:
Coffee: Rs40
Tea: Rs30
Sandwich: Rs60
Cake: Rs50
Juice: Rs30

Usage:
Start the Application: Run the script to display the menu and welcome message.

Place an Order:
Enter the name of the item you wish to order.
If the item is available, it will be added to your order.
You will be prompted to add another item if desired.
If an item is not available, an error message will be shown.
View Total Amount: After placing your orders, the total amount of your order will be displayed.

Example
To run the application, execute the script:

bash
Copy code
python cafe_ordering_system.py

Code Structure:
Menu Dictionary: Contains items and their prices.
Order Input: Prompts the user to enter items and checks their availability.
Total Calculation: Computes the total amount based on the user's order.

Requirements:
Python 3.x
