productlist = ["Egg Mayo", "Tuna Cucumber", "Club Sandwich", "Black Americano", "Coke Zero", "Ice Tea"]
orders = [{
 "name": "John",
 "address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "number": "0789887334",
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


main_menu()
option = input("Enter your option: ")
while option != 0:
    if option == '1':
        print()
        product_menu()
        option = input("Enter your option: ")
    elif option == '2':
        print()
        orders_menu()
        option = input("Enter your option: ")
    else:
        print("invalid option. Enter 0-2")
        break
exit

product_menu()
option = input("Enter your option: ")
while option != '0':
    if option == '1':
        print(productlist)
    elif option == '2':
        addproduct = input("Add product name: ")
        productlist.append(addproduct)
        print(productlist)
    elif option == '3':
        oldname = input("Type in old name: ")
        newname = input("Enter new name: ")
        i = productlist.index(oldname)
        productlist[i] = newname
        print(productlist)
    elif option == '4':
        deleteproduct = input("Type in the name of item you would like to remove: ")
        productlist.remove(deleteproduct)
        print(productlist)
    else:
        print("invalid option. Enter 0-4")

    print()
    product_menu()
    option = input("Enter your option: ")
main_menu()
option = input("Enter your option: ")

 
orders_menu()
option = (input("Enter your option: "))
while option != '0':
    if option == '1':
        print(orders)
    elif option == '2':
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
    elif option == '3':
        for orders in orders:
            if orders['name'] == [input('Input customer name: ')]:
                orders['status'] = input("please enter current order status: ")
            print(orders)       
    elif option == '4':
        for index, emp in enumerate(orders):
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
    elif option == '5':
        print(orders)
        enter_customer_name = input("Enter customer's name you would like to delete: ")
        for index, emp in enumerate(orders):
            if enter_customer_name == emp['name']:
                confirm = input("Do you want to delete, type yes: ")
                if confirm == 'yes':
                    del orders[index]      
                    break     
    else: 
        print("Invalid input")

    print()
    orders_menu()
    option = input("Enter your option: ")
main_menu()
option = input("Enter your option: ")