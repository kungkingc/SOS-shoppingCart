# ----------------------------------------------------------------------------
# Import
from decimal import Decimal
# ----------------------------------------------------------------------------
class Product:
    # ------------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------------
    def __init__(self, id, name, description, price, quantity=1):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.totalprice = self.price*self.quantity
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Quantity Control
    # These Function Control The Quantity Of The Product With Buit-In Fail-Sa
    # fe System
    # ------------------------------------------------------------------------
    def setQuantity(self,number):
        self.quantity = number
        self.totalprice = (self.price * self.quantity)

    def increaseQuantity(self,number):
        if(number >= 1):
            self.quantity += number
            self.totalprice = (self.price * self.quantity)

    def decreaseQuantity(self,number):
        if (number >= 1):
            if(self.quantity > 0):
                self.quantity -= number
                self.totalprice = (self.price * self.quantity)
    # ------------------------------------------------------------------------



    # ------------------------------------------------------------------------
    def __eq__(self, other):
        if not isinstance(other, Product):
            return
        return ((other.id == self.id) and (other.name == self.name) and (other.description == self.description) and (other.price == self.price))

    def getTotalPrice(self):
        self.totalprice = (self.price * self.quantity)
        return self.totalprice

    def isOne(self):
        return (self.quantity == 1)
    # ------------------------------------------------------------------------



    # ------------------------------------------------------------------------
    # Getter
    # These Functions Gets The Data
    # ------------------------------------------------------------------------
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price
    # ------------------------------------------------------------------------



    # ------------------------------------------------------------------------
    # Display
    # This Function Display The Product Information
    # ------------------------------------------------------------------------
    def display(self):
        text = "\tProduct ID  : " + str(self.id)
        text += "\n\tName        : " + self.name
        text += "\n\tDescription : " + self.description
        text += "\n\tQuantity    : " + str(self.quantity)
        text += "\n\tUnit Price  : $ " + str(self.price)
        text += "\n\n\tTotal Price : $ " + str(self.totalprice)

        print(text)
    # ------------------------------------------------------------------------



# ----------------------------------------------------------------------------


