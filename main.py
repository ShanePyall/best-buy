import products
import store
import promotions

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def empty_str_checker(data):
    # If string is empty return False.
    if data == '':
        return False
    return True


def input_validator(data):
    try:
        int(data)
        if int(data) > 0:
            return True
        return "Please enter number larger than 0"
    except ValueError:
        return "Please only enter numbers"


def start(store_object):
    # while loop until 'Quit' is prompted
    while True:
        option = int(input('''~~~~~~~
    Store Catalogue
    -_-_-_-_-_-_-_-

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: '''))

        if option == 1:
            # returns the list of products in the store.
            num = 1
            print("~~~~~~~")
            for item in store_object.product_list:
                if item.is_active():
                    print(f"{num}. {item.show()}")
                    num += 1

        elif option == 2:
            # returns the quantity of all items in store
            print(f"~~~~~~~\n{store_object.get_total_quantity()} items total in store!")

        elif option == 3:
            # places an order of item name and qnt.
            num = 1
            print("~~~~~~~")

            # Displays a list of active products and assigns a num to help retrieve later.
            product_list_key = []
            for item in store_object.product_list:
                if item.is_active():
                    print(f"{num}. {item.show()}")
                    num_to_item = num, item
                    product_list_key.append(num_to_item)
                    num += 1

            total = 0
            while True:
                # Will break once no values is entered in bot inputs.
                item_num = input("\nWhat # product do you want? (leave fields empty if you'd like to checkout): ")
                quantity = input("How many: ")

                if empty_str_checker(item_num) is False and empty_str_checker(quantity) is False:
                    print("Nothing was entered, so we will exit the order process.")
                    break
                if empty_str_checker(item_num) is False or empty_str_checker(quantity) is False:
                    print("Please ensure both fields are either empty of filled.")
                    continue

                if input_validator(item_num) == str:
                    print(input_validator(item_num))
                    continue
                if input_validator(quantity) == str:
                    print(input_validator(quantity))
                    continue

                try:
                    item = None
                    for key in product_list_key:
                        if int(item_num) == key[0]:
                            item = key[1]
                    if item is None:
                        raise UnboundLocalError
                    sub_total, message = store_object.order((item, int(quantity)))
                    print(message)
                    total += sub_total

                except UnboundLocalError:
                    print("Invalid # was entered for product.")

            print(f"Your total is £{total}")

        elif option == 4:
            break
        else:
            continue


if __name__ == "__main__":
    start(best_buy)
