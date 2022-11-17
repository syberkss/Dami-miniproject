productlist = ["Egg Mayo", "Tuna Cucumber", "Club Sandwich", "Black Americano", "Coke Zero", "Ice Tea"]
def product_menu():
    print("[1] Print product list")
    print("[2] Create a new product")
    print("[3] Update existing product")
    print("[4] Delete product")
    print("[0] exit")


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
exit()
