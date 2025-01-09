import products
import store
import sys

ui_display = """
            ---------------Store Menu---------------
            ----------------------------------------
            1. List all products in store
            2. Show total amount in store
            3. Make an order
            4. Quit
            """


def start(input_store):
    """
    The main operation of the store including user interface, handling of orders and product listing
    """

    def list_all_products_handler():
        """
        handles the product listing feature from the menu dispatcher
        """
        print("------list all products-------")
        products_list = input_store.get_all_products()
        index_num = 1
        for product in products_list:
            print(f"{index_num}. {product.show()}")
            index_num += 1
        print("------------------------------")

    def total_amount_handler():
        """
          handles the feature to display the total amount of items in the store
        """
        print("-----Total Amount of Items----")
        print(f"Total of {input_store.get_total_quantity()} items in input_store")
        print("------------------------------")

    def order_handler():
        """
          handles the ordering process in the store
        """

        print("------Order processing-------")
        print("When you want to finish order, enter empty text.")
        list_all_products_handler()
        # Create a dummy_products_list to show the user what the shop list looks like after ordering
        products_list = input_store.get_all_products()
        order_list = []
        while True:
            try:
                product_index = input("Which product # do you want?")
                amount_input = input("What amount do you want?")
                # If the product_index and amount_input are both empty, end the ordering process
                if not product_index and not amount_input:
                    # Check if the order list empty or not, if empty then no order has been made while ending the ordering process
                    if order_list:
                        total_price = input_store.order(order_list)
                        print(f"\nOrders made! Total payment: ${total_price}")
                        break
                    else:
                        print("No order has been made!")
                        break
                # Convert the input into integer
                product_index = int(product_index)
                amount_input = int(amount_input)
                # If the user enters an invalid index number while choosing the product, a warning should be raised
                if product_index < 1 or product_index > len(products_list):
                    raise Exception("The chosen index number doesn't exist on the list")
                # Check if the input amount is smaller or equal the existed amount in the warehouse
                # if smaller or equal, add the order into the list in form of a tuple with 2 elements: product_name and amount_input
                if amount_input <= products_list[product_index - 1].get_quantity():
                    # if the order_list is not empty, check whether an order of the same product already exists
                    # in the order_list, if the product exists, just add the new order amount to the existing amount of that product to
                    # prevent more tuples of the same product order
                    if order_list:
                        is_product_in_order_list = False
                        for i, product_tuple in enumerate(order_list):
                            if products_list[product_index - 1] in product_tuple:
                                order_list[i] = (products_list[product_index - 1], product_tuple[1] + amount_input)
                                is_product_in_order_list = True
                        if not is_product_in_order_list:
                            order_list.append((products_list[product_index - 1], amount_input))
                    else:
                        order_list.append((products_list[product_index - 1], amount_input))

                    print("Order for the product is added to the list")
                else:
                    raise Exception("The ordered amount is larger than the amount available in the store!")
            except ValueError:
                print("Invalid input, please enter numbers only")
            except Exception as err_msg:
                print("Invalid input! " + str(err_msg))

    def quit_handler():
        """
          escape the program
        """
        print("Thanks for visiting our store, goodbye!")
        sys.exit()

    menu_dispatch = {
        "1": list_all_products_handler,
        "2": total_amount_handler,
        "3": order_handler,
        "4": quit_handler
    }
    # Handle the user input when choosing an option available on the menu dispatcher (1 to 4)
    while True:
        try:
            user_input = int(input(ui_display + "\n"))
            if user_input <= 0 or user_input > 4:
                raise Exception("Please enter only a number between 1 and 4 (1 and 4 included)!")
        except ValueError:
            print("Invalid Input! Please only enter a number")
        except Exception as err:
            print("Invalid Input! " + str(err))
        else:
            break

    menu_dispatch[str(user_input)]()


# setup initial stock of inventory

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)

# Main program starts here

if __name__ == "__main__":
    while True:
        start(best_buy)
