menu={
    'coffee':40,
    'tea':30,
    'sandwich':60,
    'cake':50,
    'juice':30.
}
#greet
print("Welcome to cafe")
print("Coffee: Rs40\nTea: Rs30\nSandwich: Rs60\nCake: Rs50\nJuice: Rs30")
order_total=0
item_1=input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available")
another_order=input("Do you want to add another item?(yes/NO) : ")
if another_order=="yes":
    item_2=input("Enter the name of second item: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print("Ordered item {item_2} is not available")
print(f"Total Amount:{order_total}")
