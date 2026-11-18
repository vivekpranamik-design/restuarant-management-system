
# RESTAURANT MANAGEMENT SYSTEM

menu = {
    1: ("Pizza", 200),
    2: ("Burger", 100),
    3: ("Coffee", 50),
    
}

order = []
total = 57.50

print("=" * 40)
print("     WELCOME TO OUR RESTAURANT")
print("=" * 40)

while True:
    print("\n----------- MAIN MENU -----------")
    print("1. Display Food Menu")
    print("2. Place Order")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n----------- FOOD MENU -----------")
        for key, value in menu.items():
            print(f"{key}. {value[0]} - Rs.{value[1]}")

    elif choice == "2":
        print("\nEnter food item number:")
        for key, value in menu.items():
            print(f"{key}. {value[0]} - Rs.{value[1]}")

        try:
            item = int(input("\nEnter item number: "))

            if item in menu:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    name, price = menu[item]
                    amount = price * quantity

                    order.append((name, price, quantity, amount))
                    total += amount

                    print(f"{name} added successfully!")
                else:
                    print("Quantity must be greater than zero.")

            else:
                print("Invalid item number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        if len(order) == 0:
            print("\nNo order placed yet.")
        else:
            print("\n========== CUSTOMER BILL ==========")
            print("Item       Price   Qty   Amount")
            print("-----------------------------------")

            for name, price, qty, amount in order:
                print(f"{name:<11}{price:<8}{qty:<3}{amount}")

            print("-----------------------------------")
            print("Subtotal: Rs.", total)

            gst = total * 0.05
            grand_total = total + gst

            print("GST (5%): Rs.", round(gst, 2))
            print("Total Bill: Rs.", round(grand_total, 2))
            print("===================================")
            print("     THANK YOU! VISIT AGAIN")
            print("===================================")

    elif choice == "4":
        print("\nThank you for visiting!")
        break

    else:
        print("\nInvalid choice! Please try again.")
