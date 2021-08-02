menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
prices = [3, 2.25, 2.50, 2.50]

gst = float(0.1)
takeAway = float(0.05)

x = 0

orderItems = []
orderPrice = []

nextItem = True

choice = input("Hi, welcome to Cafe au Lait\nWould you like takeaway [T] or Dine in [D]? ")
print("Here is the menu:\n ")

print("$3.00    " + menu[0])
print("$2.25    " + menu[1])
print("$2.50    " + menu[2])
print("$2.50    " + menu[3])

print("\nTo complete order, press enter ")


def order_func():
    count = 0
    while nextItem:
        order = input("Enter Item: ")
        if order == "Cappuccino":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[0] + " * " + str(qty))
            orderPrice.append(prices[0] * qty)
            count = count + 1
        elif order == "Espresso":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[1] + " * " + str(qty))
            orderPrice.append(prices[1] * qty)
            count = count + 1
        elif order == "Latte":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[2] + " * " + str(qty))
            orderPrice.append(prices[2] * qty)
            count = count + 1
        elif order == "Iced Coffee":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[3] + " * " + str(qty))
            orderPrice.append(prices[3] * qty)
            count = count + 1
        elif order == "":
            print("Here is your order summary:")
            a = 0
            sub_total = sum(orderPrice)
            while a < count:
                print(f"Item:  {orderItems[a]}")
                print(f"Price: ${orderPrice[a]:.2f}")
                a = a + 1
            print(f"\nSubtotal: ${sum(orderPrice):.2f}")
            if choice == "T":
                print(f"Surcharge: ${sub_total * takeAway:.2f}")
                print(f"GST: ${sub_total * gst:.2f}")
                print(f"The total price of your order is: ${sub_total + (sub_total * takeAway) + (sub_total * gst):.2f}")
            else:
                print(f"GST: ${sub_total * gst:.2f}")
                print(f"The total price of your order is: ${sub_total + sub_total * gst:.2f}")
            next_item = False
            return next_item
        else:
            print("Invalid input / item not on menu")


order_func()
