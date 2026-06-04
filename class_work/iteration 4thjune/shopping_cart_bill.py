#program to display shopping cart bill
cart_price=0 #to initialize the total price of items in the shopping cart to zero
while(True): #to create an infinite loop for adding items to the shopping cart until the user decides to stop by entering a price of zero
    item_price=int(input("Enter Item Price :")) #to get the price of an item from the user and convert it to an integer for calculation
    if(item_price==0): #to check if the entered item price is zero, which indicates that the user has finished adding items to the shopping cart
        print("Total Bill Amount:",cart_price) #to display the total bill amount for the items in the shopping cart
        break #to exit the loop if the user has finished adding items to the shopping cart
    else: #to handle the case where the entered item price is not zero, which means the user wants to add the item to the shopping cart
        cart_price+=item_price #to add the price of the current item to the total cart price and continue the loop to allow the user to add more items until they enter a price of zero to finish