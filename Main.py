# ----------------------------------------------------------------------------
# Import
from Cart import Cart
from Product import Product
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    # ------------------------------------------------------------------------

    cart = Cart()
    print ("\n------------------------------------------------------------------------\n")

    # ------------------------------------------------------------------------
    # Create Products
    # ------------------------------------------------------------------------
    p1 = Product(1,"Mythos","Book written by British author Stephen Fry, published in 2017. It is a retelling of a number of Ancient Greek myths selected by Fry.",7.99)
    p2 = Product(2,"Bose NC 700","Keep your phone in your pocket and your head up to the world with easy access to voice assistants for music, navigation, weather and more",349.99)
    p3 = Product(3,"Audemars Piguet Code 11:59 Selfwinding","One of the more controversial launches of 2019 was the Code 11:59 from Audemars Piguet, a whole new collection of classical watches to sit alongside the sportier Royal Oak.",26200,2)
    p4 = Product(4, "Ray-Ban Aviator","Protect your eyes with style made famous by aviators since 1937. Ray-Ban RB3025 Large Metal Aviator Sunglasses are superior unisex glasses with multiple frame and lens options.",80)
    p5 = Product(5, "Ray-Ban Aviator","Protect your eyes with style made famous by aviators since 1937. Ray-Ban RB3025 Large Metal Aviator Sunglasses are superior unisex glasses with multiple frame and lens options.",80)
    p6 = Product(6, "Ray-Ban Aviator","Protect your eyes with style made famous by aviators since 1937. Ray-Ban RB3025 Large Metal Aviator Sunglasses are superior unisex glasses with multiple frame and lens options.",80)
    p7 = Product(7, "Ray-Ban Aviator","Protect your eyes with style made famous by aviators since 1937. Ray-Ban RB3025 Large Metal Aviator Sunglasses are superior unisex glasses with multiple frame and lens options.",80)
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Add Product To Cart
    # ------------------------------------------------------------------------
    cart.addItem(p1)
    cart.addItem(p2)
    cart.addItem(p3)
    cart.addItem(p4)
    cart.addItem(p5)
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Quantity Control
    # ------------------------------------------------------------------------
    cart.increaseQuantity(p1,6)
    cart.increaseQuantity(p3, 2)

    cart.decreaseQuantity(p1,1)
    cart.decreaseQuantity(p3,1)
    # ------------------------------------------------------------------------


    # ------------------------------------------------------------------------
    # Failsafe Testing
    # ------------------------------------------------------------------------
    cart.addItem(p2)
    cart.increaseQuantity(p1, -6)
    cart.decreaseQuantity(p2, -1)
    cart.decreaseQuantity(p6, 1)
    # ------------------------------------------------------------------------



    # ------------------------------------------------------------------------
    # Cart Display
    # ------------------------------------------------------------------------
    cart.display()
    # ------------------------------------------------------------------------



# ----------------------------------------------------------------------------