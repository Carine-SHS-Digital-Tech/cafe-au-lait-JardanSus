import csv

program = True
while program:
    menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
    prices = [3, 2.25, 2.50, 2.50]

    gst = float(0.1)
    takeAway = float(0.05)

    x = 0
    d_count = 0
    t_count = 0
    order_ID = 0

    orderItems = []
    orderPrice = []
    order_qty = []

    nextItem = True

    # user can choose operating mode and type of order which then adds a count to the takeaway or dine in orders
    mode_op = input("Select Mode of Operation. New Order [1] or Daily Summary [2]: ")
    choice = input("Takeaway [1] or Dine in [2]? ")
    if choice == 1:
        t_count += 1
    else:
        d_count += 1

    # a function that allows the user to enter order information
    def new_order():
        count = 0
        menu1 = 0
        menu2 = 0
        menu3 = 0
        menu4 = 0
        print("Here is the menu:\n ")
        print(f"[1]\t  {menu[0]}\t$3.00")
        print(f"[2]\t  {menu[1]}\t\t$2.25")
        print(f"[3]\t  {menu[2]}\t\t\t$2.50")
        print(f"[4]\t  {menu[3]}\t$2.50")
        print("\nTo complete order, enter [5] ")
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

                    # payment system
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
                            print(f"You still owe: ${round(total, 2):.2f}")
                        else:
                            print(f"Your Change is: ${round(total - payment, 2)* -1:.2f}")
                            print("Payment Complete")
                            checkout = False
                            return checkout
                next_item = False
                return next_item
            else:
                print("Invalid input")


    if mode_op == "1":
        order_ID += 1
        new_order()
        end_day = input("Is it the end of the day [Y/N]")
        if end_day == "Y":
            program = False

        header = ["Order_ID", "Type", "Item_1", "QTY_1", "EXGST_1", "ITEM_2", "QTY_2", "EXGST_2", "ITEM_3", "QTY_3",
        "EXGST_3", "ITEM_4", "QTY_4", "EXGST_4", "ORDER_CUPS", "ORDER_GST", "ORDER_TAX", "ORDER_TOTAL"]

        # writes information to a csv file
        with open('daily_summary.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(str(order_ID))
