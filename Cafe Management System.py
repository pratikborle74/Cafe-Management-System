import pandas as pd
import matplotlib.pyplot as plt

while True:
    print("\nWelcome to Cafe Management System!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    user_type = input("Enter your choice: ")

    if user_type == '1':
        customer_name = input("Enter your name: ")
        customer_email = input("Enter your email: ")
        customer_phone = input("Enter your phone number: ")
        customer_address = input("Enter your address: ")

        try:
            customers = pd.read_csv("customers.csv")
        except FileNotFoundError:
            customers = pd.DataFrame(columns=["Name", "Email", "Phone", "Address"])
            customers.to_csv("customers.csv", index=False)

        customer_data = pd.DataFrame([[customer_name, customer_email, customer_phone, customer_address]])
        customer_data.to_csv("customers.csv", mode="a", header=False, index=False)

        while True:
            print("\nCustomer Menu:")
            print("1. Place Order")
            print("2. View Order Summary")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                while True:
                    print("\nMenu:")
                    print("1. Coffee")
                    print("2. Tea")
                    print("3. Desserts")
                    print("4. Burgers")
                    print("5. Pizzas")
                    print("6. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        menu_type = "coffee"
                    elif choice == "2":
                        menu_type = "tea"
                    elif choice == "3":
                        menu_type = "desserts"
                    elif choice == "4":
                        menu_type = "burgers"
                    elif choice == "5":
                        menu_type = "pizzas"
                    elif choice == "6":
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
                        continue

                    try:
                        menu_items = pd.read_csv(menu_type + "_menu.csv")
                    except FileNotFoundError:
                        print("No", menu_type, "items available.")
                        continue

                    while True:
                        print("\n", menu_type.capitalize(), "Menu:")
                        for index, item in menu_items.iterrows():
                            print(index + 1, ".", item['Item'], " - ₹", item['Price'])

                        item_key = input("Enter the number of the item you want to purchase (or '0' to exit): ")

                        if item_key == '0':
                            break
                        elif item_key.isdigit() and 1 <= int(item_key) <= len(menu_items):
                            item_name = menu_items.iloc[int(item_key) - 1]['Item']
                            item_price = menu_items.iloc[int(item_key) - 1]['Price']

                            quantity = input("Enter the quantity: ")

                            if quantity.isdigit() and int(quantity) > 0:
                                customer_order = pd.DataFrame([[item_name, item_price, int(quantity)]], columns=["Item", "Price", "Quantity"])

                                try:
                                    existing_order = pd.read_csv(customer_name + "_order.csv")
                                    customer_order.to_csv(customer_name + "_order.csv", mode="a", header=False, index=False)
                                except FileNotFoundError:
                                    customer_order.to_csv(customer_name + "_order.csv", index=False)

                                print("Item added to your order successfully!")
                            else:
                                print("Invalid quantity. Please enter a positive integer.")
                        else:
                            print("Invalid choice. Please choose a valid option.")

                try:
                    customer_order = pd.read_csv(customer_name + "_order.csv")
                    print("\nOrder Summary:")
                    print(customer_order)
                    total_revenue = (customer_order['Price'].astype(float) * customer_order['Quantity'].astype(int)).sum()
                    print("Order Total: ₹", total_revenue)
                except FileNotFoundError:
                    print("No order placed.")

            elif choice == "2":
                try:
                    customer_order = pd.read_csv(customer_name + "_order.csv")
                    print("\nOrder Summary:")
                    print(customer_order)
                    total_revenue = (customer_order['Price'].astype(float) * customer_order['Quantity'].astype(int)).sum()
                    print("Order Total: ₹", total_revenue)
                except FileNotFoundError:
                    print("No order placed.")

            elif choice == "3":
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    elif user_type == '2':
        while True:
            print("\nAdmin Menu:")
            print("1. Manage Menu")
            print("2. View All Products")
            print("3. View All Customers")
            print("4. View Price Distribution")
            print("5. View Revenue Purchased by Each Customer")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nManage Menu:")
                print("1. Coffee")
                print("2. Tea")
                print("3. Desserts")
                print("4. Burgers")
                print("5. Pizzas")

                menu_choice = input("Enter your choice: ")

                if menu_choice == "1":
                    menu_type = "coffee"
                elif menu_choice == "2":
                    menu_type = "tea"
                elif menu_choice == "3":
                    menu_type = "desserts"
                elif menu_choice == "4":
                    menu_type = "burgers"
                elif menu_choice == "5":
                    menu_type = "pizzas"

                try:
                    menu_items = pd.read_csv(menu_type + "_menu.csv")
                except FileNotFoundError:
                    menu_items = pd.DataFrame(columns=["Item", "Price"])
                    menu_items.to_csv(menu_type + "_menu.csv", index=False)

                while True:
                    print("\nManage", menu_type.capitalize(), "Menu:")
                    print("1. Add Item")
                    print("2. Remove Item")
                    print("3. Exit")

                    manage_choice = input("Enter your choice: ")

                    if manage_choice == "1":
                        item_name = input("Enter the name of the item: ")
                        item_price = input("Enter the price of the item: ")

                        item_data = pd.DataFrame([[item_name, item_price]])
                        item_data.to_csv(menu_type + "_menu.csv", mode="a", header=False, index=False)

                        print("Item added successfully!")

                    elif manage_choice == "2":
                        print("\n", menu_type.capitalize(), "Menu:")
                        for index, item in menu_items.iterrows():
                            print(index + 1, ".", item['Item'], " - ₹", item['Price'])

                        item_key = input("Enter the number of the item you want to remove: ")

                        if item_key.isdigit() and 1 <= int(item_key) <= len(menu_items):
                            menu_items.drop(menu_items.index[int(item_key) - 1], inplace=True)
                            menu_items.to_csv(menu_type + "_menu.csv", index=False)

                            print("Item removed successfully!")

                    elif manage_choice == "3":
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")

            elif choice == "2":
                menu_files = ["coffee_menu.csv", "tea_menu.csv", "desserts_menu.csv", "burgers_menu.csv", "pizzas_menu.csv"]
                for menu_file in menu_files:
                    try:
                        menu_items = pd.read_csv(menu_file)
                        print(f"\n{menu_file.split('_')[0].capitalize()} Menu:")
                        for index, item in menu_items.iterrows():
                            print(index + 1, ".", item['Item'], " - ₹", item['Price'])
                    except FileNotFoundError:
                        print(f"No {menu_file.split('_')[0]} items available.")

            elif choice == "3":
                try:
                    customers = pd.read_csv("customers.csv")
                    print("\nCustomers:")
                    for index, customer in customers.iterrows():
                        print(index + 1, ".", customer['Name'], " - ", customer['Email'], " - ", customer['Phone'], " - ", customer['Address'])
                except FileNotFoundError:
                    print("No customers available.")

            elif choice == "4":
                menu_files = ["coffee_menu.csv", "tea_menu.csv", "desserts_menu.csv", "burgers_menu.csv", "pizzas_menu.csv"]
                for menu_file in menu_files:
                    try:
                        menu_items = pd.read_csv(menu_file)
                        menu_prices = menu_items['Price'].astype(float)
                        plt.hist(menu_prices, bins=5)
                        plt.xlabel("Price")
                        plt.ylabel("Frequency")
                        plt.title(f"{menu_file.split('_')[0].capitalize()} Price Distribution")
                        plt.show()
                    except FileNotFoundError:
                        print(f"No {menu_file.split('_')[0]} items available.")

            elif choice == "5":
                customer_files = ["customers.csv"]
                customer_revenues = []
                customer_names = []

                for customer_file in customer_files:
                    try:
                        customer_orders = pd.read_csv(customer_file)
                        for index, customer in customer_orders.iterrows():
                            customer_name = customer['Name']
                            try:
                                order_items = pd.read_csv(customer_name + "_order.csv")
                                total_revenue = (order_items['Price'].astype(float) * order_items['Quantity'].astype(int)).sum()
                                customer_names.append(customer_name)
                                customer_revenues.append(total_revenue)
                            except FileNotFoundError:
                                continue
                    except FileNotFoundError:
                        continue

                if customer_names and customer_revenues:
                    plt.bar(customer_names, customer_revenues)
                    plt.xlabel("Customer Name")
                    plt.ylabel("Revenue")
                    plt.title("Revenue Purchased by Each Customer")
                    plt.show()
                else:
                    print("No customer orders available.")

            elif choice == "6":
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    elif user_type == '3':
        break
    else:
        print("Invalid choice. Please choose a valid option.")
# hi