# ----------------------------------------------------------------------------
class Cart:
    # ------------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------------
    def __init__(self):
        self.cart = []
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Items
    # These Function Are Used To Add Or Remove Items In The Cart with Fail-
    # Safe Measures for Checking For Existence
    # ------------------------------------------------------------------------
    def addItem(self,product):
        if(self.isInCart(product)):
            print("Product '"+product.name + "' Is Already In The Cart")
        else:
            self.cart.append(product)
            print("Product Added '" + product.name + "' To Cart")

    def removeItem(self,product):
        if(self.isInCart(product)):
            self.cart.remove(product)
            print("Product Removed '" + product.name + "' From Cart")
        else:
            print("Can't Remove Product Which Isn't In The Cart")
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Quantity Control
    # These Function Are Used To Increase / Decrease The Quantity with Fail-
    # Safe Measures for Checking For Existence
    # ------------------------------------------------------------------------
    def increaseQuantity(self,product,quantity=1):
        if(self.isInCart(product)):
            for p in self.cart:
                if(p == product):
                    p.increaseQuantity(quantity)
                    print("Quantity Increased : '" +p.getName() + "' By " + str(quantity))

    def decreaseQuantity(self,product,quantity=1):
        if(self.isInCart(product)):
            for p in self.cart:
                if(p == product):
                    p.decreaseQuantity(quantity)
                    print("Quantity Decreased : '" + p.getName() + " By "'' + str(quantity))
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Existance Check
    # This Function Checks If A Product Is In The Cart
    # ------------------------------------------------------------------------
    def isInCart(self, product):
        for p in self.cart:
            if (p == product):
                return True
        return False
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Display Function
    # This Function Display The Contents Of The Cart
    # ------------------------------------------------------------------------
    def display(self):
        print("\n------------------------------------------------------------------------------------------------------")
        print("Your Cart")
        print("------------------------------------------------------------------------------------------------------")
        for p in self.cart:

            p.display()
            print("\t------------------------------------------------------------------------------------------------")

        print("\n\n\t------------------------------------------------------------------------------------------------")
        print("\tGrand Total : $ " + str(self.getGrandTotal()))
        print("\t------------------------------------------------------------------------------------------------")

        print("\n\n----------------------------------------------------------------------------------------------------")
    # ------------------------------------------------------------------------



    # ------------------------------------------------------------------------
    # Grand Total
    # This Function Calulates All The Prices Of The Items In The Cart
    # ------------------------------------------------------------------------
    def getGrandTotal(self):
        total = 0

        for p in self.cart:
            total += p.getTotalPrice()

        return total
    # ------------------------------------------------------------------------


# ----------------------------------------------------------------------------
