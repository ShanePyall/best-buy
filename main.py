import products
import store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_object):
    # while loop until 'Quit' is promted
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
            for item in best_buy.product_list:
                print(item.show())
                num += 1

        elif option == 2:
            # returns the quantity of all items in store
            print(f"~~~~~~~\n{best_buy.get_total_quantity()} Items total in store!")

        elif option == 3:
            # places an order of item name and qnt.
            num = 1
            print("~~~~~~~")
            for item in best_buy.product_list:
                print(f"{num}. {item.show()}")
                num += 1

            total = 0
            while True:
                # Will break once no values is entered in bot inputs.
                item_num = input("\nWhat product you want (please enter the number associated): ")
                quantity = input("How many: ")
                if item_num == '' and quantity == '':
                    print("Nothing was entered, so we will exit the order process.")
                    break
                try:
                    sub_total, message = best_buy.order([(item_num, quantity)])
                    print(message)
                    total += sub_total

                except ValueError:
                    print("Please ensure the fields are filled out as guided.")
                except IndexError:
                    print("Please only enter a number associated with a product.")
            print(f"Your total is £{total}")

        elif option == 4:
            break
        else:
            continue


if __name__ == "__main__":
    start(best_buy)
