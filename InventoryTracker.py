"""Inventory Tracker
Imagine a small store inventory like {"apple": 10, "banana": 5, "milk": 2}. Program should allow
adding new items, selling items (subtract quantity), and print items that are low in stock (<3)"""

inventory ={
    "apple":10,
    "banana":5,
    "milk":2
}
def addnewitems():
    while True:
        items = input("Enter the item you want to add (type 'done' to stop): ")

        if items.lower() == "done":
            break

        qty = int(input(f"Enter quantity of {items}: "))

        if items in inventory:
            inventory[items] += qty
        else:
            inventory[items] = qty

        print(f"{qty} of {items} added successfully.")


def sellitems():
    while True:
        items = input("Enter the item you want to sell (type 'done' to stop): ")

        if items.lower() == "done":
            break

        qty = int(input(f"Enter quantity of {items}: "))

        if items not in inventory:
            print("Item not available!")
        elif inventory[items] < qty:
            print(f"Not enough stock! Available: {inventory[items]}")
        else:
            inventory[items] -= qty
            print(f"{qty} of {items} sold successfully!")


def lowstock():
    print("Items That are low in stock")
    for item, qty in inventory.items():
        if qty < 3:
            print(f"{item}: {qty}")
        
def main():
    print("1 add new items")
    print("2 sell items")
    print("3 view low stock items")
    option = int(input("enter the option you want to perform :"))

    if option==1:
        addnewitems()
    elif option==2:
        sellitems()
    elif option==3:
        lowstock()
    else:
        print("invalid ")

main()


    




