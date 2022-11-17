import menufunctions as f
f.courier_order()
f.productlist()

orders = [{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}]
def main_menu():
    print("[1] Print product menu")
    print("[2] Orders menu")
    print("[0] Exit app")

def product_menu():
    print("[1] Print product list")
    print("[2] Create a new product")
    print("[3] Update existing product")
    print("[4] Delete product")
    print("[0] Return to main menu")


def orders_menu():
    print("[1] View orders")
    print("[2] Add new order")
    print("[3] Update order status")
    print("[4] Amend order")
    print("[5] Delete order")
    print("[0] Return to main menu")

def couriers_menu():
    print("[1] View courier")
    print("[2] Add new courier")
    print("[3] Change courier")
    print("[4] Delete courier")
    print("[0] Return to main menu")
   


main_menu()
mmenu_option = input("Enter your option: ")
while mmenu_option != 0:
    if mmenu_option == '1':
        print()
        product_menu()
        product_option = input("Enter your option: ")
        while product_option != '0':
            if product_option == '1':
                print(f.productlist)
            elif product_option == '2':
                f.create_product()
                print()
                product_menu()
                product_option = input("Enter your option: ")
            elif product_option == '3':
                f.update_product()
                print()
                product_menu()
                product_option = input("Enter your option: ")
            elif product_option == '4':
                f.delete_product()
                print()
                product_menu()
                product_option = input("Enter your option: ")
            else:
                print("invalid option. Enter 1-4")
                break
            print()
            main_menu()
            mmenu_option = input("Enter your option: ")
    elif mmenu_option == '2':
        print()
        orders_menu()
        order_option = input("Enter your option: ")
        while order_option != '0':
            if order_option == '1':
                print(orders)
            elif order_option == '2':
                 print("Add new order")
                 orders.append(
                {
            "name": input("Please enter customer name: "),
            "address": input("Please enter customer's address: "),
             "phone": input("Please enter customer's telephone number: "),
            "status": 'Preparing'
            }
            )
                 print(orders)
                 print("Order placed. Returning to orders menu.")
            elif order_option == '3':
                for orders in orders:
                    if orders['name'] == [input('Input customer name: ')]:
                        orders['status'] = input("please enter current order status: ")
                        print(orders)       
            elif order_option == '4':
                for index, emp in enumerate(orders):
                    enter_customer_name = input("Enter name of customer: ")
                    if enter_customer_name == emp['name']:
                        change = input("enter what you would like to change: ")
                        if change == 'name':
                            orders[index]['name'] = input("Enter customer's name: ")
                        elif change == 'address':
                            orders[index]['address'] == input("Enter customer's address: ")
                        elif change == 'number':
                            orders[index]['number'] == input("Enter customer's number: ")
                        else: 
                            print("Invalid change selection")
                            break
                        print(orders)
                        print("order updated, returning to order menu")
            elif order_option == '5':
                print(orders)
                enter_customer_name = input("Enter customer's name you would like to delete: ")
                for index, emp in enumerate(orders):
                    if enter_customer_name == emp['name']:
                        confirm = input("Do you want to delete, type yes: ")
                        if confirm == 'yes':
                            del orders[index]      
                            break    
            else: 
                print()
                main_menu()
                mmenu_option = input("Enter your option: ")      
    elif mmenu_option == '3':
        print()
        couriers_menu()
        courier_option = input("Enter your option: ")
        while courier_option != '0':
            if courier_option == '1':
                print(f.couriers)
                print()
                couriers_menu()
                courier_option = input("Enter your option: ")
            elif courier_option == '2':
                f.create_courier()
                print()
                couriers_menu()
                courier_option = input("Enter your option: ")
            elif courier_option == '3':
                f.update_courier()
                print()
                couriers_menu()
                courier_option = input("Enter your option: ")
            elif courier_option == 4:
                f.delete_courier()
                print()
                couriers_menu()
                courier_option = input("Enter your option: ")
            print()
            main_menu()
            mmenu_option = input("Enter your option: ")
        
else:
    confirm = input("would you like to exit, type 'yes': ")
    if confirm == "yes":
        f.savexit_products()
        f.savexit_couriers()
        exit()

            