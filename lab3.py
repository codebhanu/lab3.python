
shoppingCart = {}
print("WELCOME TO ARMOANDO SHOPPING SITE")
print("1.Add product to the cart.")
print("2.Search the product.")
print("3.Delete the product from the cart.")
print("4.Quit.")


while True:
    chice = int(input("Enter your choice(1,2,3,4): "))
    if chice == 1:
        number_of_items = int(input("Enter the number of items to be added to Stationary shop:"))
        if number_of_items < 5:
            for i in range(number_of_items):
                item = input("Enter an items:")
                brand = input("Enter the brand:")
                shoppingCart[item] = brand
            print("you aded following items to the cart")
            for item, brand in shoppingCart.items():
                print(f"{item}: {brand}")
        elif number_of_items < 0:
            print("invalid input")

        else:
            print("Cart is full")

    elif chice == 2:
        searched = input("Enter the items to be searched:")

        if searched in shoppingCart:
           print(f"{searched}:{shoppingCart[searched]}")
        else:
            print("Items does not exist")
    elif chice == 3:
        delit = input("Enter the item to be removed:")
        if delit in shoppingCart:
            shoppingCart.pop(delit)
            print("Product removed from cart")
        else:
            print("items does not exist")
    elif chice == 4:
        print("Thank you for using this shopping site")
        break

    else:
        print("Wrong option Entered")
