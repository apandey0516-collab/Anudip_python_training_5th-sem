#program to display shopping cart bill
cart_price=0
while(True):
    item_price=int(input("Enter Item Price :"))
    if(item_price==0):
        print("Total Bill Amount:",cart_price)
        break
    else:
        cart_price+=item_price