menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
prices = [3, 2.25, 2.50, 2.50]

gst = float(0.1)
takeAway = float(0.05)

x = 0

orderItems = []
orderPrice = []
order_qty = []
nextItem = True

mode_op = input("Select Mode of Operation. New Order [1] or Daily Summary [2]: ")
choice = input("Takeaway [1] or Dine in [2]? ")
print("Here is the menu:\n ")

print(f"[1]\t  {menu[0]}\t$3.00")
print(f"[2]\t  {menu[1]}\t\t$2.25")
print(f"[3]\t  {menu[2]}\t\t\t$2.50")
print(f"[4]\t  {menu[3]}\t$2.50")

print("\nTo complete order, enter [5] ")


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
        elif order == "5":
            print("Here is your order summary:")
            a = 0
            sub_total = sum(orderPrice)
            while a < count:
                print(f"Item:\t{orderItems[a]}")
                print(f"Qty:\t{order_qty[a]}")
                print(f"Price:\t${orderPrice[a]:.2f}")
                a = a + 1
            print(f"\nSubtotal:\t${sum(orderPrice):.2f}")
            if choice == "1":
                total = sub_total + (sub_total * takeAway) + (sub_total * gst)
                print(f"Surcharge:\t${sub_total * takeAway:.2f}")
                print(f"GST:\t\t${sub_total * gst:.2f}")
                print(f"Total:\t\t${total:.2f}")
                checkout = True
                while checkout:
                    payment = float(input("Enter Payment Amount: "))
                    if payment == total:
                        print("Payment Complete")
                        checkout = False
                        return checkout
                    elif payment < total:
                        total = round(total - payment, 2)
                        print(f"You still owe: $ {round(total, 2):.2f}")
                    else:
                        print(f"Your Change is: $ {round(total - payment, 2) * -1:.2f}")
                        print("Payment Complete")
                        checkout = False
                        return checkout
            else:
                total = round(sub_total + sub_total * gst, 2)
                print(f"GST: ${sub_total * gst:.2f}")
                print(f"Total: ${total:.2f}")
                checkout = True
                while checkout:
                    payment = float(input("Enter Payment Amount: "))
                    if payment == total:
                        print("Payment Complete")
                        checkout = False
                        return checkout
                    elif payment < total:
                        total = round(total - payment, 2)
                        print(f"You still owe: $ {round(total, 2):.2f}")
                    else:
                        print(f"Your Change is: $ {round(total - payment, 2)* -1:.2f}")
                        print("Payment Complete")
                        checkout = False
                        return checkout
            next_item = False
            return next_item
        else:
            print("Invalid input / item not on menu")


if mode_op == "1":
    new_order()
#   elif mode_op == "2":

#    else:
#        print("Invalid Mode of Operation")

#header = ["Order_ID", "Type", "Item_1", "QTY_1", "EXGST_1", "ITEM_2", "QTY_2", "EXGST_2", "ITEM_3", "QTY_3",
# "EXGST_3", "ITEM_4", "QTY_4", "EXGST_4", "ORDER_CUPS", "ORDER_GST", "ORDER_TAX", "ORDER_TOTAL"]
#with open()
