productlist = []
couriers = []

def productlist():
    f = open('productlist.txt', 'r')
    products = f.read()
    print (products)


def create_product():
    addproduct = input("Add product name: ")
    productlist.append(addproduct)
    print(productlist)

def update_product():
     for product in enumerate(productlist):
            print(product)
            oldname = input("Type in old name: ")
            newname = input("Enter new name: ")
            i = productlist.index(oldname)
            productlist[i] = newname
            print(productlist)

def delete_product():
    for product in enumerate(productlist):
        print(product)
        deleteproduct = input("Type in the name of item you would like to remove: ")
        productlist.remove(deleteproduct)
        print(productlist)

def courier_order(): 
    f = open('couriers.txt', 'r')
    couriers = f.read()
    print (couriers)

def create_courier():
    addcourier = input("Add product name: ")
    couriers.append(addcourier)
    print(couriers)

def update_courier():
    for courier in enumerate(couriers):
            print(courier)
            oldname = input("Type in old name: ")
            newname = input("Enter new name: ")
            i = couriers.index(oldname)
            couriers[i] = newname
            print(couriers)
     
def delete_courier():
     for courier in enumerate(couriers):
            print(courier)
            deletecourier = input("Type in the name of item you would like to remove: ")
            couriers.remove(deletecourier)
            print(couriers)

    
def savexit_products():
    f = open('productlist.txt','w')
    for products in productlist:
         f.write(f'{products}\n') 
         f.close()

def savexit_courier():
    f = open('people.txt','w')
    for courier in couriers:
        f.write((f'{couriers}\n') ) 
        f.close()