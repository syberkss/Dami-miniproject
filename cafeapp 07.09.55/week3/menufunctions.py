products = []
couriers = []


def productlist():
    f = open('productlist.txt', 'r')
    product = f.read()
    print(product)


def create_product():
    with open("productlist.txt", "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0 :
             f.write("\n")
        f.write(input("Add product name: "))
        

def update_product():
    oldname = input("Type in old name: ")
    newname = input("Enter new name: ")
    with open("productlist.txt", "r") as f:
        data = f.read()
        data = data.replace(oldname, newname)
    with open(r"productlist.txt", "w") as f:
         f.write(data)
         print("product changed!")

def delete_product():
    deleteproduct = input("Enter the value you wish to delete: ")
    with open("productlist.txt", "r") as f:
        data = f.readlines()
    with open("productlist.txt", "w") as f:
        for line in data:
            words = line.strip("\n").lower().split(' ')
            if deleteproduct.lower() not in words:
                f.write(line)

def courierlist(): 
    f = open('couriers.txt', 'r')
    courier = f.read()
    print (courier)

def create_courier():
    with open("courierlist.txt", "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0 :
             f.write("\n")
        f.write(input("Add courier name: "))
        

def update_courier():
    oldname = input("Type in old name: ")
    newname = input("Enter new name: ")
    with open("courierlist.txt", "r") as f:
        data = f.read()
        data = data.replace(oldname, newname)
    with open(r"courier.txt", "w") as f:
         f.write(data)
         print("courier changed!")

def delete_courier():
    deletecourier = input("Enter the value you wish to delete: ")
    with open("courierlist.txt", "r") as f:
        data = f.readlines()
    with open("courierlist.txt", "w") as f:
        for line in data:
            words = line.strip("\n").lower().split(' ')
            if deletecourier.lower() not in words:
                f.write(line)

    
def savexit_products():
    f = open('productlist.txt','w')
    for products in productlist:
         f.write(f'{products}\n') 
         f.close()

def savexit_courier():
    f = open('people.txt','w')
    for courier in courierlist:
        f.write((f'{courier}\n') ) 
        f.close()