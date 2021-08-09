import csv
import os

header = ["Order_ID", "Type", "Item_1", "QTY_1", "EXGST_1", "ITEM_2", "QTY_2", "EXGST_2", "ITEM_3", "QTY_3",
          "EXGST_3", "ITEM_4", "QTY_4", "EXGST_4", "ORDER_CUPS", "ORDER_GST", "ORDER_TAX", "ORDER_TOTAL"]

# writes the header to the csv file
with open('daily_summary.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

d_count = 0
t_count = 0
order_ID = 0

t_price = []
gst_collected = []

program = True
while program:
    # all variables and lists are set
    menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
    prices = [3, 2.25, 2.50, 2.50]

    gst = float(0.1)
    takeAway = float(0.05)

    data = 0
    x = 0
    count = 0

    menu1 = ""
    menu2 = ""
    menu3 = ""
    menu4 = ""

    qty1 = 0
    qty2 = 0
    qty3 = 0
    qty4 = 0

    price1 = 0
    price2 = 0
    price3 = 0
    price4 = 0

    order_cups = 0
    order_choice = ""

    orderItems = []
    orderPrice = []
    order_qty = []

    nextItem = True

    # user can choose a mode of operation
    mode_op = input("Select Mode of Operation. New Order [1] or Daily Summary [2]: ")

    if mode_op == "1":
        order_ID = order_ID + 1
        choice = input("Takeaway [1] or Dine in [2]? ")
        if choice == "1":
            t_count += 1
            order_choice = "Takeaway"
        else:
            d_count += 1
            order_choice = "Dine-In"

        # prints all item from the menu
        print("Here is the menu:\n ")
        print(f"[1]\t  {menu[0]}\t$3.00")
        print(f"[2]\t  {menu[1]}\t\t$2.25")
        print(f"[3]\t  {menu[2]}\t\t\t$2.50")
        print(f"[4]\t  {menu[3]}\t$2.50")
        print("\nTo complete order, enter [5] ")

        # loop where user can enter items and their quantities to the order
        while nextItem:
            order = input("Enter Item Number [1-5]: ")
            if order == "1":
                qty = int(input("Enter Quantity: "))
                orderItems.append(menu[0])
                orderPrice.append(prices[0] * qty)
                order_qty.append(qty)
                count = count + 1
                menu1 = menu[0]
                qty1 = qty
                price1 = prices[0] * qty
                order_cups = order_cups + qty
                gst_collected.append(prices[0] * qty * gst)
                if choice == "2":
                    t_price.append(prices[0] * qty + prices[0] * qty * gst)
                else:
                    t_price.append(prices[0] * qty + prices[0] * qty * gst + prices[0] * qty * takeAway)
            elif order == "2":
                qty = int(input("Enter Quantity: "))
                orderItems.append(menu[1])
                orderPrice.append(prices[1] * qty)
                order_qty.append(qty)
                count = count + 1
                menu2 = menu[1]
                qty2 = qty
                price2 = prices[1] * qty
                order_cups = order_cups + qty
                gst_collected.append(prices[1] * qty * gst)
                if choice == "2":
                    t_price.append(prices[1] * qty + prices[1] * qty * gst)
                else:
                    t_price.append(prices[1] * qty + prices[1] * qty * gst + prices[1] * qty * takeAway)
            elif order == "3":
                qty = int(input("Enter Quantity: "))
                orderItems.append(menu[2])
                orderPrice.append(prices[2] * qty)
                order_qty.append(qty)
                count = count + 1
                menu3 = menu[2]
                qty3 = qty
                price3 = prices[2] * qty
                order_cups = order_cups + qty
                gst_collected.append(prices[2] * qty * gst)
                if choice == "2":
                    t_price.append(prices[2] * qty + prices[2] * qty * gst)
                else:
                    t_price.append(prices[2] * qty + prices[2] * qty * gst + prices[2] * qty * takeAway)
            elif order == "4":
                qty = int(input("Enter Quantity: "))
                orderItems.append(menu[3])
                orderPrice.append(prices[3] * qty)
                order_qty.append(qty)
                count = count + 1
                menu4 = menu[3]
                qty4 = qty
                price4 = prices[3] * qty
                order_cups = order_cups + qty
                gst_collected.append(prices[3] * qty * gst)
                if choice == "2":
                    t_price.append(prices[3] * qty + prices[3] * qty * gst)
                else:
                    t_price.append(prices[3] * qty + prices[3] * qty * gst + prices[3] * qty * takeAway)
            # exits ordering loop and prints order summary
            elif order == "5":
                nextItem = False
                print("Here is your order summary:")
                a = 0
                sub_total = sum(orderPrice)

                # prints ordered items with their quantities and prices
                while a < count:
                    print(f"Item:\t{orderItems[a]}")
                    print(f"Qty:\t{order_qty[a]}")
                    print(f"Price:\t${orderPrice[a]:.2f}")
                    a = a + 1
                if choice == "1":

                    # prints different charges
                    total = round(sub_total + (sub_total * takeAway) + (sub_total * gst), 2)
                    print(f"Surcharge:\t${sub_total * takeAway:.2f}")
                    print(f"GST:\t\t${sub_total * gst:.2f}")
                    print(f"Total:\t\t${total:.2f}")

                    # payment calculations system
                    checkout = True
                    while checkout:
                        payment = float(input("Enter Payment Amount: "))
                        if payment == total:
                            print("Payment Complete")
                            checkout = False
                        elif payment < total:
                            total = round(total - payment, 2)
                            print(f"You still owe: ${round(total, 2):.2f}")
                        else:
                            print(f"Your Change is: ${round(total - payment, 2) * -1:.2f}")
                            print("Payment Complete")
                            checkout = False
                else:
                    total = round(sub_total + sub_total * gst, 2)
                    print(f"GST: \t${sub_total * gst:.2f}")
                    print(f"Total:\t${total:.2f}")

                    # payment calculations system
                    checkout = True
                    while checkout:
                        payment = float(input("Enter Payment Amount: "))
                        if payment == total:
                            print("Payment Complete")
                            checkout = False
                        elif payment < total:
                            total = round(total - payment, 2)
                            print(f"You still owe: ${round(total, 2):.2f}")
                        else:
                            print(f"Your Change is: ${round(total - payment, 2) * -1:.2f}")
                            print("Payment Complete")
                            checkout = False

                # allows user to close program if day has ended
                end_day = input("Is it the end of the day? [Y/N] ")
                if end_day == "Y":
                    program = False
            else:
                print("Invalid input")

        data1 = [order_ID, order_choice, menu1, qty1, price1, menu2, qty2, price2, menu3, qty3, price3, menu4, qty4,
                 price4, order_cups, round(sum(orderPrice) * gst, 2), 0,
                 round(sum(orderPrice) + sum(orderPrice) * gst, 2)]

        data2 = [order_ID, order_choice, menu1, qty1, price1, menu2, qty2, price2, menu3, qty3, price3, menu4, qty4,
                 price4, order_cups, round(sum(orderPrice) * gst, 2), round(sum(orderPrice) * takeAway, 2),
                 round(sum(orderPrice) + sum(orderPrice) * gst + sum(orderPrice) * takeAway, 2)]

        # depending on choice data is set data1 or data2
        if choice == "1":
            data = data2
        else:
            data = data1

        with open('daily_summary.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

            total_cups = qty1 + qty2 + qty3 + qty4
            total_gst = sum(gst_collected)
            daily_income = sum(t_price)

    # daily summary opens in excel
    elif mode_op == "2":
        header_2 = ["ORDERS_COUNT", "DINE-IN", "TAKE-AWAY", "CUPS_COUNT", "GST_COLLECTED", "DAILY_INCOME"]
        data3 = [order_ID, d_count, t_count, total_cups, round(total_gst, 2), round(daily_income, 2)]

        with open('daily_summary.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header_2)
            writer.writerow(data3)
        os.system("start EXCEL.EXE daily_summary.csv")

        # allows user to close program if day has ended
        end_day = input("Is it the end of the day? [Y/N] ")
        if end_day == "Y":
            program = False

