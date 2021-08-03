menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
prices = [3, 2.25, 2.50, 2.50]

gst = float(0.1)
takeAway = float(0.05)

x = 0

orderItems = []
orderPrice = []
order_qty = []
nextItem = True

mode_op = input("Select Mode of Operation. New Order [N] or Daily Summary [D]: ")
choice = input("Takeaway [T] or Dine in [D]? ")
print("Here is the menu:\n ")

print("[1]    $3.00    " + menu[0])
print("[2]    $2.25    " + menu[1])
print("[3]    $2.50    " + menu[2])
print("[4]    $2.50    " + menu[3])

print("\nTo complete order, press enter ")


def new_order():
    count = 0
    menu1 = 0
    menu2 = 0
    menu3 = 0
    menu4 = 0
    while nextItem:
        order = input("Enter Item Number [1-4]: ")
        if order == "1":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[0])
            orderPrice.append(prices[0] * qty)
            order_qty.append(qty)
            count = count + 1
            menu1 = menu1 + qty
        elif order == "2":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[1])
            orderPrice.append(prices[1] * qty)
            order_qty.append(qty)
            count = count + 1
            menu2 = menu2 + qty
        elif order == "3":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[2])
            orderPrice.append(prices[2] * qty)
            order_qty.append(qty)
            count = count + 1
            menu3 = menu3 + qty
        elif order == "4":
            qty = int(input("Enter Quantity: "))
            orderItems.append(menu[3])
            orderPrice.append(prices[3] * qty)
            order_qty.append(qty)
            count = count + 1
            menu4 = menu4 + qty
        elif order == "":
            print("Here is your order summary:")
            a = 0
            sub_total = sum(orderPrice)
            while a < count:
                print(f"Item:  {orderItems[a]}")
                print(f"Qty: {order_qty[a]}")
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


new_order()
